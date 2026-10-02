"""
routes/crop_routes.py
Handles crop recommendation predictions.
"""
from datetime import datetime, timezone

from flask import Blueprint, jsonify, render_template, request, session

from db import crop_predictions_collection as crop_predictions
from utils.auth_utils import login_required
from utils.model_loader import predict_crop, get_crop_info
from utils.validators import validate_crop_inputs

crop_bp = Blueprint("crop", __name__)


@crop_bp.route("/predict-crop", methods=["GET", "POST"])
@login_required
def predict_crop_route():
    if request.method == "GET":
        return render_template("crop.html")

    # Accept both JSON (API calls) and HTML form submissions
    data = request.get_json() if request.is_json else request.form.to_dict()

    # Validate inputs
    valid, result = validate_crop_inputs(data)
    if not valid:
        if request.is_json:
            return jsonify({"error": result}), 400
        return render_template("crop.html", error=result)

    features = result  # dict: {N, P, K, temperature, humidity, ph, rainfall}

    try:
        recommended_crop = predict_crop(features)
        crop_details = get_crop_info(recommended_crop)
    except Exception as e:
        error_msg = f"Prediction failed: {str(e)}"
        if request.is_json:
            return jsonify({"error": error_msg}), 500
        return render_template("crop.html", error=error_msg)

    # Save to MongoDB
    crop_predictions.insert_one({
        "user_id":          session["user_id"],
        "inputs":           features,
        "recommended_crop": recommended_crop,
        "crop_details":     crop_details,
        "created_at":       datetime.now(timezone.utc),
    })

    output = {
        "recommended_crop": recommended_crop,
        "details":          crop_details,
        "inputs":           features,
    }

    if request.is_json:
        return jsonify(output)

    return render_template("crop.html", result=output)