"""
utils/model_loader.py
Lazy-loads ML models once and provides prediction functions.
"""
import pickle
import numpy as np
import tensorflow as tf
from config import Config

# ── Singletons ─────────────────────────────────────────────────────────────
_disease_model = None
_crop_model    = None
_crop_scaler   = None


def get_disease_model():
    global _disease_model
    if _disease_model is None:
        _disease_model = tf.keras.models.load_model(Config.DISEASE_MODEL_PATH)
    return _disease_model


def get_crop_model():
    global _crop_model
    if _crop_model is None:
        with open(Config.CROP_MODEL_PATH, "rb") as f:
            _crop_model = pickle.load(f)
    return _crop_model


def get_crop_scaler():
    global _crop_scaler
    if _crop_scaler is None:
        with open(Config.CROP_SCALER_PATH, "rb") as f:
            _crop_scaler = pickle.load(f)
    return _crop_scaler


# ── Disease prediction ──────────────────────────────────────────────────────
def predict_disease(image_path: str) -> dict:
    model = get_disease_model()
    image = tf.keras.utils.load_img(image_path, target_size=Config.DISEASE_IMG_SIZE)
    arr   = tf.keras.utils.img_to_array(image)
    arr   = np.expand_dims(arr, axis=0).astype("float32")

    preds      = model.predict(arr, verbose=0)
    idx        = int(np.argmax(preds))
    confidence = float(np.max(preds) * 100)

    return {
        "disease_name": Config.DISEASE_CLASSES[idx],
        "confidence":   round(confidence, 2),
    }


# ── Crop prediction ─────────────────────────────────────────────────────────
CROP_FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

CROP_DETAILS = {
    "apple": {
        "display_name": "Apple",
        "season": "Spring planting and autumn harvest in temperate regions.",
        "temperature": "15-24°C",
        "humidity": "60-70%",
        "ph": "6.0-7.0",
        "rainfall": "600-800 mm",
        "soil": "Well-drained loamy soil",
        "care": "Prune regularly, provide balanced fertilization, and monitor for pests and fungal diseases.",
    },
    "banana": {
        "display_name": "Banana",
        "season": "Warm, humid climate year-round with best yields in spring/summer.",
        "temperature": "26-30°C",
        "humidity": "75-95%",
        "ph": "5.5-7.0",
        "rainfall": "1000-2500 mm",
        "soil": "Deep, fertile soil with good moisture retention.",
        "care": "Keep soil moist, mulch heavily, and manage nutrients with potassium-rich fertilizer.",
    },
    "blackgram": {
        "display_name": "Blackgram",
        "season": "Kharif season with sowing at the start of monsoon.",
        "temperature": "25-35°C",
        "humidity": "60-80%",
        "ph": "6.0-7.5",
        "rainfall": "300-500 mm",
        "soil": "Light loamy soil with good drainage.",
        "care": "Use short-duration varieties, maintain moisture during flowering, and practice crop rotation.",
    },
    "chickpea": {
        "display_name": "Chickpea",
        "season": "Winter crop grown in cool, dry weather.",
        "temperature": "10-25°C",
        "humidity": "35-50%",
        "ph": "6.0-7.5",
        "rainfall": "200-400 mm",
        "soil": "Well-drained loam or sandy loam.",
        "care": "Avoid waterlogging, use phosphorous-rich fertilizer, and control weeds early.",
    },
    "coconut": {
        "display_name": "Coconut",
        "season": "Can be grown year-round in tropical climates.",
        "temperature": "24-30°C",
        "humidity": "70-80%",
        "ph": "5.0-8.0",
        "rainfall": "1500-2500 mm",
        "soil": "Sandy, well-drained soil low in salts.",
        "care": "Ensure regular irrigation, mulch around the base, and provide micronutrients.",
    },
    "coffee": {
        "display_name": "Coffee",
        "season": "Plant in the rainy season; shade and cool conditions are best.",
        "temperature": "18-24°C",
        "humidity": "70-80%",
        "ph": "5.5-6.5",
        "rainfall": "1500-2000 mm",
        "soil": "Rich, well-drained loam with organic matter.",
        "care": "Maintain shade, apply organic mulch, and protect from strong sunlight.",
    },
    "cotton": {
        "display_name": "Cotton",
        "season": "Kharif season with sowing after the first rains.",
        "temperature": "21-30°C",
        "humidity": "50-70%",
        "ph": "5.5-7.5",
        "rainfall": "600-1200 mm",
        "soil": "Deep, well-drained loamy soil.",
        "care": "Use proper spacing, control pests early, and give nitrogen and potassium at key stages.",
    },
    "grapes": {
        "display_name": "Grapes",
        "season": "Spring planting with harvest in late summer/autumn.",
        "temperature": "20-30°C",
        "humidity": "60-70%",
        "ph": "5.5-7.0",
        "rainfall": "600-800 mm",
        "soil": "Well-drained sandy loam.",
        "care": "Train vines, prune for good air flow, and avoid waterlogging.",
    },
    "jute": {
        "display_name": "Jute",
        "season": "Monsoon season with warm, wet weather.",
        "temperature": "24-35°C",
        "humidity": "70-90%",
        "ph": "5.5-6.8",
        "rainfall": "1200-1800 mm",
        "soil": "Alluvial soil with good moisture retention.",
        "care": "Keep soil moist, provide adequate nitrogen, and protect seedlings from drought.",
    },
    "kidneybeans": {
        "display_name": "Kidney Beans",
        "season": "Warm season crop planted after the last frost.",
        "temperature": "18-30°C",
        "humidity": "40-70%",
        "ph": "6.0-7.0",
        "rainfall": "300-600 mm",
        "soil": "Well-drained loam.",
        "care": "Avoid waterlogging, support vines if needed, and apply phosphorus at planting.",
    },
    "lentil": {
        "display_name": "Lentil",
        "season": "Cool season crop planted in early spring or late winter.",
        "temperature": "10-25°C",
        "humidity": "30-60%",
        "ph": "6.0-8.0",
        "rainfall": "300-500 mm",
        "soil": "Sandy loam with good drainage.",
        "care": "Maintain moisture during germination and avoid heavy fertilizers.",
    },
    "maize": {
        "display_name": "Maize",
        "season": "Warm season crop with planting in spring or early summer.",
        "temperature": "18-32°C",
        "humidity": "50-80%",
        "ph": "5.5-7.5",
        "rainfall": "500-1000 mm",
        "soil": "Loamy, well-drained soil.",
        "care": "Use balanced fertilization, weed control, and irrigate during tasseling and grain fill.",
    },
    "mango": {
        "display_name": "Mango",
        "season": "Tropical/subtropical crop planted in spring with flowering in late winter.",
        "temperature": "24-30°C",
        "humidity": "50-60%",
        "ph": "5.5-7.5",
        "rainfall": "750-2500 mm",
        "soil": "Deep, well-drained fertile soil.",
        "care": "Water young trees regularly, provide mulch, and prune for structure.",
    },
    "mothbeans": {
        "display_name": "Mothbeans",
        "season": "Summer crop suited for arid and semi-arid regions.",
        "temperature": "25-35°C",
        "humidity": "30-60%",
        "ph": "6.0-7.5",
        "rainfall": "200-300 mm",
        "soil": "Sandy loam with good drainage.",
        "care": "Use drought-tolerant practices, minimal irrigation, and timely weeding.",
    },
    "mungbean": {
        "display_name": "Mung Bean",
        "season": "Warm season crop, usually planted in spring/summer.",
        "temperature": "24-30°C",
        "humidity": "40-70%",
        "ph": "6.0-7.5",
        "rainfall": "350-600 mm",
        "soil": "Well-drained sandy loam.",
        "care": "Keep soil moist early, avoid waterlogging, and apply rhizobium inoculant if available.",
    },
    "muskmelon": {
        "display_name": "Muskmelon",
        "season": "Warm season crop with planting after last frost.",
        "temperature": "24-30°C",
        "humidity": "50-70%",
        "ph": "6.0-7.5",
        "rainfall": "400-500 mm",
        "soil": "Sandy loam rich in organic matter.",
        "care": "Provide consistent moisture until fruit set, then reduce watering to improve sweetness.",
    },
    "orange": {
        "display_name": "Orange",
        "season": "Subtropical climate; best planted in spring or early summer.",
        "temperature": "13-38°C",
        "humidity": "50-70%",
        "ph": "5.5-6.5",
        "rainfall": "1000-1500 mm",
        "soil": "Well-drained sandy loam.",
        "care": "Irrigate deeply, fertilize regularly, and protect from frost.",
    },
    "papaya": {
        "display_name": "Papaya",
        "season": "Warm tropical crop grown year-round in frost-free areas.",
        "temperature": "22-28°C",
        "humidity": "60-80%",
        "ph": "5.5-7.0",
        "rainfall": "1000-1500 mm",
        "soil": "Well-drained, fertile soil.",
        "care": "Water regularly, apply organic mulch, and remove diseased leaves promptly.",
    },
    "pigeonpeas": {
        "display_name": "Pigeon Peas",
        "season": "Kharif crop with sowing during the onset of monsoon.",
        "temperature": "25-35°C",
        "humidity": "65-80%",
        "ph": "5.5-7.5",
        "rainfall": "600-900 mm",
        "soil": "Light loam with good drainage.",
        "care": "Use rhizobium inoculant, avoid heavy nitrogen, and manage weeds early.",
    },
    "pomegranate": {
        "display_name": "Pomegranate",
        "season": "Warm season crop tolerant of dry conditions.",
        "temperature": "20-35°C",
        "humidity": "40-60%",
        "ph": "5.5-7.5",
        "rainfall": "300-700 mm",
        "soil": "Well-drained loamy soil.",
        "care": "Provide regular irrigation during fruit set, prune for airflow, and avoid waterlogging.",
    },
    "rice": {
        "display_name": "Rice",
        "season": "Kharif crop grown during the rainy season.",
        "temperature": "20-35°C",
        "humidity": "70-90%",
        "ph": "5.0-7.0",
        "rainfall": "1000-2000 mm",
        "soil": "Clayey loam with good water retention.",
        "care": "Maintain flooded fields early, manage pests, and use balanced nitrogen applications.",
    },
    "watermelon": {
        "display_name": "Watermelon",
        "season": "Warm season crop planted after frost risk passes.",
        "temperature": "21-30°C",
        "humidity": "50-60%",
        "ph": "6.0-7.5",
        "rainfall": "400-600 mm",
        "soil": "Sandy loam with good drainage.",
        "care": "Keep soil moist but not waterlogged, and thin vines for proper fruit development.",
    },
}


def get_crop_info(crop_name: str) -> dict:
    if not crop_name:
        return {
            "display_name": "Unknown Crop",
            "season": "Season data not available.",
            "temperature": "N/A",
            "humidity": "N/A",
            "ph": "N/A",
            "rainfall": "N/A",
            "soil": "N/A",
            "care": "Provide general crop care with balanced nutrients, water management, and pest monitoring.",
        }
    return CROP_DETAILS.get(crop_name.lower(), {
        "display_name": crop_name.title(),
        "season": "Season data not available.",
        "temperature": "N/A",
        "humidity": "N/A",
        "ph": "N/A",
        "rainfall": "N/A",
        "soil": "N/A",
        "care": "Provide general crop care with balanced nutrients, water management, and pest monitoring.",
    })


def predict_crop(features: dict) -> str:
    """
    features: dict with keys N, P, K, temperature, humidity, ph, rainfall
    Returns: recommended crop name as string
    """
    model  = get_crop_model()
    scaler = get_crop_scaler()

    input_arr    = np.array([[features[f] for f in CROP_FEATURES]], dtype="float32")
    input_scaled = scaler.transform(input_arr)   # scale before predicting
    prediction   = model.predict(input_scaled)

    return str(prediction[0])