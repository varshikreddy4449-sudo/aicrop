"""
utils/model_loader.py
Lazy-loads ML models as thread-safe singletons and provides validated prediction pipelines.
"""
import os
import pickle
import numpy as np
import tensorflow as tf
from PIL import Image
from config import Config
from utils.translations import get_crop_translation, get_disease_translation

# ── Model Singletons ────────────────────────────────────────────────────────
_disease_model = None
_shubham_model = None
_crop_model    = None
_crop_scaler   = None


def get_disease_model():
    global _disease_model
    if _disease_model is None:
        if not os.path.exists(Config.DISEASE_MODEL_PATH):
            raise FileNotFoundError(f"Disease model not found at: {Config.DISEASE_MODEL_PATH}")
        _disease_model = tf.keras.models.load_model(Config.DISEASE_MODEL_PATH)
    return _disease_model


def get_shubham_disease_model():
    global _shubham_model
    if _shubham_model is None:
        if not os.path.exists(Config.SHUBHAM_MODEL_PATH):
            raise FileNotFoundError(f"Crop-Disease-Detection model not found at: {Config.SHUBHAM_MODEL_PATH}")
        # compile=False avoids legacy optimizer deserialization issues
        _shubham_model = tf.keras.models.load_model(Config.SHUBHAM_MODEL_PATH, compile=False)
    return _shubham_model


def get_crop_model():
    global _crop_model
    if _crop_model is None:
        if not os.path.exists(Config.CROP_MODEL_PATH):
            raise FileNotFoundError(f"Crop model not found at: {Config.CROP_MODEL_PATH}")
        with open(Config.CROP_MODEL_PATH, "rb") as f:
            _crop_model = pickle.load(f)
    return _crop_model


def get_crop_scaler():
    global _crop_scaler
    if _crop_scaler is None:
        if not os.path.exists(Config.CROP_SCALER_PATH):
            raise FileNotFoundError(f"Crop scaler not found at: {Config.CROP_SCALER_PATH}")
        with open(Config.CROP_SCALER_PATH, "rb") as f:
            _crop_scaler = pickle.load(f)
    return _crop_scaler


# ── Disease Prediction Pipeline ─────────────────────────────────────────────
def validate_image_file(image_path: str):
    """Ensure the file is a readable, uncorrupted image."""
    try:
        with Image.open(image_path) as img:
            img.verify()
        # Re-open after verify to ensure headers can be decoded
        with Image.open(image_path) as img:
            img.load()
    except Exception as e:
        raise ValueError(f"Corrupted or invalid image file: {str(e)}")


def predict_disease(image_path: str, engine: str = None) -> dict:
    """
    Validates, preprocesses and predicts disease from a leaf image.
    Supports multi-engine inference:
      - 'mobilenet': AgriAI MobileNetV2 (29 classes, fast)
      - 'shubham': Crop-Disease-Detection AlexNet/CNN (38 classes, extended)
    Returns:
        dict: {
            disease_name, confidence, status, top_predictions, engine, engine_label
        }
    """
    validate_image_file(image_path)

    if not engine or engine not in Config.AVAILABLE_DISEASE_ENGINES:
        engine = Config.DEFAULT_DISEASE_ENGINE

    image = tf.keras.utils.load_img(image_path, target_size=Config.DISEASE_IMG_SIZE, color_mode="rgb")
    arr = tf.keras.utils.img_to_array(image)

    if engine == "shubham":
        model = get_shubham_disease_model()
        classes = Config.SHUBHAM_DISEASE_CLASSES
        # Shubham model expects 0.0 - 1.0 normalized float32
        arr = np.expand_dims(arr, axis=0).astype("float32") / 255.0
        engine_label = Config.AVAILABLE_DISEASE_ENGINES.get("shubham", "Crop-Disease-Detection CNN (38 Classes)")
    else:
        model = get_disease_model()
        classes = Config.DISEASE_CLASSES
        # MobileNetV2 model has Rescaling(1./255) as layer 0, expecting 0-255 float32
        arr = np.expand_dims(arr, axis=0).astype("float32")
        engine_label = Config.AVAILABLE_DISEASE_ENGINES.get("mobilenet", "AgriAI MobileNetV2 (29 Classes)")

    raw_preds = model.predict(arr, verbose=0)[0]
    top_idx = int(np.argmax(raw_preds))
    confidence = round(float(raw_preds[top_idx] * 100), 2)
    disease_name = classes[top_idx]

    # Calculate top 3 predictions
    top_3_indices = np.argsort(raw_preds)[-3:][::-1]
    top_3 = [
        {
            "disease_name": classes[i],
            "confidence": round(float(raw_preds[i] * 100), 2)
        }
        for i in top_3_indices
    ]

    status = "Healthy" if "Healthy" in disease_name else "Diseased"

    return {
        "disease_name": disease_name,
        "confidence": confidence,
        "status": status,
        "top_predictions": top_3,
        "engine": engine,
        "engine_label": engine_label
    }


# ── Crop Prediction Pipeline ────────────────────────────────────────────────
CROP_FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

# Agronomic optimal reference ranges for explanation
CROP_REFERENCE_RANGES = {
    "apple": {"temp": "15-24°C", "humidity": "60-70%", "ph": "6.0-7.0", "rainfall": "600-800 mm", "soil": "Well-drained loam"},
    "banana": {"temp": "26-30°C", "humidity": "75-95%", "ph": "5.5-7.0", "rainfall": "1000-2500 mm", "soil": "Deep fertile loam"},
    "blackgram": {"temp": "25-35°C", "humidity": "60-80%", "ph": "6.0-7.5", "rainfall": "300-500 mm", "soil": "Light loamy soil"},
    "chickpea": {"temp": "10-25°C", "humidity": "35-50%", "ph": "6.0-7.5", "rainfall": "200-400 mm", "soil": "Well-drained loam"},
    "coconut": {"temp": "24-30°C", "humidity": "70-80%", "ph": "5.0-8.0", "rainfall": "1500-2500 mm", "soil": "Sandy alluvial soil"},
    "coffee": {"temp": "18-24°C", "humidity": "70-80%", "ph": "5.5-6.5", "rainfall": "1500-2000 mm", "soil": "Rich organic loam"},
    "cotton": {"temp": "21-30°C", "humidity": "50-70%", "ph": "5.5-7.5", "rainfall": "600-1200 mm", "soil": "Black cotton soil"},
    "grapes": {"temp": "20-30°C", "humidity": "60-70%", "ph": "5.5-7.0", "rainfall": "600-800 mm", "soil": "Sandy loam"},
    "jute": {"temp": "24-35°C", "humidity": "70-90%", "ph": "5.5-6.8", "rainfall": "1200-1800 mm", "soil": "Alluvial floodplain"},
    "kidneybeans": {"temp": "18-30°C", "humidity": "40-70%", "ph": "6.0-7.0", "rainfall": "300-600 mm", "soil": "Well-drained loam"},
    "lentil": {"temp": "10-25°C", "humidity": "30-60%", "ph": "6.0-8.0", "rainfall": "300-500 mm", "soil": "Sandy loam"},
    "maize": {"temp": "18-32°C", "humidity": "50-80%", "ph": "5.5-7.5", "rainfall": "500-1000 mm", "soil": "Rich fertile loam"},
    "mango": {"temp": "24-30°C", "humidity": "50-60%", "ph": "5.5-7.5", "rainfall": "750-2500 mm", "soil": "Deep alluvial loam"},
    "mothbeans": {"temp": "25-35°C", "humidity": "30-60%", "ph": "6.5-8.0", "rainfall": "200-300 mm", "soil": "Sandy loam"},
    "mungbean": {"temp": "24-30°C", "humidity": "40-70%", "ph": "6.0-7.5", "rainfall": "350-600 mm", "soil": "Well-drained loam"},
    "muskmelon": {"temp": "24-30°C", "humidity": "50-70%", "ph": "6.0-7.5", "rainfall": "400-500 mm", "soil": "Sandy loam"},
    "orange": {"temp": "13-38°C", "humidity": "50-70%", "ph": "5.5-6.5", "rainfall": "1000-1500 mm", "soil": "Well-drained loam"},
    "papaya": {"temp": "22-28°C", "humidity": "60-80%", "ph": "5.5-7.0", "rainfall": "1000-1500 mm", "soil": "Rich fertile soil"},
    "pigeonpeas": {"temp": "25-35°C", "humidity": "65-80%", "ph": "5.5-7.5", "rainfall": "600-900 mm", "soil": "Deep loam"},
    "pomegranate": {"temp": "20-35°C", "humidity": "40-60%", "ph": "5.5-7.5", "rainfall": "300-700 mm", "soil": "Loamy soil"},
    "rice": {"temp": "20-35°C", "humidity": "70-90%", "ph": "5.0-7.0", "rainfall": "1000-2000 mm", "soil": "Clayey alluvial loam"},
    "watermelon": {"temp": "21-30°C", "humidity": "50-60%", "ph": "6.0-7.5", "rainfall": "400-600 mm", "soil": "Sandy loam"}
}


def get_crop_info(crop_name: str, lang: str = "en") -> dict:
    """Retrieve localized crop information."""
    crop_key = crop_name.lower().strip()
    i18n_info = get_crop_translation(crop_key, lang)
    ranges = CROP_REFERENCE_RANGES.get(crop_key, {
        "temp": "N/A", "humidity": "N/A", "ph": "N/A", "rainfall": "N/A", "soil": "N/A"
    })
    return {
        "display_name": i18n_info["name"],
        "season": i18n_info["season"],
        "soil": i18n_info["soil"],
        "care": i18n_info["care"],
        "temperature": ranges["temp"],
        "humidity": ranges["humidity"],
        "ph": ranges["ph"],
        "rainfall": ranges["rainfall"],
    }


def predict_crop(features: dict) -> dict:
    """
    Runs the crop recommendation pipeline with true model probabilities.
    Returns:
        dict: {
            recommended_crop, confidence, top_predictions
        }
    """
    model  = get_crop_model()
    scaler = get_crop_scaler()

    import warnings
    input_arr = np.array([[features[f] for f in CROP_FEATURES]], dtype="float32")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        input_scaled = scaler.transform(input_arr)
        pred_class = str(model.predict(input_scaled)[0])
        probabilities = model.predict_proba(input_scaled)[0]
    confidence = round(float(np.max(probabilities) * 100), 2)

    # Top 3 alternative recommendations with probabilities
    top_indices = np.argsort(probabilities)[-3:][::-1]
    top_predictions = [
        {
            "crop": str(model.classes_[idx]),
            "confidence": round(float(probabilities[idx] * 100), 2)
        }
        for idx in top_indices
    ]

    return {
        "recommended_crop": pred_class,
        "confidence": confidence,
        "top_predictions": top_predictions
    }