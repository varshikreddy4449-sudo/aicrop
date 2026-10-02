import os
import sys
import pickle
import numpy as np
import tensorflow as tf
from config import Config
from utils.model_loader import (
    get_crop_model,
    get_crop_scaler,
    predict_crop,
    get_disease_model,
    predict_disease,
    CROP_FEATURES
)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 70)
print("PART 1: CROP MODEL INSPECTION & VERIFICATION")
print("=" * 70)

# 1. Load model and scaler
crop_model = get_crop_model()
crop_scaler = get_crop_scaler()

print(f"Model file: models/model.pkl")
print(f"Model class: {crop_model.__class__.__name__}")
print(f"Module: {crop_model.__class__.__module__}")
print(f"Number of trees (estimators): {len(crop_model.estimators_)}")
print(f"Criterion: {crop_model.criterion}")
print(f"Bootstrap: {crop_model.bootstrap}")

# 2. Exact crop classes
crop_classes = list(crop_model.classes_)
print(f"\nExact number of crop classes: {len(crop_classes)}")
print("Exact crop classes list:")
for i, c in enumerate(crop_classes, 1):
    print(f"  {i:2d}. {c}")

# 3. Features and order
scaler_features = list(crop_scaler.feature_names_in_)
print(f"\nExact number of input features: {len(scaler_features)}")
print(f"Scaler feature names: {scaler_features}")
print(f"Code CROP_FEATURES:   {CROP_FEATURES}")
features_match = (scaler_features == CROP_FEATURES)
print(f"Features match exactly in name and order: {features_match}")
print(f"Scaler Data Min: {list(crop_scaler.data_min_)}")
print(f"Scaler Data Max: {list(crop_scaler.data_max_)}")

# 4. Test crop prediction pipeline
print("\n--- Testing Crop Prediction Pipeline with Valid Inputs ---")
test_inputs = [
    {"name": "Rice sample", "features": {"N": 80, "P": 40, "K": 40, "temperature": 24.5, "humidity": 82.0, "ph": 6.5, "rainfall": 200.0}},
    {"name": "Maize sample", "features": {"N": 80, "P": 45, "K": 20, "temperature": 23.0, "humidity": 65.0, "ph": 6.5, "rainfall": 70.0}},
    {"name": "Chickpea sample", "features": {"N": 40, "P": 60, "K": 80, "temperature": 18.0, "humidity": 16.0, "ph": 7.0, "rainfall": 80.0}},
    {"name": "Cotton sample", "features": {"N": 120, "P": 45, "K": 20, "temperature": 24.0, "humidity": 80.0, "ph": 6.8, "rainfall": 80.0}},
    {"name": "Apple sample", "features": {"N": 20, "P": 135, "K": 200, "temperature": 22.0, "humidity": 92.0, "ph": 5.9, "rainfall": 110.0}},
]

all_in_classes = True
for t in test_inputs:
    res = predict_crop(t["features"])
    is_valid_class = res["recommended_crop"] in crop_classes
    if not is_valid_class:
        all_in_classes = False
    print(f"  {t['name']:16s} -> Predicted: {res['recommended_crop']:12s} | Confidence: {res['confidence']}% | In Classes: {is_valid_class}")

print(f"\nAll predictions correspond to actual model classes: {all_in_classes}")

print("\n" + "=" * 70)
print("PART 2: DISEASE MODEL INSPECTION & VERIFICATION")
print("=" * 70)

# 1. Load model
d_model = get_disease_model()
print(f"Model file: models/disease_model.h5")
print(f"Model class: {d_model.__class__.__name__}")
print(f"Input shape: {d_model.input_shape}")
print(f"Output shape: {d_model.output_shape}")
print(f"Total layers: {len(d_model.layers)}")
for i, l in enumerate(d_model.layers):
    print(f"  Layer {i}: {l.name} ({l.__class__.__name__}) -> output shape: {getattr(l, 'output_shape', 'N/A')}")

# 2. Exact disease classes
disease_classes = Config.DISEASE_CLASSES
print(f"\nExact number of disease classes: {len(disease_classes)}")
print("Exact disease classes list:")
for i, c in enumerate(disease_classes, 1):
    healthy_tag = " [HEALTHY]" if "Healthy" in c else ""
    print(f"  {i:2d}. {c}{healthy_tag}")

healthy_classes = [c for c in disease_classes if "Healthy" in c]
diseased_classes = [c for c in disease_classes if "Healthy" not in c]
print(f"\nHealthy plant classes: {len(healthy_classes)}")
print(f"Diseased classes:      {len(diseased_classes)}")

# 3. Input size and preprocessing
print(f"\nExpected image input size: {Config.DISEASE_IMG_SIZE}")
print(f"Model layer 0 rescaling: {d_model.layers[0].scale} (maps [0, 255] RGB float32 into [0, 1])")

# 4. Test disease prediction pipeline on real upload images
print("\n--- Testing Disease Prediction Pipeline on Real Upload Images ---")
upload_dir = Config.UPLOAD_FOLDER
upload_files = sorted([f for f in os.listdir(upload_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])
print(f"Found {len(upload_files)} real images in {upload_dir}")

disease_all_in_classes = True
test_predictions_summary = {}

for f in upload_files:
    fpath = os.path.join(upload_dir, f)
    res = predict_disease(fpath)
    pred_name = res["disease_name"]
    is_valid = pred_name in disease_classes
    if not is_valid:
        disease_all_in_classes = False
    test_predictions_summary[f] = res
    print(f"  {f[:18]}... -> Status: {res['status']:8s} | Disease: {pred_name:35s} | Conf: {res['confidence']}% | In Classes: {is_valid}")

print(f"\nAll disease predictions correspond to actual model classes: {disease_all_in_classes}")

unique_predicted_diseases = set(r["disease_name"] for r in test_predictions_summary.values())
print(f"Distinct disease classes predicted across test set: {len(unique_predicted_diseases)}")
for d in sorted(unique_predicted_diseases):
    count = sum(1 for r in test_predictions_summary.values() if r["disease_name"] == d)
    print(f"  - {d}: {count} image(s)")

print("\n" + "=" * 70)
print("PART 3: ORIGIN OF THE '99.09%' ACCURACY METRIC")
print("=" * 70)
print("Inspecting evaluate_models.py...")
with open("evaluate_models.py", "r", encoding="utf-8") as f:
    eval_code = f.read()

has_benchmarks = "crop_benchmarks" in eval_code
print(f"Contains crop_benchmarks: {has_benchmarks}")
if has_benchmarks:
    # Count samples
    import evaluate_models
    total_samples = len(evaluate_models.y_true)
    total_correct = sum(1 for yt, yp in zip(evaluate_models.y_true, evaluate_models.y_pred) if yt == yp)
    acc = total_correct / total_samples
    print(f"Model evaluated: Crop Recommendation Model (RandomForestClassifier)")
    print(f"Dataset: Empirical agronomic benchmark test set (5 environmental variations per crop)")
    print(f"Total test samples: {total_samples} samples across all 22 classes")
    print(f"Total correct: {total_correct} / {total_samples}")
    print(f"Exact calculated accuracy: {total_correct}/{total_samples} = {acc * 100:.2f}% ({acc:.4f})")
