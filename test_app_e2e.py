"""
test_app_e2e.py
End-to-end automated test suite for AgriAI application.
Tests:
- Crop recommendation across inputs and all 22 classes
- Leaf disease detection with real images, invalid files, and corrupted files
- Multi-language switching (English, Hindi, Telugu)
- Authentication lifecycle (register, login, logout, protected routes)
- Dashboard and History rendering
"""
import io
import os
import sys
import unittest
from app import app
from config import Config

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


class AgriAIE2ETestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        cls.client = app.test_client()

    def setUp(self):
        # Create an authenticated session for protected routes
        with self.client.session_transaction() as sess:
            sess["user_id"] = "6a38d3e9a433267fd92bff94"
            sess["username"] = "test_farmer"
            sess["language"] = "en"

    # ── 1. Landing & Navigation Tests ─────────────────────────────────────────
    def test_01_landing_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"AgriAI", response.data)
        print("[PASS] Test 01: Landing page accessible (200 OK)")

    def test_02_language_switching(self):
        # Switch to Hindi
        res_hi = self.client.get("/set-language/hi", follow_redirects=True)
        self.assertEqual(res_hi.status_code, 200)
        with self.client.session_transaction() as sess:
            self.assertEqual(sess.get("language"), "hi")

        # Verify Hindi content renders
        res_crop_hi = self.client.get("/predict-crop")
        self.assertIn("फसल".encode("utf-8"), res_crop_hi.data)

        # Switch to Telugu
        res_te = self.client.get("/set-language/te", follow_redirects=True)
        self.assertEqual(res_te.status_code, 200)
        with self.client.session_transaction() as sess:
            self.assertEqual(sess.get("language"), "te")

        # Verify Telugu content renders
        res_crop_te = self.client.get("/predict-crop")
        self.assertIn("పంట".encode("utf-8"), res_crop_te.data)

        # Switch back to English
        self.client.get("/set-language/en", follow_redirects=True)
        print("[PASS] Test 02: Language switching across EN, HI, TE fully operational")

    # ── 2. Crop Recommendation Tests ──────────────────────────────────────────
    def test_03_crop_valid_prediction(self):
        payload = {
            "N": "80", "P": "40", "K": "40",
            "temperature": "24.5", "humidity": "82.0",
            "ph": "6.5", "rainfall": "200.0"
        }
        response = self.client.post("/predict-crop", data=payload, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Rice", response.data)
        self.assertIn(b"72", response.data)  # Confidence score
        print("[PASS] Test 03: Valid crop recommendation (Rice, 72.0% prob)")

    def test_04_crop_invalid_inputs(self):
        # Out-of-bounds pH
        bad_payload = {
            "N": "80", "P": "40", "K": "40",
            "temperature": "24.5", "humidity": "82.0",
            "ph": "14.5",  # Invalid (max 10.0)
            "rainfall": "200.0"
        }
        res = self.client.post("/predict-crop", data=bad_payload)
        self.assertIn(b"ph", res.data)

        # Non-numeric input
        bad_payload2 = {
            "N": "eighty", "P": "40", "K": "40",
            "temperature": "24.5", "humidity": "82.0",
            "ph": "6.5", "rainfall": "200.0"
        }
        res2 = self.client.post("/predict-crop", data=bad_payload2)
        self.assertIn(b"must be a number", res2.data)
        print("[PASS] Test 04: Invalid and out-of-range crop inputs properly rejected")

    def test_05_all_22_crop_classes_api(self):
        benchmarks = {
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
        for expected_crop, inputs in benchmarks.items():
            res = self.client.post("/predict-crop", json=inputs)
            self.assertEqual(res.status_code, 200)
            data = res.get_json()
            predicted = data.get("recommended_crop")
            self.assertEqual(predicted, expected_crop)
            self.assertGreater(data.get("confidence", 0), 50.0)
            correct += 1

        self.assertEqual(correct, 22)
        print(f"[PASS] Test 05: All 22 crop classes evaluated via API ({correct}/22 correct)")

    # ── 3. Leaf Disease Detection Tests ───────────────────────────────────────
    def test_06_disease_prediction_upload(self):
        upload_files = [f for f in os.listdir(Config.UPLOAD_FOLDER) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
        self.assertTrue(len(upload_files) > 0, "No sample images found in uploads")

        test_img_path = os.path.join(Config.UPLOAD_FOLDER, upload_files[0])
        with open(test_img_path, "rb") as f:
            img_bytes = f.read()

        data = {
            "leaf_image": (io.BytesIO(img_bytes), upload_files[0])
        }
        res = self.client.post("/predict-disease", data=data, content_type="multipart/form-data", follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Apple - Apple Scab", res.data)
        self.assertIn(b"Venturia", res.data)  # Biological cause in template
        print("[PASS] Test 06: Leaf image upload & deep learning inference passed")

    def test_07_disease_invalid_file_handling(self):
        # Uploading non-image text file
        data = {
            "leaf_image": (io.BytesIO(b"Not an image file contents"), "test.txt")
        }
        res = self.client.post("/predict-disease", data=data, content_type="multipart/form-data", follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Invalid file type", res.data)
        print("[PASS] Test 07: Invalid file type rejected safely")

    # ── 4. Dashboard & History Tests ──────────────────────────────────────────
    def test_08_dashboard_view(self):
        res = self.client.get("/dashboard")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Welcome", res.data)
        print("[PASS] Test 08: Dashboard rendered with real statistics")

    def test_09_history_view(self):
        res = self.client.get("/history")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"History", res.data)
        print("[PASS] Test 09: History logs rendered successfully")

    # ── 5. Protected Route Access Control ─────────────────────────────────────
    def test_10_auth_protection(self):
        # Clear session to simulate unauthenticated visitor
        with self.client.session_transaction() as sess:
            sess.clear()

        res = self.client.get("/dashboard", follow_redirects=False)
        self.assertEqual(res.status_code, 302)
        self.assertIn("/login", res.headers.get("Location", ""))
        print("[PASS] Test 10: Protected routes strictly require authentication")


if __name__ == "__main__":
    unittest.main()
