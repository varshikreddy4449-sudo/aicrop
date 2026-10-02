import os
import pickle
import numpy as np

print("==========================================")
print("1. AUDITING CROP RECOMMENDATION MODEL")
print("==========================================")

crop_model_path = os.path.join("models", "model.pkl")
crop_scaler_path = os.path.join("models", "minmaxscaler.pkl")

print(f"Crop model path: {crop_model_path} (exists: {os.path.exists(crop_model_path)})")
print(f"Crop scaler path: {crop_scaler_path} (exists: {os.path.exists(crop_scaler_path)})")

if os.path.exists(crop_model_path):
    with open(crop_model_path, "rb") as f:
        crop_model = pickle.load(f)
    print("Crop Model Type:", type(crop_model))
    print("Model attributes/parameters:")
    for attr in ["classes_", "n_classes_", "n_features_in_", "feature_names_in_", "estimators_", "n_estimators"]:
        if hasattr(crop_model, attr):
            val = getattr(crop_model, attr)
            if attr == "classes_":
                print(f"  {attr} (count={len(val)}): {list(val)}")
            elif attr == "estimators_":
                print(f"  {attr}: count={len(val)}")
            else:
                print(f"  {attr}: {val}")

if os.path.exists(crop_scaler_path):
    with open(crop_scaler_path, "rb") as f:
        scaler = pickle.load(f)
    print("\nScaler Type:", type(scaler))
    for attr in ["n_features_in_", "feature_names_in_", "data_min_", "data_max_", "scale_", "min_"]:
        if hasattr(scaler, attr):
            print(f"  Scaler {attr}: {getattr(scaler, attr)}")

print("\n==========================================")
print("2. AUDITING DISEASE MODEL")
print("==========================================")

import tensorflow as tf

disease_model_path = os.path.join("models", "disease_model.h5")
print(f"Disease model path: {disease_model_path} (exists: {os.path.exists(disease_model_path)})")

if os.path.exists(disease_model_path):
    d_model = tf.keras.models.load_model(disease_model_path)
    print("Disease Model Summary:")
    d_model.summary()
    print("Input shape:", d_model.input_shape)
    print("Output shape:", d_model.output_shape)
    print("Number of output units:", d_model.output_shape[-1])
    print("Layers:")
    for i, layer in enumerate(d_model.layers):
        print(f"  Layer {i}: {layer.name} ({type(layer).__name__}), input: {getattr(layer, 'input_shape', 'N/A')}, output: {getattr(layer, 'output_shape', 'N/A')}")

print("\n==========================================")
print("3. AUDITING UPLOADED TEST IMAGES")
print("==========================================")
upload_dir = "uploads"
if os.path.exists(upload_dir):
    files = [f for f in os.listdir(upload_dir) if os.path.isfile(os.path.join(upload_dir, f))]
    print(f"Found {len(files)} files in {upload_dir}")
    for f in files:
        f_path = os.path.join(upload_dir, f)
        print(f"  File: {f} ({os.path.getsize(f_path)} bytes)")

print("\nAudit script complete.")
