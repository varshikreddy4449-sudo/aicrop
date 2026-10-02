"""
config.py
Centralized configuration for the Flask application.
"""
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "agri_ai_secure_session_key_2026")

    # MongoDB connection
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
    DB_NAME   = os.environ.get("DB_NAME", "AgriAI_DB")

    # Upload settings
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB

    # Model paths
    DISEASE_MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "disease_model.h5")
    SHUBHAM_MODEL_PATH = os.path.join(os.path.dirname(__file__), "Crop-Disease-Detection", "Model.hdf5")
    CROP_MODEL_PATH    = os.path.join(os.path.dirname(__file__), "models", "model.pkl")
    CROP_SCALER_PATH   = os.path.join(os.path.dirname(__file__), "models", "minmaxscaler.pkl")

    # Multi-language configuration
    SUPPORTED_LANGUAGES = ["en", "hi", "te"]
    DEFAULT_LANGUAGE    = "en"

    # Disease model engines
    DEFAULT_DISEASE_ENGINE = "mobilenet"
    AVAILABLE_DISEASE_ENGINES = {
        "mobilenet": "AgriAI MobileNetV2 (29 Classes, Fast)",
        "shubham": "Crop-Disease-Detection CNN (38 Classes, Extended)"
    }

    # Disease class labels for default AgriAI MobileNetV2 model (29 classes)
    DISEASE_CLASSES = [
        "Apple - Apple Scab",
        "Apple - Black Rot",
        "Apple - Cedar Apple Rust",
        "Apple - Healthy",
        "Bell Pepper - Bacterial Spot",
        "Bell Pepper - Healthy",
        "Cherry - Healthy",
        "Cherry - Powdery Mildew",
        "Corn (Maize) - Cercospora Leaf Spot",
        "Corn (Maize) - Common Rust",
        "Corn (Maize) - Healthy",
        "Corn (Maize) - Northern Leaf Blight",
        "Grape - Black Rot",
        "Grape - Esca (Black Measles)",
        "Grape - Healthy",
        "Grape - Leaf Blight",
        "Peach - Bacterial Spot",
        "Peach - Healthy",
        "Potato - Early Blight",
        "Potato - Healthy",
        "Potato - Late Blight",
        "Strawberry - Healthy",
        "Strawberry - Leaf Scorch",
        "Tomato - Bacterial Spot",
        "Tomato - Early Blight",
        "Tomato - Healthy",
        "Tomato - Late Blight",
        "Tomato - Septoria Leaf Spot",
        "Tomato - Yellow Leaf Curl Virus",
    ]

    # Raw class labels from Shubham-Jain-09/Crop-Disease-Detection Model.hdf5 (38 classes)
    SHUBHAM_RAW_CLASSES = [
        'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
        'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
        'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
        'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
        'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
        'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
        'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
        'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
        'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
        'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
        'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
        'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
        'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
    ]

    # Normalized human-readable names for Shubham 38 classes
    SHUBHAM_DISEASE_CLASSES = [
        "Apple - Apple Scab",
        "Apple - Black Rot",
        "Apple - Cedar Apple Rust",
        "Apple - Healthy",
        "Blueberry - Healthy",
        "Cherry - Powdery Mildew",
        "Cherry - Healthy",
        "Corn (Maize) - Cercospora Leaf Spot",
        "Corn (Maize) - Common Rust",
        "Corn (Maize) - Northern Leaf Blight",
        "Corn (Maize) - Healthy",
        "Grape - Black Rot",
        "Grape - Esca (Black Measles)",
        "Grape - Leaf Blight",
        "Grape - Healthy",
        "Orange - Huanglongbing (Citrus Greening)",
        "Peach - Bacterial Spot",
        "Peach - Healthy",
        "Bell Pepper - Bacterial Spot",
        "Bell Pepper - Healthy",
        "Potato - Early Blight",
        "Potato - Late Blight",
        "Potato - Healthy",
        "Raspberry - Healthy",
        "Soybean - Healthy",
        "Squash - Powdery Mildew",
        "Strawberry - Leaf Scorch",
        "Strawberry - Healthy",
        "Tomato - Bacterial Spot",
        "Tomato - Early Blight",
        "Tomato - Late Blight",
        "Tomato - Leaf Mold",
        "Tomato - Septoria Leaf Spot",
        "Tomato - Spider Mites (Two-spotted spider mite)",
        "Tomato - Target Spot",
        "Tomato - Yellow Leaf Curl Virus",
        "Tomato - Tomato Mosaic Virus",
        "Tomato - Healthy"
    ]

    DISEASE_IMG_SIZE = (224, 224)
    SESSION_PERMANENT = False