"""
routes/crop_routes.py
Handles crop recommendation predictions with verified model probabilities,
multi-language support, and database history tracking.
"""
from datetime import datetime, timezone
import logging
from flask import Blueprint, jsonify, render_template, request, session
from db import crop_predictions_collection, is_db_connected
from utils.auth_utils import login_required
from utils.model_loader import predict_crop, get_crop_info
from utils.validators import validate_crop_inputs
from utils.translations import get_crop_translation

logger = logging.getLogger("AgriAI.Crop")
crop_bp = Blueprint("crop", __name__)


@crop_bp.route("/predict-crop", methods=["GET", "POST"])
@login_required
def predict_crop_route():
    lang = session.get("language", "en")
    
    if request.method == "GET":
        return render_template("crop.html", result=None)

    # Accept both JSON (API calls) and standard HTML form submissions
    data = request.get_json() if request.is_json else request.form.to_dict()

    # Validate inputs
    valid, result = validate_crop_inputs(data)
    if not valid:
        if request.is_json:
            return jsonify({"error": result}), 400
        return render_template("crop.html", error=result, inputs=data, result=None)

    features = result  # Clean dict: {N, P, K, temperature, humidity, ph, rainfall}

    try:
        prediction_result = predict_crop(features)
        recommended_crop = prediction_result["recommended_crop"]
        confidence = prediction_result["confidence"]
        top_predictions = prediction_result["top_predictions"]
        
        # Localize crop details for display
        crop_details = get_crop_info(recommended_crop, lang=lang)
        
        # Localize alternative crops
        localized_alternatives = []
        for alt in top_predictions:
            alt_info = get_crop_translation(alt["crop"], lang=lang)
            localized_alternatives.append({
                "crop_key": alt["crop"],
                "crop_name": alt_info["name"],
                "confidence": alt["confidence"]
            })
            
    except Exception as e:
        logger.error("Crop prediction pipeline failure: %s", e)
        error_msg = f"Crop recommendation failed: {str(e)}"
        if request.is_json:
            return jsonify({"error": error_msg}), 500
        return render_template("crop.html", error=error_msg, inputs=data, result=None)

    # Save to MongoDB with graceful fallback
    doc = {
        "user_id":          session.get("user_id"),
        "inputs":           features,
        "recommended_crop": recommended_crop,
        "confidence":       confidence,
        "crop_details":     crop_details,
        "created_at":       datetime.now(timezone.utc),
    }
    
    try:
        crop_predictions_collection.insert_one(doc)
    except Exception as db_err:
        logger.warning("Could not persist crop prediction to MongoDB: %s", db_err)

    output = {
        "recommended_crop": recommended_crop,
        "confidence":       confidence,
        "details":          crop_details,
        "inputs":           features,
        "alternatives":     localized_alternatives
    }

    if request.is_json:
        return jsonify(output)

    return render_template("crop.html", result=output, inputs=features)