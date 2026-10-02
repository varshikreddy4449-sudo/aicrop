"""
app.py
Main entry point for AgriAI: AI-Powered Crop Recommendation & Leaf Disease Detection System.
Registers blueprints, configures multi-language helpers, seeds disease pathology into MongoDB,
and manages application lifecycle.
"""
import os
import logging
from flask import Flask, jsonify, render_template, request, session, redirect, url_for, send_from_directory
from werkzeug.exceptions import RequestEntityTooLarge
from config import Config
from db import (
    disease_solutions_collection,
    init_indexes,
    is_db_connected,
)
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.disease_routes import disease_bp
from routes.crop_routes import crop_bp
from utils.translations import LANGUAGES, DEFAULT_LANGUAGE, get_ui_text, DISEASES_I18N
from utils.model_loader import get_crop_model, get_disease_model

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("AgriAI.App")

app = Flask(__name__)
app.config.from_object(Config)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(disease_bp)
app.register_blueprint(crop_bp)

# Ensure upload directory exists
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)


# ── Database Initialization ───────────────────────────────────────────────────
def seed_disease_solutions():
    """Ensure all 29 disease solutions with causes and treatments are seeded into MongoDB."""
    try:
        if not is_db_connected():
            logger.warning("MongoDB not connected during seed check; proceeding with in-memory fallbacks.")
            return

        for disease_name, lang_dict in DISEASES_I18N.items():
            en_data = lang_dict.get("en", {})
            hi_data = lang_dict.get("hi", {})
            te_data = lang_dict.get("te", {})

            doc = {
                "disease_name": disease_name,
                "crop": en_data.get("crop", "General"),
                "status": en_data.get("status", "Diseased"),
                "cause": en_data.get("cause", ""),
                "symptoms": en_data.get("symptoms", ""),
                "solution": en_data.get("treatment", ""),
                "organic_solution": en_data.get("organic", ""),
                "prevention": en_data.get("prevention", ""),
                "i18n": {
                    "hi": hi_data,
                    "te": te_data
                }
            }
            disease_solutions_collection.update_one(
                {"disease_name": disease_name},
                {"$set": doc},
                upsert=True
            )
        logger.info("Verified and updated all 29 disease pathology solutions in MongoDB.")
    except Exception as e:
        logger.warning("Disease solutions seed warning: %s", e)


try:
    init_indexes()
    seed_disease_solutions()
except Exception as e:
    logger.warning("Startup database initialization: %s", e)


# ── Template Context Processor (Multi-Language) ──────────────────────────────
@app.context_processor
def inject_i18n():
    """Injects translation helper, current language, and language list to all templates."""
    current_lang = session.get("language", DEFAULT_LANGUAGE)
    if current_lang not in LANGUAGES:
        current_lang = DEFAULT_LANGUAGE

    def t(key):
        return get_ui_text(key, current_lang)

    return {
        "t": t,
        "current_lang": current_lang,
        "languages": LANGUAGES,
        "is_db_connected": is_db_connected()
    }


# ── Language Switcher Route ───────────────────────────────────────────────────
@app.route("/set-language/<lang_code>")
def set_language(lang_code):
    """Switch active session language and redirect back to previous page."""
    if lang_code in LANGUAGES:
        session["language"] = lang_code
    referrer = request.referrer
    if referrer and referrer.startswith(request.host_url):
        return redirect(referrer)
    return redirect(url_for("index"))


# ── Core Routes ───────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename: str):
    return send_from_directory(Config.UPLOAD_FOLDER, filename)


# Backwards-compatible /predict route forwarding to /predict-disease
@app.route("/predict", methods=["POST"])
def legacy_predict():
    from routes.disease_routes import predict_disease_route
    return predict_disease_route()


# ── Error Handlers ────────────────────────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", message="The requested page could not be found."), 404


@app.errorhandler(413)
def too_large(e):
    msg = "File too large. Maximum allowed size is 5MB."
    if request.is_json or request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify({"error": msg}), 413
    return render_template("500.html", message=msg), 413


@app.errorhandler(500)
def server_error(e):
    logger.error("Internal Server Error: %s", e)
    msg = "An unexpected server error occurred. Please try again."
    if request.is_json or request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify({"error": msg}), 500
    return render_template("500.html", message=msg), 500


if __name__ == "__main__":
    # Preload models at startup
    try:
        logger.info("Pre-warming crop model...")
        get_crop_model()
        logger.info("Pre-warming disease detection model...")
        get_disease_model()
        logger.info("Models preloaded successfully.")
    except Exception as e:
        logger.warning("Model pre-warming note: %s", e)

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)