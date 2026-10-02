"""
routes/disease_routes.py
Handles leaf image upload, disease prediction using the TensorFlow
model, remedy lookup, and saving prediction history to MongoDB.
"""

import os
import uuid
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app
from bson.objectid import ObjectId

from db import disease_predictions_collection, disease_solutions_collection, get_server_time
from utils.auth_utils import login_required
from utils.validators import is_allowed_file
from utils.model_loader import predict_disease
from config import Config

disease_bp = Blueprint("disease", __name__)


@disease_bp.route("/predict-disease", methods=["GET", "POST"])
@login_required
def predict_disease_route():
    if request.method == "POST":
        # ---- Validate file presence ----
        if "leaf_image" not in request.files:
            flash("No file part in the request.", "danger")
            return redirect(url_for("disease.predict_disease_route"))

        file = request.files["leaf_image"]

        if file.filename == "":
            flash("No file selected.", "danger")
            return redirect(url_for("disease.predict_disease_route"))

        if not is_allowed_file(file.filename, Config.ALLOWED_EXTENSIONS):
            flash("Invalid file type. Allowed types: png, jpg, jpeg.", "danger")
            return redirect(url_for("disease.predict_disease_route"))

        try:
            # ---- Save file with unique name ----
            ext = file.filename.rsplit(".", 1)[1].lower()
            unique_filename = f"{uuid.uuid4().hex}.{ext}"
            filepath = os.path.join(Config.UPLOAD_FOLDER, unique_filename)
            file.save(filepath)

            # ---- Run prediction ----
            prediction = predict_disease(filepath)
            disease_name = prediction["disease_name"]
            confidence = prediction["confidence"]

            # Log for debugging
            current_app.logger.info(f"Disease detected: {disease_name} (confidence: {confidence}%)")

            # ---- Fetch remedy from disease_solutions collection ----
            remedy_doc = disease_solutions_collection.find_one({"disease_name": disease_name})
            if remedy_doc:
                cause = remedy_doc.get("cause", "Not available")
                solution = remedy_doc.get("solution", "Not available")
                current_app.logger.info(f"✓ Found remedy for: {disease_name}")
            else:
                cause = "No information available for this disease."
                solution = "Please consult an agricultural expert."
                current_app.logger.warning(f"⚠ No remedy found for: {disease_name}")
                # Try case-insensitive search
                remedy_doc = disease_solutions_collection.find_one({"disease_name": {"$regex": disease_name, "$options": "i"}})
                if remedy_doc:
                    cause = remedy_doc.get("cause", "Not available")
                    solution = remedy_doc.get("solution", "Not available")
                    current_app.logger.info(f"✓ Found remedy (case-insensitive) for: {disease_name}")

            # ---- Save prediction history ----
            prediction_doc = {
                "user_id": session["user_id"],
                "image_filename": unique_filename,
                "disease_name": disease_name,
                "confidence": confidence,
                "cause": cause,
                "solution": solution,
                "created_at": get_server_time(),
            }
            disease_predictions_collection.insert_one(prediction_doc)

            return render_template(
                "disease.html",
                result={
                    "disease_name": disease_name,
                    "confidence": confidence,
                    "cause": cause,
                    "solution": solution,
                    "image_filename": unique_filename,
                }
            )

        except Exception as e:
            current_app.logger.error(f"Disease prediction error: {e}")
            flash("An error occurred while processing the image. Please try again.", "danger")
            return redirect(url_for("disease.predict_disease_route"))

    return render_template("disease.html", result=None)
