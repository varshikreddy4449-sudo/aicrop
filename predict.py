"""
predict.py
Standalone test script to run leaf disease prediction on any image.
Usage: python predict.py [optional_image_path]
"""
import os
import sys
from config import Config
from utils.model_loader import predict_disease
from utils.translations import get_disease_translation

def main():
    # Default to first image in uploads or prompt user
    img_path = None
    if len(sys.argv) > 1:
        img_path = sys.argv[1]
    else:
        upload_files = [f for f in os.listdir(Config.UPLOAD_FOLDER) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
        if upload_files:
            img_path = os.path.join(Config.UPLOAD_FOLDER, upload_files[0])
            print(f"Using default sample image: {img_path}")
        else:
            print("No test image provided and no files found in uploads.")
            return

    print("==========================================")
    print("AGRIAI LEAF DISEASE PREDICTION TEST")
    print("==========================================")
    print(f"Target Image: {img_path}")
    
    try:
        result = predict_disease(img_path)
        pathology = get_disease_translation(result['disease_name'], 'en')
        print(f"\nStatus:      {result['status']}")
        print(f"Disease:     {result['disease_name']}")
        print(f"Confidence:  {result['confidence']}%")
        print(f"Cause:       {pathology.get('cause', 'N/A')}")
        print(f"Treatment:   {pathology.get('treatment', 'N/A')}")
        print(f"Organic:     {pathology.get('organic', 'N/A')}")
        print(f"Prevention:  {pathology.get('prevention', 'N/A')}")
        print("\nTop 3 Predictions:")
        for i, p in enumerate(result['top_predictions'], 1):
            print(f"  {i}. {p['disease_name']} ({p['confidence']}%)")
    except Exception as e:
        print(f"Prediction failed: {e}")

    print("==========================================")

if __name__ == "__main__":
    main()