import os
import pickle
import numpy as np
import tensorflow as tf
from pymongo import MongoClient
from config import Config
from utils.model_loader import get_crop_model, get_crop_scaler, predict_crop, CROP_DETAILS

print("==========================================")
print("1. QUERYING MONGODB DATABASE")
print("==========================================")
client = MongoClient("mongodb://localhost:27017/")
db = client["AgriAI_DB"]
print("Collections:", db.list_collection_names())
print("User count:", db.users.count_documents({}))
for u in db.users.find({}, {"password": 0}):
    print("  User:", u)

print("\nCrop predictions count:", db.crop_predictions.count_documents({}))
for cp in db.crop_predictions.find().limit(5):
    print("  Crop pred:", cp.get("recommended_crop"), "Inputs:", cp.get("inputs"))

print("\nDisease predictions count:", db.disease_predictions.count_documents({}))
for dp in db.disease_predictions.find().limit(10):
    print("  Disease pred:", dp.get("disease_name"), "Confidence:", dp.get("confidence"), "Img:", dp.get("image_filename"))

print("\nDisease solutions count:", db.disease_solutions.count_documents({}))
sol_names = [s["disease_name"] for s in db.disease_solutions.find()]
print(f"  Disease solutions ({len(sol_names)}):")
for s in sorted(sol_names):
    print(f"    - {s}")

print("\n==========================================")
print("2. TESTING DISEASE MODEL ON UPLOADED IMAGES")
print("==========================================")
d_model = tf.keras.models.load_model(Config.DISEASE_MODEL_PATH)
upload_dir = Config.UPLOAD_FOLDER

upload_files = [f for f in os.listdir(upload_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
print(f"Testing {len(upload_files)} images from {upload_dir}...")

predictions_summary = {}
for img_name in upload_files:
    img_path = os.path.join(upload_dir, img_name)
    img = tf.keras.utils.load_img(img_path, target_size=Config.DISEASE_IMG_SIZE)
    arr = tf.keras.utils.img_to_array(img)
    arr = np.expand_dims(arr, axis=0).astype("float32")
    
    preds = d_model.predict(arr, verbose=0)
    top_idx = int(np.argmax(preds))
    confidence = float(np.max(preds) * 100)
    disease_name = Config.DISEASE_CLASSES[top_idx]
    
    # Get top 3 predictions
    top_3_indices = np.argsort(preds[0])[-3:][::-1]
    top_3 = [(Config.DISEASE_CLASSES[i], round(float(preds[0][i] * 100), 2)) for i in top_3_indices]
    
    predictions_summary[img_name] = (disease_name, round(confidence, 2), top_3)
    print(f"  Image: {img_name}")
    print(f"    Top-1: {disease_name} ({confidence:.2f}%)")
    print(f"    Top-3: {top_3}")

print("\nUnique diseases predicted across test images:")
unique_preds = set(v[0] for v in predictions_summary.values())
for up in sorted(unique_preds):
    count = sum(1 for v in predictions_summary.values() if v[0] == up)
    print(f"  {up}: {count} image(s)")

print("\n==========================================")
print("3. TESTING CROP RECOMMENDATION MODEL")
print("==========================================")
crop_model = get_crop_model()
crop_scaler = get_crop_scaler()

print(f"Model classes ({len(crop_model.classes_)}): {list(crop_model.classes_)}")

# Test inputs for each crop class based on standard agricultural ranges in India/global datasets
# Features: ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
test_cases = {
    "rice":        {"N": 80, "P": 40, "K": 40, "temperature": 25.0, "humidity": 82.0, "ph": 6.5, "rainfall": 200.0},
    "maize":       {"N": 80, "P": 45, "K": 20, "temperature": 23.0, "humidity": 65.0, "ph": 6.5, "rainfall": 70.0},
    "chickpea":    {"N": 40, "P": 60, "K": 80, "temperature": 18.0, "humidity": 16.0, "ph": 7.0, "rainfall": 80.0},
    "kidneybeans": {"N": 20, "P": 60, "K": 20, "temperature": 20.0, "humidity": 21.0, "ph": 5.7, "rainfall": 105.0},
    "pigeonpeas":  {"N": 20, "P": 65, "K": 20, "temperature": 28.0, "humidity": 45.0, "ph": 5.7, "rainfall": 150.0},
    "mothbeans":   {"N": 20, "P": 45, "K": 20, "temperature": 28.0, "humidity": 55.0, "ph": 7.2, "rainfall": 50.0},
    "mungbean":    {"N": 20, "P": 45, "K": 20, "temperature": 28.0, "humidity": 85.0, "ph": 6.7, "rainfall": 50.0},
    "blackgram":   {"N": 40, "P": 65, "K": 20, "temperature": 30.0, "humidity": 65.0, "ph": 7.2, "rainfall": 65.0},
    "lentil":      {"N": 20, "P": 65, "K": 20, "temperature": 24.0, "humidity": 65.0, "ph": 6.9, "rainfall": 45.0},
    "pomegranate": {"N": 20, "P": 20, "K": 40, "temperature": 22.0, "humidity": 90.0, "ph": 6.8, "rainfall": 110.0},
    "banana":      {"N": 100, "P": 75, "K": 50, "temperature": 27.0, "humidity": 80.0, "ph": 6.0, "rainfall": 100.0},
    "mango":       {"N": 20, "P": 25, "K": 30, "temperature": 31.0, "humidity": 50.0, "ph": 5.5, "rainfall": 95.0},
    "grapes":      {"N": 20, "P": 130, "K": 200, "temperature": 24.0, "humidity": 81.0, "ph": 6.0, "rainfall": 70.0},
    "watermelon":  {"N": 100, "P": 18, "K": 50, "temperature": 26.0, "humidity": 85.0, "ph": 6.5, "rainfall": 50.0},
    "muskmelon":   {"N": 100, "P": 18, "K": 50, "temperature": 28.0, "humidity": 92.0, "ph": 6.4, "rainfall": 25.0},
    "apple":       {"N": 20, "P": 135, "K": 200, "temperature": 22.0, "humidity": 92.0, "ph": 5.9, "rainfall": 110.0},
    "orange":      {"N": 20, "P": 15, "K": 10, "temperature": 23.0, "humidity": 92.0, "ph": 7.0, "rainfall": 110.0},
    "papaya":      {"N": 50, "P": 60, "K": 50, "temperature": 34.0, "humidity": 92.0, "ph": 6.7, "rainfall": 150.0},
    "coconut":     {"N": 20, "P": 15, "K": 30, "temperature": 27.0, "humidity": 96.0, "ph": 6.0, "rainfall": 175.0},
    "cotton":      {"N": 120, "P": 45, "K": 20, "temperature": 24.0, "humidity": 80.0, "ph": 6.8, "rainfall": 80.0},
    "jute":        {"N": 80, "P": 45, "K": 40, "temperature": 25.0, "humidity": 80.0, "ph": 6.7, "rainfall": 175.0},
    "coffee":      {"N": 100, "P": 30, "K": 30, "temperature": 26.0, "humidity": 58.0, "ph": 6.8, "rainfall": 160.0},
}

correct = 0
total = len(test_cases)
print(f"Testing {total} representative crop test cases (1 per class)...")
for expected_crop, inputs in test_cases.items():
    feats = [inputs[f] for f in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    scaled = crop_scaler.transform([feats])
    pred = crop_model.predict(scaled)[0]
    proba = crop_model.predict_proba(scaled)[0]
    top_prob = np.max(proba) * 100
    
    match = (pred.lower() == expected_crop.lower())
    if match:
        correct += 1
        status = "[PASS]"
    else:
        status = "[FAIL]"
    print(f"  {status} Expected: {expected_crop:12s} | Predicted: {pred:12s} | Prob: {top_prob:5.1f}%")

print(f"\nCrop Test Accuracy on representative cases: {correct}/{total} ({correct/total*100:.1f}%)")
