import os
import uuid
from typing import Dict, Any
import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, render_template, request, send_from_directory
from PIL import Image
from werkzeug.utils import secure_filename

from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.disease_routes import disease_bp
from routes.crop_routes import crop_bp
from db import disease_solutions_collection, init_indexes

app = Flask(__name__)
app.config["SECRET_KEY"] = "agri_ai_secret_key_2026"

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(disease_bp)
app.register_blueprint(crop_bp)


# ── Initialize database ────────────────────────────────────────────────────────
def init_disease_solutions():
    """Seed disease solutions if collection is empty."""
    if disease_solutions_collection.count_documents({}) == 0:
        solutions = [
            {"disease_name": "Apple - Apple Scab",
             "cause": "Fungal disease caused by Venturia inaequalis, favored by cool, wet spring weather.",
             "solution": "Apply fungicide sprays from bud break, rake and destroy fallen leaves, prune for airflow, and choose scab-resistant varieties."},
            {"disease_name": "Apple - Black Rot",
             "cause": "Caused by the fungus Botryosphaeria obtusa, which enters through wounds and dead wood.",
             "solution": "Prune out cankers and dead wood, remove mummified fruit, and apply fungicide during the growing season."},
            {"disease_name": "Apple - Cedar Apple Rust",
             "cause": "Fungal disease that alternates between apple and nearby juniper/cedar trees.",
             "solution": "Remove nearby junipers/cedars if possible, apply preventive fungicide in spring, and plant rust-resistant varieties."},
            {"disease_name": "Apple - Healthy",
             "cause": "No disease detected.",
             "solution": "Plant appears healthy. Continue regular watering, fertilization, and monitoring."},
            {"disease_name": "Bell Pepper - Bacterial Spot",
             "cause": "Caused by Xanthomonas bacteria, spread by water splash, rain, and contaminated tools or seed.",
             "solution": "Use disease-free seed, avoid overhead irrigation, apply copper-based bactericides, and rotate crops for 2-3 years."},
            {"disease_name": "Bell Pepper - Healthy",
             "cause": "No disease detected.",
             "solution": "Plant appears healthy. Maintain consistent watering and balanced fertilization."},
            {"disease_name": "Cherry - Healthy",
             "cause": "No disease detected.",
             "solution": "Plant appears healthy. Continue routine pruning and pest monitoring."},
            {"disease_name": "Cherry - Powdery Mildew",
             "cause": "Fungal disease favored by warm days, cool nights, and high humidity.",
             "solution": "Improve air circulation through pruning, apply sulfur or approved fungicides, and avoid excess nitrogen fertilizer."},
            {"disease_name": "Corn (Maize) - Cercospora Leaf Spot",
             "cause": "Fungal disease (gray leaf spot) that thrives in warm, humid conditions with extended leaf wetness.",
             "solution": "Rotate crops, plant resistant hybrids, manage crop residue, and apply foliar fungicide if disease pressure is high."},
            {"disease_name": "Corn (Maize) - Common Rust",
             "cause": "Fungal disease caused by Puccinia sorghi, spread by windborne spores.",
             "solution": "Plant resistant hybrids, monitor fields regularly, and apply fungicide if infection is early and severe."},
            {"disease_name": "Corn (Maize) - Healthy",
             "cause": "No disease detected.",
             "solution": "Plant appears healthy. Maintain proper fertilization and irrigation."},
            {"disease_name": "Corn (Maize) - Northern Leaf Blight",
             "cause": "Fungal disease favored by moderate temperatures and high humidity.",
             "solution": "Use resistant hybrids, rotate crops, till under crop residue, and apply fungicide if needed."},
            {"disease_name": "Grape - Black Rot",
             "cause": "Fungal disease that spreads rapidly in warm, wet weather.",
             "solution": "Remove mummified berries and infected canes, apply fungicide from early shoot growth through fruit set, and improve canopy airflow."},
            {"disease_name": "Grape - Esca (Black Measles)",
             "cause": "Caused by a complex of wood-rotting fungi entering through pruning wounds.",
             "solution": "Avoid pruning in wet weather, protect pruning cuts, and remove severely infected vines. No curative chemical treatment exists."},
            {"disease_name": "Grape - Healthy",
             "cause": "No disease detected.",
             "solution": "Plant appears healthy. Continue regular canopy management and monitoring."},
            {"disease_name": "Grape - Leaf Blight",
             "cause": "Fungal leaf spot disease favored by warm, humid conditions.",
             "solution": "Improve canopy ventilation, remove infected leaves, and apply fungicide preventively."},
            {"disease_name": "Peach - Bacterial Spot",
             "cause": "Caused by Xanthomonas bacteria, spread by rain splash and wind.",
             "solution": "Use resistant varieties, apply copper-based sprays during dormancy, avoid overhead irrigation, and prune for airflow."},
            {"disease_name": "Peach - Healthy",
             "cause": "No disease detected.",
             "solution": "Plant appears healthy. Continue regular care, watering, and pest monitoring."},
            {"disease_name": "Potato - Early Blight",
             "cause": "Fungal disease caused by Alternaria solani, favored by warm temperatures and high humidity.",
             "solution": "Rotate crops, remove infected debris, apply fungicide, avoid overhead watering, and maintain plant nutrition."},
            {"disease_name": "Potato - Healthy",
             "cause": "No disease detected.",
             "solution": "Plant appears healthy. Continue regular irrigation and monitoring."},
            {"disease_name": "Potato - Late Blight",
             "cause": "Caused by Phytophthora infestans, which spreads rapidly in cool, wet conditions.",
             "solution": "Plant resistant varieties, apply fungicide preventively, destroy infected plants promptly, and avoid overhead irrigation."},
            {"disease_name": "Strawberry - Healthy",
             "cause": "No disease detected.",
             "solution": "Plant appears healthy. Continue regular watering and bed renovation practices."},
            {"disease_name": "Strawberry - Leaf Scorch",
             "cause": "Fungal disease that spreads in warm, wet conditions.",
             "solution": "Remove infected leaves after harvest, improve air circulation, apply fungicide if needed, and avoid overhead irrigation."},
            {"disease_name": "Tomato - Bacterial Spot",
             "cause": "Caused by Xanthomonas species, spread through contaminated seed, water splash, and tools.",
             "solution": "Use certified disease-free seed/transplants, apply copper-based bactericides, avoid handling wet plants, and rotate crops."},
            {"disease_name": "Tomato - Early Blight",
             "cause": "Fungal disease caused by Alternaria solani, common in warm humid weather, often starting on lower leaves.",
             "solution": "Remove infected leaves, mulch to reduce soil splash, apply fungicide, rotate crops, and stake plants for airflow."},
            {"disease_name": "Tomato - Healthy",
             "cause": "No disease detected.",
             "solution": "Plant appears healthy. Continue balanced watering and fertilization."},
            {"disease_name": "Tomato - Late Blight",
             "cause": "Caused by Phytophthora infestans, which spreads quickly in cool, moist conditions and can destroy a crop within days.",
             "solution": "Apply fungicide preventively, remove and destroy infected plants immediately, avoid overhead watering, and ensure good ventilation."},
            {"disease_name": "Tomato - Septoria Leaf Spot",
             "cause": "Fungal disease that spreads via splashing water and favors humid conditions.",
             "solution": "Remove lower infected leaves, mulch around plants, apply fungicide, avoid overhead irrigation, and rotate crops."},
            {"disease_name": "Tomato - Yellow Leaf Curl Virus",
             "cause": "Viral disease transmitted by whiteflies, causing leaf curling, yellowing, and stunted growth.",
             "solution": "Control whiteflies with insecticides or sticky traps, use resistant varieties, remove infected plants, and use reflective mulches."},
        ]
        for item in solutions:
            disease_solutions_collection.update_one(
                {"disease_name": item["disease_name"]},
                {"$set": item},
                upsert=True
            )
        print(f"✓ Initialized {len(solutions)} disease solutions")


# Initialize on startup
try:
    init_indexes()
    init_disease_solutions()
    print("✓ Database initialized successfully")
except Exception as e:
    print(f"⚠ Database init warning: {e}")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "disease_model.h5")   # ← fixed path
DATASET_DIR = os.path.join(BASE_DIR, "dataset", "Train")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
IMG_SIZE = (224, 224)

os.makedirs(UPLOAD_DIR, exist_ok=True)

# Load disease model once at startup
model = tf.keras.models.load_model(MODEL_PATH)


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_class_names() -> list[str]:
    return sorted(
        [name for name in os.listdir(DATASET_DIR) if os.path.isdir(os.path.join(DATASET_DIR, name))]
    )


def preprocess_image(image_path: str) -> np.ndarray:
    try:
        image = tf.keras.utils.load_img(
            image_path,
            target_size=IMG_SIZE,
            color_mode="rgb",
        )
        image_array = tf.keras.utils.img_to_array(image)
        image_array = np.expand_dims(image_array, axis=0)
        return image_array.astype("float32")
    except Exception as exc:
        raise ValueError(f"Unable to read image file: {exc}") from exc


def determine_status(disease_name: str) -> str:
    return "Healthy" if "Healthy" in disease_name else "Diseased"


def get_recommendation(disease_name: str) -> Dict[str, Any]:
    disease_key = disease_name.strip().lower()

    remedies = {
        "apple - apple scab": {
            "remedy": "Remove infected leaves promptly and apply a copper-based fungicide or sulfur spray.",
            "prevention": "Avoid overhead watering and improve air circulation around the trees."
        },
        "apple - black rot": {
            "remedy": "Prune and destroy affected fruit and branches, then apply a fungicide labeled for black rot.",
            "prevention": "Keep fruit dry, thin the canopy, and remove fallen fruit from the ground."
        },
        "apple - cedar apple rust": {
            "remedy": "Use fungicides and remove nearby juniper hosts to reduce reinfection.",
            "prevention": "Space trees well and avoid wet foliage during cool periods."
        },
        "bell pepper - bacterial spot": {
            "remedy": "Remove heavily infected leaves and apply copper bactericide treatments.",
            "prevention": "Water at the base of plants and avoid touching wet foliage."
        },
        "cherry - powdery mildew": {
            "remedy": "Apply sulfur or potassium bicarbonate fungicide and improve plant airflow.",
            "prevention": "Avoid dense planting and keep leaves dry."
        },
        "corn (maize) - cercospora leaf spot": {
            "remedy": "Use fungicides and rotate crops to reduce disease pressure.",
            "prevention": "Plant resistant hybrids and manage crop residues."
        },
        "corn (maize) - common rust": {
            "remedy": "Apply rust-targeted fungicide if disease pressure is high.",
            "prevention": "Use resistant varieties and monitor fields regularly."
        },
        "corn (maize) - northern leaf blight": {
            "remedy": "Treat with fungicide and remove infected residue after harvest.",
            "prevention": "Use resistant varieties and avoid excessive nitrogen."
        },
        "grape - black rot": {
            "remedy": "Prune infected clusters and spray a copper or mancozeb fungicide.",
            "prevention": "Remove fallen leaves and improve canopy ventilation."
        },
        "grape - esca (black measles)": {
            "remedy": "Remove affected vines and avoid using infected wood for propagation.",
            "prevention": "Prune carefully and keep vineyard sanitation high."
        },
        "grape - leaf blight": {
            "remedy": "Apply fungicide and remove severely infected foliage.",
            "prevention": "Avoid overhead irrigation and keep vines well spaced."
        },
        "peach - bacterial spot": {
            "remedy": "Use copper sprays and remove infected shoots early.",
            "prevention": "Reduce overhead irrigation and sanitize pruning tools."
        },
        "potato - early blight": {
            "remedy": "Use chlorothalonil or copper fungicides and remove infected leaves.",
            "prevention": "Mulch soil, avoid wet foliage, and rotate crops."
        },
        "potato - late blight": {
            "remedy": "Apply copper-based fungicide immediately and remove infected plant material.",
            "prevention": "Use resistant varieties and monitor weather conditions for blight risk."
        },
        "strawberry - leaf scorch": {
            "remedy": "Remove infected leaves and use fungicides appropriate for leaf scorch.",
            "prevention": "Improve airflow and minimize leaf wetness."
        },
        "tomato - bacterial spot": {
            "remedy": "Treat with copper bactericide and remove badly infected leaves.",
            "prevention": "Avoid splashing water and rotate tomato crops yearly."
        },
        "tomato - early blight": {
            "remedy": "Use fungicide and remove lower infected leaves promptly.",
            "prevention": "Mulch the soil and keep foliage dry."
        },
        "tomato - late blight": {
            "remedy": "Apply copper-based fungicide and remove infected foliage immediately.",
            "prevention": "Provide good spacing and avoid wet leaves overnight."
        },
        "tomato - septoria leaf spot": {
            "remedy": "Use fungicide and prune lower leaves to improve airflow.",
            "prevention": "Water at the base and remove fallen leaves."
        },
        "tomato - yellow leaf curl virus": {
            "remedy": "Remove infected plants and manage whiteflies to stop spread.",
            "prevention": "Use insect-proof netting and plant resistant varieties."
        },
        "tomato - healthy": {
            "remedy": "Keep the plant healthy with regular watering, balanced fertilization, and pest monitoring.",
            "prevention": "Inspect leaves weekly and maintain good airflow around the plant."
        },
    }

    for key, data in remedies.items():
        if key in disease_key:
            return data

    return {
        "remedy": "Inspect the plant closely and apply crop-specific treatment if symptoms persist.",
        "prevention": "Maintain clean tools, remove debris, and monitor the leaves regularly."
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded."}), 400

    file = request.files["image"]
    if file.filename == "" or not allowed_file(file.filename):
        return jsonify({"error": "Please upload a valid image file (JPG, JPEG, PNG, WEBP)."}), 400

    filename = secure_filename(file.filename)
    unique_name = f"{uuid.uuid4().hex}_{filename}"
    save_path = os.path.join(UPLOAD_DIR, unique_name)

    try:
        file.save(save_path)
        image_array = preprocess_image(save_path)
        prediction = model.predict(image_array, verbose=0)
        class_names = get_class_names()
        pred_index = int(np.argmax(prediction))
        confidence = float(np.max(prediction) * 100)
        disease_name = class_names[pred_index]
        recommendation = get_recommendation(disease_name)

        result = {
            "disease":            disease_name,
            "confidence":         round(confidence, 2),
            "status":             determine_status(disease_name),
            "recommended_action": recommendation["remedy"],
            "prevention":         recommendation["prevention"],
            "image_url":          f"/uploads/{unique_name}",
        }
        return jsonify(result)

    except Exception as exc:
        return jsonify({"error": f"Prediction failed: {str(exc)}"}), 500


@app.route("/uploads/<filename>")
def uploaded_file(filename: str):
    return send_from_directory(UPLOAD_DIR, filename)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(413)
def too_large(e):
    return jsonify({"error": "File too large. Maximum size is 5MB."}), 413


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)