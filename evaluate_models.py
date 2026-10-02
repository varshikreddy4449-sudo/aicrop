import os
import pickle
import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
from config import Config

print("==================================================")
print("COMPREHENSIVE CROP MODEL EVALUATION")
print("==================================================")

with open(Config.CROP_MODEL_PATH, "rb") as f:
    crop_model = pickle.load(f)
with open(Config.CROP_SCALER_PATH, "rb") as f:
    crop_scaler = pickle.load(f)

print(f"Model Type: {type(crop_model).__name__}")
print(f"Number of estimators: {crop_model.n_estimators}")
print(f"Number of classes: {len(crop_model.classes_)}")
print(f"Classes: {list(crop_model.classes_)}")
print(f"Feature Names: {crop_scaler.feature_names_in_}")
print(f"Data Min: {crop_scaler.data_min_}")
print(f"Data Max: {crop_scaler.data_max_}")

# Standard agronomic benchmark samples for all 22 crops (based on empirical Indian/global crop dataset)
# 5 benchmark test samples per crop = 110 test samples
# Testing with slight environmental variations to test robustness
crop_benchmarks = {
    "rice": [
        [80, 40, 40, 24.5, 82.0, 6.5, 200.0],
        [90, 42, 43, 20.8, 82.5, 6.4, 210.0],
        [85, 45, 42, 23.0, 80.0, 6.2, 195.0],
        [75, 38, 39, 25.0, 84.0, 6.8, 220.0],
        [88, 41, 40, 22.5, 81.0, 6.6, 205.0]
    ],
    "maize": [
        [80, 45, 20, 23.0, 65.0, 6.5, 70.0],
        [85, 48, 22, 24.0, 62.0, 6.3, 75.0],
        [78, 42, 19, 22.5, 67.0, 6.8, 68.0],
        [82, 46, 21, 25.0, 60.0, 6.1, 80.0],
        [88, 50, 20, 21.8, 68.0, 6.4, 72.0]
    ],
    "chickpea": [
        [40, 60, 80, 18.0, 16.0, 7.0, 80.0],
        [42, 62, 78, 17.5, 17.0, 7.2, 85.0],
        [38, 58, 82, 19.0, 15.0, 6.9, 75.0],
        [41, 65, 80, 18.5, 18.0, 7.1, 78.0],
        [39, 59, 79, 17.0, 16.5, 7.3, 82.0]
    ],
    "kidneybeans": [
        [20, 60, 20, 20.0, 21.0, 5.7, 105.0],
        [22, 58, 22, 19.5, 22.0, 5.8, 100.0],
        [18, 62, 19, 20.5, 20.0, 5.6, 110.0],
        [25, 61, 21, 21.0, 23.0, 5.9, 98.0],
        [19, 59, 18, 18.8, 21.5, 5.5, 108.0]
    ],
    "pigeonpeas": [
        [20, 65, 20, 28.0, 45.0, 5.7, 150.0],
        [22, 68, 22, 27.5, 48.0, 5.8, 145.0],
        [18, 62, 19, 29.0, 43.0, 5.5, 155.0],
        [24, 70, 21, 28.5, 46.0, 6.0, 140.0],
        [19, 64, 18, 26.8, 50.0, 5.6, 160.0]
    ],
    "mothbeans": [
        [20, 45, 20, 28.0, 55.0, 7.2, 50.0],
        [22, 48, 22, 29.0, 52.0, 7.0, 48.0],
        [18, 42, 19, 27.5, 58.0, 7.4, 55.0],
        [24, 46, 21, 30.0, 50.0, 6.9, 45.0],
        [19, 44, 18, 28.5, 56.0, 7.1, 52.0]
    ],
    "mungbean": [
        [20, 45, 20, 28.0, 85.0, 6.7, 50.0],
        [22, 48, 22, 28.5, 83.0, 6.8, 48.0],
        [18, 42, 19, 27.5, 88.0, 6.6, 52.0],
        [25, 47, 21, 29.0, 86.0, 6.5, 46.0],
        [19, 44, 18, 27.0, 84.0, 6.9, 54.0]
    ],
    "blackgram": [
        [40, 65, 20, 30.0, 65.0, 7.2, 65.0],
        [42, 68, 22, 29.5, 68.0, 7.0, 68.0],
        [38, 62, 19, 31.0, 62.0, 7.4, 62.0],
        [44, 70, 21, 30.5, 66.0, 7.1, 70.0],
        [39, 64, 18, 28.8, 64.0, 7.3, 63.0]
    ],
    "lentil": [
        [20, 65, 20, 24.0, 65.0, 6.9, 45.0],
        [22, 68, 22, 23.5, 63.0, 7.0, 42.0],
        [18, 62, 19, 25.0, 68.0, 6.8, 48.0],
        [24, 70, 21, 24.5, 66.0, 7.1, 40.0],
        [19, 63, 18, 22.8, 62.0, 6.7, 46.0]
    ],
    "pomegranate": [
        [20, 20, 40, 22.0, 90.0, 6.8, 110.0],
        [22, 22, 42, 21.5, 88.0, 6.7, 108.0],
        [18, 18, 38, 23.0, 92.0, 6.9, 112.0],
        [24, 25, 41, 22.5, 91.0, 7.0, 105.0],
        [19, 19, 39, 20.8, 89.0, 6.6, 115.0]
    ],
    "banana": [
        [100, 75, 50, 27.0, 80.0, 6.0, 100.0],
        [105, 80, 52, 26.5, 82.0, 6.2, 105.0],
        [98, 72, 48, 28.0, 78.0, 5.9, 95.0],
        [110, 82, 55, 27.5, 85.0, 6.4, 110.0],
        [95, 70, 47, 25.8, 79.0, 5.8, 98.0]
    ],
    "mango": [
        [20, 25, 30, 31.0, 50.0, 5.5, 95.0],
        [22, 28, 32, 32.0, 52.0, 5.6, 92.0],
        [18, 22, 28, 30.0, 48.0, 5.4, 98.0],
        [24, 30, 31, 33.0, 54.0, 5.8, 90.0],
        [19, 24, 29, 29.5, 49.0, 5.3, 100.0]
    ],
    "grapes": [
        [20, 130, 200, 24.0, 81.0, 6.0, 70.0],
        [22, 135, 205, 23.5, 82.0, 6.1, 72.0],
        [18, 128, 198, 25.0, 80.0, 5.9, 68.0],
        [25, 140, 202, 24.5, 83.0, 6.3, 75.0],
        [19, 125, 195, 22.8, 79.0, 5.8, 69.0]
    ],
    "watermelon": [
        [100, 18, 50, 26.0, 85.0, 6.5, 50.0],
        [105, 20, 52, 25.5, 86.0, 6.4, 52.0],
        [98, 17, 48, 27.0, 84.0, 6.6, 48.0],
        [110, 22, 53, 26.5, 88.0, 6.7, 55.0],
        [95, 16, 47, 24.8, 83.0, 6.3, 49.0]
    ],
    "muskmelon": [
        [100, 18, 50, 28.0, 92.0, 6.4, 25.0],
        [102, 19, 52, 28.5, 93.0, 6.5, 26.0],
        [98, 17, 48, 27.5, 91.0, 6.3, 24.0],
        [105, 21, 51, 29.0, 94.0, 6.6, 28.0],
        [96, 16, 49, 27.0, 90.0, 6.2, 23.0]
    ],
    "apple": [
        [20, 135, 200, 22.0, 92.0, 5.9, 110.0],
        [22, 138, 202, 21.5, 93.0, 6.0, 112.0],
        [18, 132, 198, 23.0, 91.0, 5.8, 108.0],
        [24, 140, 205, 22.5, 94.0, 6.1, 115.0],
        [19, 130, 195, 20.8, 90.0, 5.7, 105.0]
    ],
    "orange": [
        [20, 15, 10, 23.0, 92.0, 7.0, 110.0],
        [22, 18, 12, 22.5, 93.0, 7.1, 112.0],
        [18, 14, 9, 24.0, 91.0, 6.9, 108.0],
        [25, 20, 14, 23.5, 94.0, 7.3, 115.0],
        [19, 16, 11, 21.8, 90.0, 6.8, 105.0]
    ],
    "papaya": [
        [50, 60, 50, 34.0, 92.0, 6.7, 150.0],
        [52, 62, 52, 33.5, 93.0, 6.8, 155.0],
        [48, 58, 48, 35.0, 91.0, 6.6, 145.0],
        [55, 65, 54, 34.5, 94.0, 6.9, 160.0],
        [49, 59, 49, 32.8, 90.0, 6.5, 148.0]
    ],
    "coconut": [
        [20, 15, 30, 27.0, 96.0, 6.0, 175.0],
        [22, 18, 32, 26.5, 97.0, 6.1, 180.0],
        [18, 14, 28, 28.0, 95.0, 5.9, 170.0],
        [25, 19, 34, 27.5, 98.0, 6.2, 185.0],
        [19, 16, 29, 25.8, 94.0, 5.8, 172.0]
    ],
    "cotton": [
        [120, 45, 20, 24.0, 80.0, 6.8, 80.0],
        [125, 48, 22, 23.5, 82.0, 6.9, 82.0],
        [118, 42, 19, 25.0, 78.0, 6.7, 78.0],
        [130, 50, 24, 24.5, 84.0, 7.1, 85.0],
        [115, 40, 18, 22.8, 79.0, 6.6, 75.0]
    ],
    "jute": [
        [80, 45, 40, 25.0, 80.0, 6.7, 175.0],
        [85, 48, 42, 24.5, 82.0, 6.8, 180.0],
        [78, 42, 38, 26.0, 78.0, 6.6, 170.0],
        [88, 50, 44, 25.5, 83.0, 7.0, 185.0],
        [79, 44, 39, 23.8, 79.0, 6.5, 172.0]
    ],
    "coffee": [
        [100, 30, 30, 26.0, 58.0, 6.8, 160.0],
        [105, 32, 32, 25.5, 60.0, 6.9, 165.0],
        [98, 28, 28, 27.0, 56.0, 6.7, 155.0],
        [110, 35, 34, 26.5, 62.0, 7.0, 170.0],
        [95, 29, 29, 24.8, 57.0, 6.6, 158.0]
    ]
}

y_true = []
y_pred = []
confidences = []

for crop_name, samples in crop_benchmarks.items():
    for sample in samples:
        y_true.append(crop_name)
        scaled = crop_scaler.transform([sample])
        pred = crop_model.predict(scaled)[0]
        proba = crop_model.predict_proba(scaled)[0]
        y_pred.append(pred)
        confidences.append(np.max(proba) * 100)

print(f"\nTotal test samples: {len(y_true)}")
report = classification_report(y_true, y_pred, target_names=crop_model.classes_, digits=4)
print("\nClassification Report:\n", report)
print(f"Mean Confidence across all predictions: {np.mean(confidences):.2f}%")
print(f"Min Confidence: {np.min(confidences):.2f}% | Max Confidence: {np.max(confidences):.2f}%")

print("\n==================================================")
print("COMPREHENSIVE DISEASE MODEL EVALUATION")
print("==================================================")
d_model = tf.keras.models.load_model(Config.DISEASE_MODEL_PATH)
print(f"Disease Model Input: {d_model.input_shape}, Output: {d_model.output_shape}")
print(f"Configured Classes ({len(Config.DISEASE_CLASSES)}):")
for i, c in enumerate(Config.DISEASE_CLASSES):
    print(f"  [{i:2d}] {c}")

upload_dir = Config.UPLOAD_FOLDER
upload_files = sorted([f for f in os.listdir(upload_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])
print(f"\nFound {len(upload_files)} images in uploads directory for empirical evaluation.")

disease_preds = []
disease_confs = []
for fname in upload_files:
    fpath = os.path.join(upload_dir, fname)
    img = tf.keras.utils.load_img(fpath, target_size=Config.DISEASE_IMG_SIZE)
    arr = tf.keras.utils.img_to_array(img)
    arr = np.expand_dims(arr, axis=0).astype("float32")
    
    preds = d_model.predict(arr, verbose=0)[0]
    top_idx = int(np.argmax(preds))
    conf = float(preds[top_idx] * 100)
    disease = Config.DISEASE_CLASSES[top_idx]
    
    disease_preds.append((fname, disease, conf, top_idx))
    disease_confs.append(conf)

print(f"\nEmpirical Predictions on Uploaded Test Images:")
for fname, disease, conf, top_idx in disease_preds:
    print(f"  {fname[:20]}... -> Class [{top_idx:2d}] {disease:35s} ({conf:5.2f}%)")

print("\nEvaluation completed successfully.")
