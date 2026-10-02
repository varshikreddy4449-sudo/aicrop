#!/usr/bin/env python
"""
Verification script to check MongoDB and disease solutions setup.
Run this before starting the Flask app to diagnose issues.
"""
import sys
from db import disease_solutions_collection
from config import Config
from utils.model_loader import predict_disease
import os

print("=" * 70)
print("AgriAI Setup Verification")
print("=" * 70)

# 1. Check MongoDB connection
print("\n1️⃣ Checking MongoDB Connection...")
try:
    count = disease_solutions_collection.count_documents({})
    print(f"   ✓ MongoDB connected. Disease solutions in DB: {count}")
except Exception as e:
    print(f"   ✗ MongoDB connection failed: {e}")
    sys.exit(1)

# 2. Verify disease solutions are seeded
print("\n2️⃣ Checking Disease Solutions...")
if count == 0:
    print("   ⚠ Disease solutions collection is EMPTY!")
    print("   Seeding now...")
    solutions = [
        {"disease_name": "Apple - Apple Scab", "cause": "Fungal disease", "solution": "Apply fungicide sprays."},
        {"disease_name": "Apple - Healthy", "cause": "No disease detected.", "solution": "Plant appears healthy."},
        {"disease_name": "Tomato - Healthy", "cause": "No disease detected.", "solution": "Plant appears healthy."},
        {"disease_name": "Tomato - Early Blight", "cause": "Fungal disease", "solution": "Remove infected leaves."},
    ]
    for item in solutions:
        disease_solutions_collection.update_one({"disease_name": item["disease_name"]}, {"$set": item}, upsert=True)
    print(f"   ✓ Seeded {len(solutions)} sample solutions")
else:
    sample = disease_solutions_collection.find_one()
    print(f"   ✓ Sample record: {sample.get('disease_name', 'N/A')}")

# 3. Check disease model classes
print("\n3️⃣ Checking Disease Model Classes...")
classes = Config.DISEASE_CLASSES
print(f"   ✓ Found {len(classes)} disease classes")
print(f"   Sample classes: {classes[:3]}")

# 4. Verify model predictions work
print("\n4️⃣ Testing Model Prediction Function...")
test_image = r"c:\Users\Lenovo\Desktop\MiniPro(Crop)\AI-Crop1-main\dataset\Test\Tomato - Healthy\001cbe78-1d5c-45eb-877f-f409526032d5.JPG"
if os.path.exists(test_image):
    try:
        result = predict_disease(test_image)
        print(f"   ✓ Prediction successful!")
        print(f"     Disease: {result['disease_name']}")
        print(f"     Confidence: {result['confidence']}%")
    except Exception as e:
        print(f"   ✗ Prediction failed: {e}")
else:
    print(f"   ⚠ Test image not found. Skipping prediction test.")
    print(f"   (Looked for: {test_image})")

# 5. Final status
print("\n" + "=" * 70)
print("✓ Setup verification complete!")
print("=" * 70)
print("\nNext steps:")
print("1. Ensure MongoDB is running (mongod)")
print("2. Run: python app.py")
print("3. Visit: http://localhost:5000")
