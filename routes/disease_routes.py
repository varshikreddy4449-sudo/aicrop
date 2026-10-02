"""
routes/disease_routes.py
Handles leaf image upload, deep-learning disease prediction using MobileNetV2,
multi-language pathology lookup (cause, symptoms, chemical & organic treatments, prevention),
and prediction history persistence in MongoDB.
"""
import os
import uuid
import logging
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app, jsonify
from werkzeug.utils import secure_filename
from db import disease_predictions_collection, get_server_time
from utils.auth_utils import login_required
from utils.validators import is_allowed_file
from utils.model_loader import predict_disease
from utils.translations import get_disease_translation
from config import Config

logger = logging.getLogger("AgriAI.Disease")
disease_bp = Blueprint("disease", __name__)


@disease_bp.route("/predict-disease", methods=["GET", "POST"])
@login_required
def predict_disease_route():
    lang = session.get("language", "en")
    selected_engine = session.get("preferred_disease_engine", Config.DEFAULT_DISEASE_ENGINE)
    
    if request.method == "GET":
        return render_template(
            "disease.html",
            result=None,
            available_engines=Config.AVAILABLE_DISEASE_ENGINES,
            selected_engine=selected_engine
        )

    # Determine requested model engine
    req_engine = None
    if request.is_json and request.get_json():
        req_engine = request.get_json().get("model_engine")
    elif request.form.get("model_engine"):
        req_engine = request.form.get("model_engine")
    elif request.args.get("model_engine"):
        req_engine = request.args.get("model_engine")

    if req_engine in Config.AVAILABLE_DISEASE_ENGINES:
        selected_engine = req_engine
        session["preferred_disease_engine"] = req_engine

    # 1. Validate file presence
    file = None
    if "leaf_image" in request.files:
        file = request.files["leaf_image"]
    elif "image" in request.files:
        file = request.files["image"]

    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest" or request.is_json or "json" in request.headers.get("Accept", "")

    if not file or file.filename == "":
        msg = "Please select or drop an image file."
        if is_ajax:
            return jsonify({"error": msg}), 400
        flash(msg, "danger")
        return redirect(url_for("disease.predict_disease_route"))

    if not is_allowed_file(file.filename, Config.ALLOWED_EXTENSIONS):
        msg = "Invalid file type. Allowed formats: PNG, JPG, JPEG, WEBP."
        if is_ajax:
            return jsonify({"error": msg}), 400
        flash(msg, "danger")
        return redirect(url_for("disease.predict_disease_route"))

    try:
        # 2. Save file with safe UUID filename
        ext = file.filename.rsplit(".", 1)[1].lower()
        unique_filename = f"{uuid.uuid4().hex}.{ext}"
        filepath = os.path.join(Config.UPLOAD_FOLDER, unique_filename)
        os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
        file.save(filepath)

        # 3. Run verified prediction pipeline with selected engine
        prediction = predict_disease(filepath, engine=selected_engine)
        disease_name = prediction["disease_name"]
        confidence = prediction["confidence"]
        status = prediction["status"]
        top_predictions = prediction["top_predictions"]
        engine_used = prediction.get("engine", selected_engine)
        engine_label = prediction.get("engine_label", Config.AVAILABLE_DISEASE_ENGINES.get(engine_used, engine_used))

        # 4. Fetch rich multi-language disease information
        pathology = get_disease_translation(disease_name, lang=lang)

        # 5. Localize top predictions for UI
        localized_top = []
        for p in top_predictions:
            p_info = get_disease_translation(p["disease_name"], lang=lang)
            localized_top.append({
                "disease_key": p["disease_name"],
                "name": p_info.get("name", p["disease_name"]),
                "confidence": p["confidence"]
            })

        result_payload = {
            "disease_name":       disease_name,
            "display_name":       pathology.get("name", disease_name),
            "crop":               pathology.get("crop", "Plant"),
            "confidence":         confidence,
            "status":             status,
            "localized_status":   pathology.get("status", status),
            "cause":              pathology.get("cause", "Not available."),
            "symptoms":           pathology.get("symptoms", "Not available."),
            "solution":           pathology.get("treatment", "Consult local agricultural extension."),
            "organic_solution":   pathology.get("organic", "Maintain clean cultural practices."),
            "prevention":         pathology.get("prevention", "Practice regular crop rotation."),
            "image_filename":     unique_filename,
            "top_predictions":    localized_top,
            "engine":             engine_used,
            "engine_label":       engine_label
        }

        # 6. Save prediction history to MongoDB
        try:
            prediction_doc = {
                "user_id":        session.get("user_id"),
                "image_filename": unique_filename,
                "disease_name":   disease_name,
                "confidence":     confidence,
                "status":         status,
                "cause":          pathology.get("cause", ""),
                "solution":       pathology.get("treatment", ""),
                "model_engine":   engine_used,
                "created_at":     get_server_time(),
            }
            disease_predictions_collection.insert_one(prediction_doc)
        except Exception as db_err:
            logger.warning("Could not persist disease prediction to MongoDB: %s", db_err)

        if is_ajax:
            return jsonify(result_payload)

        return render_template(
            "disease.html",
            result=result_payload,
            available_engines=Config.AVAILABLE_DISEASE_ENGINES,
            selected_engine=engine_used
        )

    except Exception as e:
        logger.error("Disease prediction error: %s", e)
        error_msg = f"Analysis error: {str(e)}"
        if is_ajax:
            return jsonify({"error": error_msg}), 500
        flash("Could not process the uploaded image. Please ensure the photo is clear and in a supported image format.", "danger")
        return redirect(url_for("disease.predict_disease_route"))
