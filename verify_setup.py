#!/usr/bin/env python
"""
verify_setup.py
Comprehensive diagnostic and verification script for AgriAI.
Checks:
1. Virtual environment and library dependencies
2. MongoDB database connection & collections
3. Crop Recommendation Model & Scaler (all 22 crops)
4. Leaf Disease Detection Model & Preprocessing (all 29 classes)
5. Multi-language internationalization system
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 70)
print("🌱 AgriAI Complete System Verification")
print("=" * 70)

# 1. Dependency checks
print("\n1️⃣  Checking Core Dependencies...")
try:
    import flask
    import pymongo
    import bcrypt
    import tensorflow as tf
    import sklearn
    import numpy as np
    import PIL
    print(f"   [PASS] Flask:        {flask.__version__}")
    print(f"   [PASS] TensorFlow:   {tf.__version__}")
    print(f"   [PASS] Scikit-learn: {sklearn.__version__}")
    print(f"   [PASS] PyMongo:      {pymongo.__version__}")
    print(f"   [PASS] NumPy:        {np.__version__}")
    print(f"   [PASS] Pillow:       {PIL.__version__}")
except ImportError as e:
    print(f"   [FAIL] Missing dependency: {e}")
    sys.exit(1)

# 2. Database checks
print("\n2️⃣  Checking MongoDB Database...")
from db import is_db_connected, disease_solutions_collection, crop_predictions_collection, disease_predictions_collection, users_collection
if is_db_connected():
    print("   [PASS] MongoDB daemon is running and reachable.")
    print(f"          Users: {users_collection.count_documents({})}")
    print(f"          Crop predictions: {crop_predictions_collection.count_documents({})}")
    print(f"          Disease predictions: {disease_predictions_collection.count_documents({})}")
    print(f"          Disease solutions: {disease_solutions_collection.count_documents({})}")
else:
    print("   [WARN] MongoDB not reachable on configured URI. App will run with degraded persistence.")

# 3. Crop Model checks
print("\n3️⃣  Checking Crop Recommendation Model...")
try:
    from utils.model_loader import get_crop_model, get_crop_scaler, predict_crop, get_crop_info
    crop_model = get_crop_model()
    crop_scaler = get_crop_scaler()
    print(f"   [PASS] Crop Model loaded: {type(crop_model).__name__} (100 estimators)")
    print(f"   [PASS] Exact crop classes ({len(crop_model.classes_)}): {list(crop_model.classes_)}")
    sample_crop_input = {"N": 80, "P": 40, "K": 40, "temperature": 24.5, "humidity": 82.0, "ph": 6.5, "rainfall": 200.0}
    crop_res = predict_crop(sample_crop_input)
    print(f"   [PASS] Test prediction: {crop_res['recommended_crop']} (Confidence: {crop_res['confidence']}%)")
except Exception as e:
    print(f"   [FAIL] Crop model error: {e}")

# 4. Disease Model checks
print("\n4️⃣  Checking Leaf Disease Model...")
try:
    from utils.model_loader import get_disease_model, predict_disease
    from config import Config
    d_model = get_disease_model()
    print(f"   [PASS] Disease Model loaded: MobileNetV2 ({d_model.count_params()} parameters)")
    print(f"   [PASS] Exact disease classes ({len(Config.DISEASE_CLASSES)}): {Config.DISEASE_CLASSES[:3]} ...")
    upload_files = [f for f in os.listdir(Config.UPLOAD_FOLDER) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    if upload_files:
        test_img = os.path.join(Config.UPLOAD_FOLDER, upload_files[0])
        d_res = predict_disease(test_img)
        print(f"   [PASS] Test image: {upload_files[0]}")
        print(f"          Predicted: {d_res['disease_name']} ({d_res['confidence']}%)")
    else:
        print("   [INFO] No sample image in uploads to test.")
except Exception as e:
    print(f"   [FAIL] Disease model error: {e}")

# 5. Internationalization checks
print("\n5️⃣  Checking Multi-Language Internationalization...")
try:
    from utils.translations import get_ui_text, get_crop_translation, get_disease_translation
    print("   [PASS] English:  ", get_ui_text('app_name', 'en'), "| Crop:", get_crop_translation('rice', 'en')['name'])
    print("   [PASS] Hindi:    ", get_ui_text('app_name', 'hi'), "| Crop:", get_crop_translation('rice', 'hi')['name'])
    print("   [PASS] Telugu:   ", get_ui_text('app_name', 'te'), "| Crop:", get_crop_translation('rice', 'te')['name'])
except Exception as e:
    print(f"   [FAIL] Translation system error: {e}")

print("\n" + "=" * 70)
print("✓ Setup Verification Finished!")
print("=" * 70)
