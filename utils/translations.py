"""
utils/translations.py
Centralized Internationalization (i18n) for AgriAI.
Provides complete translations for English (en), Hindi (hi), and Telugu (te).
"""

LANGUAGES = {
    "en": "English",
    "hi": "हिंदी (Hindi)",
    "te": "తెలుగు (Telugu)"
}

DEFAULT_LANGUAGE = "en"

# UI String Translations
STRINGS = {
    "en": {
        "app_name": "AgriAI",
        "tagline": "AI-Powered Agriculture Platform",
        "hero_title": "Smart Farming with AI Precision",
        "hero_desc": "Empowering farmers with intelligent crop recommendations based on soil & climate data, and instant leaf disease diagnosis from photos.",
        "nav_home": "Home",
        "nav_dashboard": "Dashboard",
        "nav_crop": "Crop Recommendation",
        "nav_disease": "Disease Detection",
        "nav_history": "History",
        "nav_login": "Login",
        "nav_register": "Register",
        "nav_logout": "Logout",
        "welcome": "Welcome",
        
        # Actions
        "btn_login": "Sign In",
        "btn_register": "Create Account",
        "btn_predict_crop": "Recommend Best Crop",
        "btn_predict_disease": "Diagnose Leaf Disease",
        "btn_reset": "Reset",
        "btn_clear": "Clear Image",
        "btn_listen": "Listen (Audio)",
        "btn_stop": "Stop Audio",
        "btn_replay": "Replay",
        "btn_explore": "Get Started",
        "btn_view_history": "View Full History",
        
        # Form fields
        "nitrogen_label": "Nitrogen (N)",
        "nitrogen_desc": "Ratio in soil (0 - 140 kg/ha)",
        "phosphorus_label": "Phosphorus (P)",
        "phosphorus_desc": "Ratio in soil (5 - 145 kg/ha)",
        "potassium_label": "Potassium (K)",
        "potassium_desc": "Ratio in soil (5 - 205 kg/ha)",
        "temperature_label": "Temperature (°C)",
        "temperature_desc": "Average air temp (8 - 44 °C)",
        "humidity_label": "Relative Humidity (%)",
        "humidity_desc": "Relative humidity (14 - 100%)",
        "ph_label": "Soil pH",
        "ph_desc": "Acidity / Alkalinity (3.5 - 10.0)",
        "rainfall_label": "Rainfall (mm)",
        "rainfall_desc": "Annual precipitation (20 - 300 mm)",
        
        # Upload
        "drag_drop_title": "Drag & Drop leaf photo here",
        "drag_drop_desc": "or click to browse from device (JPG, PNG, WEBP up to 5MB)",
        "analyzing_title": "Analyzing Leaf with Deep Learning...",
        "analyzing_desc": "Running MobileNetV2 neural network for accurate disease identification",
        
        # Results
        "result_recommended_crop": "Recommended Crop",
        "result_confidence": "Model Confidence",
        "result_growing_conditions": "Optimal Growing Conditions",
        "result_season": "Optimal Season",
        "result_soil": "Recommended Soil Type",
        "result_care": "Farming & Care Guide",
        "result_leaf_status": "Health Status",
        "result_status_healthy": "HEALTHY PLANT",
        "result_status_diseased": "DISEASE DETECTED",
        "result_disease_detected": "Diagnosed Disease",
        "result_cause": "Cause & Pathology",
        "result_symptoms": "Visible Symptoms",
        "result_treatment": "Recommended Treatment (Chemical/Fungicidal)",
        "result_organic": "Organic & Natural Control",
        "result_prevention": "Preventive Measures",
        "result_alternative_crops": "Other Viable Crops",
        
        # Dashboard
        "stat_total_predictions": "Total Predictions",
        "stat_crop_count": "Crop Recommendations",
        "stat_disease_count": "Disease Diagnoses",
        "recent_crops_title": "Recent Crop Recommendations",
        "recent_diseases_title": "Recent Disease Detections",
        "no_crops_yet": "No crop predictions yet. Run your first recommendation!",
        "no_diseases_yet": "No disease scans yet. Upload a leaf photo to diagnose!",
        "table_date": "Date & Time",
        "table_crop": "Crop",
        "table_confidence": "Confidence",
        "table_disease": "Disease",
        "table_image": "Leaf Image",
        "table_solution": "Action / Remedy",
        
        # History
        "history_title": "Prediction History",
        "history_crop_tab": "Crop Recommendations",
        "history_disease_tab": "Leaf Disease Scans",
        
        # Auth
        "auth_username": "Username",
        "auth_email": "Email Address",
        "auth_password": "Password",
        "auth_confirm_password": "Confirm Password",
        "auth_no_account": "Don't have an account?",
        "auth_have_account": "Already have an account?",
        "auth_login_prompt": "Sign in to access your agricultural dashboard",
        "auth_register_prompt": "Join AgriAI for AI-assisted smart farming",
        
        # Audio
        "audio_playing": "Playing audio...",
        "audio_stopped": "Audio stopped.",
        "audio_not_supported": "Speech synthesis is not supported on this browser.",
        
        # Messages & Errors
        "err_invalid_file": "Please upload a valid image file (PNG, JPG, JPEG, WEBP).",
        "err_too_large": "File size exceeds the 5MB limit. Please upload a smaller image.",
        "err_prediction_failed": "Prediction failed. Please ensure the image is clear and try again.",
        "err_input_missing": "Please fill out all required soil and weather parameters.",

        # Index page – feature cards & metrics
        "badge_crops_supported": "22 Crops Supported",
        "badge_disease_classes": "29 Disease Classes",
        "crop_card_desc": "Trained on verified soil and climatic parameters. Enter your Nitrogen, Phosphorus, Potassium levels, along with temperature, humidity, pH, and precipitation to receive the optimal crop choice with genuine model probability.",
        "disease_card_desc": "Leveraging a MobileNetV2 convolutional neural network. Simply snap or drag-and-drop a leaf photograph to instantly diagnose disease pathology, biological causes, symptoms, and organic & chemical treatments.",
        "badge_npk": "🧪 N-P-K Analysis",
        "badge_weather": "🌦️ Weather Integration",
        "badge_rf": "🌲 Random Forest ML",
        "badge_voice": "🔊 Multi-Language Voice",
        "badge_upload": "📸 Drag & Drop Upload",
        "badge_ai": "⚡ Instant AI Inference",
        "badge_organic": "🌿 Organic & Chemical Control",
        "badge_audio_lang": "🔊 EN / हिंदी / తెలుగు Audio",
        "metric_crop_varieties": "Crop Varieties Evaluated",
        "metric_diseases": "Plant & Leaf Diseases",
        "metric_accuracy": "Crop Model Benchmark Accuracy",
        "metric_languages": "Languages (EN / HI / TE)",

        # Crop page
        "crop_subtitle": "Provide your soil test results and local meteorological data.",
        "badge_rf_model": "Random Forest (100 Trees)",
        "quick_presets": "⚡ Quick Presets:",
        "preset_rice": "🌾 Rice",
        "preset_maize": "🌽 Maize",
        "preset_chickpea": "🧆 Chickpea",
        "preset_cotton": "👕 Cotton",
        "preset_coffee": "☕ Coffee",
        "preset_apple": "🍎 Apple",
        "section_soil_nutrients": "🧪 Soil Macronutrients (kg/ha)",
        "section_weather_soil": "🌦️ Weather & Soil Conditions",
        "badge_ai_recommendation": "✓ AI Recommendation",
        "label_model_output": "Model Output:",
        "label_opt_temperature": "🌡️ Optimal Temperature",
        "label_opt_humidity": "💧 Optimal Humidity",
        "label_ideal_ph": "🧪 Ideal Soil pH",
        "label_annual_rainfall": "🌧️ Annual Rainfall",

        # Disease page
        "disease_subtitle": "Upload a clear leaf photo for deep-learning plant disease diagnosis.",
        "badge_mobilenet": "MobileNetV2 Deep Learning",
        "btn_browse": "📁 Browse Device Photo",
        "engine_select_label": "🧠 Select AI Diagnosis Model Engine",
        "engine_select_hint": "Choose between AgriAI MobileNetV2 (29 classes, fast) or Crop-Disease-Detection CNN (38 classes, extended).",
        "alt_diagnoses_label": "Alternative Diagnostic Possibilities:",
        "label_model_tag": "Model Tag:",
        "label_plant": "Plant:",

        # Dashboard
        "dashboard_subtitle": "Here is your agricultural AI diagnostic and recommendation summary.",

        # History page
        "history_subtitle": "Complete historical logs of your crop recommendations and leaf disease diagnoses.",
        "table_n": "N",
        "table_p": "P",
        "table_k": "K",
        "table_temp": "Temp (°C)",
        "table_humidity_col": "Humidity (%)",
        "table_ph": "pH",
        "table_rain": "Rain (mm)",
        "table_audio": "Audio",

        # Footer
        "footer_tech": "Powered by MobileNetV2 Deep Learning & Random Forest Classifier | Flask • MongoDB • Scikit-learn"
    },
    
    "hi": {
        "app_name": "एग्री-एआई (AgriAI)",
        "tagline": "एआई-संचालित कृषि मंच",
        "hero_title": "एआई की सटीकता के साथ स्मार्ट खेती",
        "hero_desc": "मिट्टी और मौसम के अनुसार सर्वोत्तम फसल सुझाव और पत्तियों की फोटो से तुरंत रोग पहचान द्वारा किसानों को सशक्त बनाना।",
        "nav_home": "होम",
        "nav_dashboard": "डैशबोर्ड",
        "nav_crop": "फसल अनुशंसा",
        "nav_disease": "रोग पहचान",
        "nav_history": "इतिहास",
        "nav_login": "लॉग इन",
        "nav_register": "रजिस्टर",
        "nav_logout": "लॉग आउट",
        "welcome": "नमस्ते",
        
        # Actions
        "btn_login": "लॉग इन करें",
        "btn_register": "नया खाता बनाएं",
        "btn_predict_crop": "सर्वोत्तम फसल जानें",
        "btn_predict_disease": "पत्ती रोग की जांच करें",
        "btn_reset": "रीसेट करें",
        "btn_clear": "फोटो हटाएं",
        "btn_listen": "ऑडियो सुनें",
        "btn_stop": "ऑडियो रोकें",
        "btn_replay": "पुनः सुनें",
        "btn_explore": "शुरू करें",
        "btn_view_history": "पूरा इतिहास देखें",
        
        # Form fields
        "nitrogen_label": "नाइट्रोजन (N)",
        "nitrogen_desc": "मिट्टी में नाइट्रोजन स्तर (0 - 140 किग्रा/हेक्टेयर)",
        "phosphorus_label": "फास्फोरस (P)",
        "phosphorus_desc": "मिट्टी में फास्फोरस स्तर (5 - 145 किग्रा/हेक्टेयर)",
        "potassium_label": "पोटेशियम (K)",
        "potassium_desc": "मिट्टी में पोटेशियम स्तर (5 - 205 किग्रा/हेक्टेयर)",
        "temperature_label": "तापमान (°C)",
        "temperature_desc": "औसत वायु तापमान (8 - 44 °C)",
        "humidity_label": "सापेक्ष आर्द्रता (%)",
        "humidity_desc": "हवा में नमी (14 - 100%)",
        "ph_label": "मिट्टी का पीएच (pH)",
        "ph_desc": "अम्लता / क्षारीयता (3.5 - 10.0)",
        "rainfall_label": "वर्षा (मिमी)",
        "rainfall_desc": "वार्षिक वर्षा (20 - 300 मिमी)",
        
        # Upload
        "drag_drop_title": "पत्ती की फोटो यहाँ खींचें और छोड़ें",
        "drag_drop_desc": "या डिवाइस से चुनने के लिए क्लिक करें (JPG, PNG, WEBP अधिकतम 5MB)",
        "analyzing_title": "डीप लर्निंग द्वारा पत्ती का विश्लेषण हो रहा है...",
        "analyzing_desc": "सटीक रोग पहचान के लिए न्यूरल नेटवर्क मॉडल चल रहा है",
        
        # Results
        "result_recommended_crop": "अनुशंसित फसल",
        "result_confidence": "मॉडल सटीकता / आत्मविश्वास",
        "result_growing_conditions": "अनुकूल विकास स्थितियां",
        "result_season": "सर्वोत्तम बुवाई का मौसम",
        "result_soil": "उपयुक्त मिट्टी",
        "result_care": "कृषि व देखभाल मार्गदर्शिका",
        "result_leaf_status": "पौधे का स्वास्थ्य स्तर",
        "result_status_healthy": "स्वस्थ पौधा (कोई रोग नहीं)",
        "result_status_diseased": "रोग का पता चला (उपचार आवश्यक)",
        "result_disease_detected": "पहचाना गया रोग",
        "result_cause": "रोग का कारण",
        "result_symptoms": "दिखने वाले लक्षण",
        "result_treatment": "अनुशंसित रासायनिक उपचार",
        "result_organic": "जैविक एवं प्राकृतिक उपचार",
        "result_prevention": "बचाव के उपाय",
        "result_alternative_crops": "अन्य उपयुक्त फसलें",
        
        # Dashboard
        "stat_total_predictions": "कुल भविष्यवाणियां",
        "stat_crop_count": "फसल सिफारिशें",
        "stat_disease_count": "रोग निदान",
        "recent_crops_title": "हालिया फसल सिफारिशें",
        "recent_diseases_title": "हालिया रोग निदान",
        "no_crops_yet": "अभी तक कोई फसल सिफारिश नहीं है। अपनी पहली सिफारिश प्राप्त करें!",
        "no_diseases_yet": "अभी तक कोई रोग स्कैन नहीं है। जांच के लिए पत्ती की फोटो अपलोड करें!",
        "table_date": "तारीख और समय",
        "table_crop": "फसल",
        "table_confidence": "सटीकता",
        "table_disease": "रोग",
        "table_image": "पत्ती की फोटो",
        "table_solution": "उपचार / समाधान",
        
        # History
        "history_title": "पूर्वानुमान इतिहास",
        "history_crop_tab": "फसल सिफारिशें",
        "history_disease_tab": "पत्ती रोग स्कैन",
        
        # Auth
        "auth_username": "उपयोगकर्ता नाम",
        "auth_email": "ईमेल पता",
        "auth_password": "पासवर्ड",
        "auth_confirm_password": "पासवर्ड की पुष्टि करें",
        "auth_no_account": "खाता नहीं है?",
        "auth_have_account": "पहले से खाता है?",
        "auth_login_prompt": "अपने कृषि डैशबोर्ड में प्रवेश करें",
        "auth_register_prompt": "स्मार्ट खेती के लिए एग्री-एआई से जुड़ें",
        
        # Audio
        "audio_playing": "ऑडियो चल रहा है...",
        "audio_stopped": "ऑडियो रोक दिया गया।",
        "audio_not_supported": "इस ब्राउज़र में स्पीच सिंथेसिस समर्थित नहीं है।",
        
        # Messages & Errors
        "err_invalid_file": "कृपया एक मान्य छवि फ़ाइल (PNG, JPG, JPEG, WEBP) अपलोड करें।",
        "err_too_large": "फ़ाइल का आकार 5MB की सीमा से अधिक है। कृपया छोटी फ़ाइल चुनें।",
        "err_prediction_failed": "भविष्यवाणी विफल रही। कृपया साफ छवि अपलोड करें और पुनः प्रयास करें।",
        "err_input_missing": "कृपया मिट्टी और मौसम के सभी आवश्यक पैरामीटर भरें।",

        # Index page – feature cards & metrics
        "badge_crops_supported": "22 फसलें समर्थित",
        "badge_disease_classes": "29 रोग श्रेणियाँ",
        "crop_card_desc": "सत्यापित मिट्टी और जलवायु मापदंडों पर प्रशिक्षित। नाइट्रोजन, फास्फोरस, पोटाशियम, तापमान, आर्द्रता, pH और वर्षा दर्ज करें और सटीक फसल अनुशंसा प्राप्त करें।",
        "disease_card_desc": "MobileNetV2 कन्वोल्यूशनल न्यूरल नेटवर्क का उपयोग करते हुए — पत्ती की फोटो खींचें या अपलोड करें और तुरंत रोग, कारण, लक्षण, और जैविक व रासायनिक उपचार जानें।",
        "badge_npk": "🧪 N-P-K विश्लेषण",
        "badge_weather": "🌦️ मौसम एकीकरण",
        "badge_rf": "🌲 रैंडम फॉरेस्ट ML",
        "badge_voice": "🔊 बहुभाषी वॉइस",
        "badge_upload": "📸 ड्रैग & ड्रॉप अपलोड",
        "badge_ai": "⚡ तत्काल AI अनुमान",
        "badge_organic": "🌿 जैविक व रासायनिक नियंत्रण",
        "badge_audio_lang": "🔊 अंग्रेज़ी / हिंदी / తెలుగు ऑडियो",
        "metric_crop_varieties": "फसल किस्में मूल्यांकित",
        "metric_diseases": "पौध व पत्ती रोग",
        "metric_accuracy": "फसल मॉडल बेंचमार्क सटीकता",
        "metric_languages": "भाषाएँ (अंग्रेज़ी / हिंदी / तेलुगु)",

        # Crop page
        "crop_subtitle": "अपनी मिट्टी जाँच रिपोर्ट और स्थानीय मौसम डेटा प्रदान करें।",
        "badge_rf_model": "रैंडम फॉरेस्ट (100 पेड़)",
        "quick_presets": "⚡ त्वरित प्रीसेट:",
        "preset_rice": "🌾 चावल",
        "preset_maize": "🌽 मक्का",
        "preset_chickpea": "🧆 चना",
        "preset_cotton": "👕 कपास",
        "preset_coffee": "☕ कॉफ़ी",
        "preset_apple": "🍎 सेब",
        "section_soil_nutrients": "🧪 मिट्टी के मुख्य पोषक तत्व (किग्रा/हेक्टेयर)",
        "section_weather_soil": "🌦️ मौसम एवं मिट्टी की स्थिति",
        "badge_ai_recommendation": "✓ AI अनुशंसा",
        "label_model_output": "मॉडल परिणाम:",
        "label_opt_temperature": "🌡️ अनुकूल तापमान",
        "label_opt_humidity": "💧 अनुकूल आर्द्रता",
        "label_ideal_ph": "🧪 आदर्श मिट्टी pH",
        "label_annual_rainfall": "🌧️ वार्षिक वर्षा",

        # Disease page
        "disease_subtitle": "गहरी-शिक्षण पौध रोग निदान के लिए स्पष्ट पत्ती फोटो अपलोड करें।",
        "badge_mobilenet": "MobileNetV2 डीप लर्निंग",
        "btn_browse": "📁 डिवाइस से फोटो चुनें",
        "engine_select_label": "🧠 AI निदान मॉडल इंजन चुनें",
        "engine_select_hint": "AgriAI MobileNetV2 (29 श्रेणियाँ, तेज़) या Crop-Disease-Detection CNN (38 श्रेणियाँ, विस्तारित) में से चुनें।",
        "alt_diagnoses_label": "वैकल्पिक निदान संभावनाएं:",
        "label_model_tag": "मॉडल टैग:",
        "label_plant": "पौधा:",

        # Dashboard
        "dashboard_subtitle": "यहाँ आपकी कृषि AI निदान और अनुशंसा का सारांश है।",

        # History page
        "history_subtitle": "आपकी फसल अनुशंसाओं और पत्ती रोग निदान का पूर्ण ऐतिहासिक लॉग।",
        "table_n": "नाइट्रोजन (N)",
        "table_p": "फास्फोरस (P)",
        "table_k": "पोटेशियम (K)",
        "table_temp": "तापमान (°C)",
        "table_humidity_col": "आर्द्रता (%)",
        "table_ph": "pH",
        "table_rain": "वर्षा (मिमी)",
        "table_audio": "ऑडियो",

        # Footer
        "footer_tech": "MobileNetV2 डीप लर्निंग और रैंडम फॉरेस्ट क्लासिफायर द्वारा संचालित | Flask • MongoDB • Scikit-learn"
    },
    
    "te": {
        "app_name": "అగ్రి-ఏఐ (AgriAI)",
        "tagline": "ఏఐ ఆధారిత వ్యవసాయ వేదిక",
        "hero_title": "ఏఐ ఖచ్చితత్వంతో ఆధునిక స్మార్ట్ వ్యవసాయం",
        "hero_desc": "నేల మరియు వాతావరణ పరిస్థితుల ఆధారంగా ఉత్తమ పంట సూచనలు మరియు ఆకుల ఫోటో ద్వారా తక్షణ తెగుళ్ల గుర్తింపుతో రైతులకు తోడ్పాటు.",
        "nav_home": "హోమ్",
        "nav_dashboard": "డ్యాష్‌బోర్డ్",
        "nav_crop": "పంట సిఫార్సు",
        "nav_disease": "తెగులు గుర్తింపు",
        "nav_history": "చరిత్ర",
        "nav_login": "లాగిన్",
        "nav_register": "నమోదు",
        "nav_logout": "లాగౌట్",
        "welcome": "స్వాగతం",
        
        # Actions
        "btn_login": "లాగిన్ అవ్వండి",
        "btn_register": "ఖాతా తెరవండి",
        "btn_predict_crop": "ఉత్తమ పంటను తెలుసుకోండి",
        "btn_predict_disease": "తెగులును గుర్తించండి",
        "btn_reset": "రీసెట్ చేయండి",
        "btn_clear": "ఫోటో తీసివేయండి",
        "btn_listen": "వినండి (ఆడియో)",
        "btn_stop": "ఆపండి",
        "btn_replay": "మళ్ళీ వినండి",
        "btn_explore": "ప్రారంభించండి",
        "btn_view_history": "పూర్తి చరిత్రను చూడండి",
        
        # Form fields
        "nitrogen_label": "నత్రజని (N)",
        "nitrogen_desc": "నేలలో నత్రజని పరిమాణం (0 - 140 కిలోలు/హెక్టారు)",
        "phosphorus_label": "భాస్వరం (P)",
        "phosphorus_desc": "నేలలో భాస్వరం పరిమాణం (5 - 145 కిలోలు/హెక్టారు)",
        "potassium_label": "పొటాషియం (K)",
        "potassium_desc": "నేలలో పొటాషియం పరిమాణం (5 - 205 కిలోలు/హెక్టారు)",
        "temperature_label": "ఉష్ణోగ్రత (°C)",
        "temperature_desc": "సగటు గాలి ఉష్ణోగ్రత (8 - 44 °C)",
        "humidity_label": "తేమ శాతం (%)",
        "humidity_desc": "గాలిలోని తేమ (14 - 100%)",
        "ph_label": "నేల పి.హెచ్ (pH)",
        "ph_desc": "ఆమ్లత్వం / క్షారత్వం (3.5 - 10.0)",
        "rainfall_label": "వర్షపాతం (మిమీ)",
        "rainfall_desc": "వార్షిక వర్షపాతం (20 - 300 మిమీ)",
        
        # Upload
        "drag_drop_title": "ఆకు ఫోటోను ఇక్కడ లాగి వదలండి",
        "drag_drop_desc": "లేదా ఫైల్ ఎంచుకోవడానికి క్లిక్ చేయండి (JPG, PNG, WEBP గరిష్టంగా 5MB)",
        "analyzing_title": "డీప్ లెర్నింగ్‌తో ఆకును విశ్లేషిస్తోంది...",
        "analyzing_desc": "తెగులు ఖచ్చితమైన గుర్తింపు కోసం న్యూరల్ నెట్‌వర్క్ నడుస్తోంది",
        
        # Results
        "result_recommended_crop": "సిఫార్సు చేయబడిన పంట",
        "result_confidence": "మోడల్ విశ్వసనీయత / ఖచ్చితత్వం",
        "result_growing_conditions": "అనుకూల సాగు పరిస్థితులు",
        "result_season": "అనువైన కాలం",
        "result_soil": "అనువైన నేల రకం",
        "result_care": "సాగు మరియు సంరక్షణ సూచనలు",
        "result_leaf_status": "మొక్క ఆరోగ్య స్థితి",
        "result_status_healthy": "ఆరోగ్యకరమైన మొక్క (తెగులు లేదు)",
        "result_status_diseased": "తెగులు గుర్తించబడింది (చికిత్స అవసరం)",
        "result_disease_detected": "గుర్తించిన తెగులు",
        "result_cause": "తెగులుకు కారణం",
        "result_symptoms": "కనిపించే లక్షణాలు",
        "result_treatment": "రసాయన నివారణ చర్యలు",
        "result_organic": "సేంద్రీయ మరియు సహజ నివారణ",
        "result_prevention": "ముందస్తు జాగ్రత్తలు",
        "result_alternative_crops": "ఇతర అనుకూలమైన పంటలు",
        
        # Dashboard
        "stat_total_predictions": "మొత్తం ఫలితాలు",
        "stat_crop_count": "పంట సిఫార్సులు",
        "stat_disease_count": "తెగుళ్ల నిర్ధారణలు",
        "recent_crops_title": "ఇటీవలి పంట సిఫార్సులు",
        "recent_diseases_title": "ఇటీవలి తెగులు నిర్ధారణలు",
        "no_crops_yet": "ఇంకా పంట ఫలితాలు లేవు. మీ మొదటి సిఫార్సును పొందండి!",
        "no_diseases_yet": "ఇంకా ఆకుల స్కాన్‌లు లేవు. తెగులును గుర్తించడానికి ఫోటో అప్‌లోడ్ చేయండి!",
        "table_date": "తేదీ మరియు సమయం",
        "table_crop": "పంట",
        "table_confidence": "విశ్వసనీయత",
        "table_disease": "తెగులు",
        "table_image": "ఆకు ఫోటో",
        "table_solution": "నివారణ / చర్య",
        
        # History
        "history_title": "గత రికార్డుల చరిత్ర",
        "history_crop_tab": "పంట సిఫార్సులు",
        "history_disease_tab": "తెగులు స్కాన్‌లు",
        
        # Auth
        "auth_username": "వినియోగదారు పేరు",
        "auth_email": "ఈమెయిల్ చిరునామా",
        "auth_password": "పాస్‌వర్డ్",
        "auth_confirm_password": "పాస్‌వర్డ్ నిర్ధారించండి",
        "auth_no_account": "ఖాతా లేదా?",
        "auth_have_account": "ఇప్పటికే ఖాతా ఉందా?",
        "auth_login_prompt": "మీ వ్యవసాయ డ్యాష్‌బోర్డ్‌లోకి లాగిన్ అవ్వండి",
        "auth_register_prompt": "స్మార్ట్ వ్యవసాయం కోసం అగ్రి-ఏఐలో చేరండి",
        
        # Audio
        "audio_playing": "ఆడియో వినిపిస్తోంది...",
        "audio_stopped": "ఆడియో ఆపబడింది.",
        "audio_not_supported": "ఈ బ్రౌజర్‌లో వాయిస్ సదుపాయం అందుబాటులో లేదు.",
        
        # Messages & Errors
        "err_invalid_file": "దయచేసి సరైన ఇమేజ్ ఫైల్‌ను (PNG, JPG, JPEG, WEBP) ఎంచుకోండి.",
        "err_too_large": "ఫైల్ పరిమాణం 5MB పరిమితిని మించింది. చిన్న ఫైల్‌ను ఎంచుకోండి.",
        "err_prediction_failed": "విశ్లేషణ విఫలమైంది. దయచేసి స్పష్టమైన చిత్రాన్ని అప్‌లోడ్ చేసి మళ్లీ ప్రయత్నించండి.",
        "err_input_missing": "దయచేసి అన్ని నేల మరియు వాతావరణ వివరాలను నమోదు చేయండి."
    }
}

# Crop Translations (All 22 crops)
CROPS_I18N = {
    "apple": {
        "en": {"name": "Apple", "season": "Spring planting, autumn harvest in temperate zones.", "soil": "Well-drained loamy soil (pH 6.0 - 7.0)", "care": "Prune annually for canopy ventilation, maintain balanced potassium, and monitor for scab."},
        "hi": {"name": "सेब (Apple)", "season": "शीतोष्ण क्षेत्रों में वसंत में बुवाई और शरद ऋतु में कटाई।", "soil": "अच्छी जल निकासी वाली दोमट मिट्टी (pH 6.0 - 7.0)", "care": "हवा के संचार के लिए वार्षिक छंटाई करें, संतुलित पोटाश दें और फफूंद पर नज़र रखें।"},
        "te": {"name": "ఆపిల్ (Apple)", "season": "శీతల ప్రాంతాలలో వసంతకాలంలో నాటడం, శరదృతువులో కోత.", "soil": "మంచి నీటి పారుదల గల నేలలు (pH 6.0 - 7.0)", "care": "గాలి ప్రసరణకు కత్తిరింపులు చేయాలి మరియు పోషకాలను సమతుల్యంగా అందించాలి."}
    },
    "banana": {
        "en": {"name": "Banana", "season": "Year-round in warm, humid tropical zones.", "soil": "Deep, fertile, well-draining organic loam (pH 5.5 - 7.0)", "care": "Requires heavy mulching, regular watering, and potassium-rich organic fertilizer."},
        "hi": {"name": "केला (Banana)", "season": "गर्म और आर्द्र उष्णकटिबंधीय क्षेत्रों में साल भर।", "soil": "गहरी, उपजाऊ और जीवांश युक्त दोमट मिट्टी (pH 5.5 - 7.0)", "care": "नियमित सिंचाई करें, जड़ों के पास मल्चिंग करें और पोटाश युक्त जैविक खाद दें।"},
        "te": {"name": "అరటి (Banana)", "season": "తేమతో కూడిన ఉష్ణమండల ప్రాంతాలలో ఏడాది పొడవునా సాగు చేయవచ్చు.", "soil": "సారవంతమైన సేంద్రీయ నేలలు (pH 5.5 - 7.0)", "care": "సమృద్ధిగా నీరు, మల్చింగ్ మరియు పొటాష్ ఎరువులు క్రమం తప్పకుండా వేయాలి."}
    },
    "blackgram": {
        "en": {"name": "Blackgram (Urad)", "season": "Kharif and summer pulse season.", "soil": "Well-drained loamy to heavy clay soil (pH 6.0 - 7.5)", "care": "Inoculate seeds with Rhizobium, ensure adequate moisture at flowering, avoid waterlogging."},
        "hi": {"name": "उड़द (Blackgram)", "season": "खरीफ और ग्रीष्मकालीन दाल का मौसम।", "soil": "अच्छी जल निकासी वाली दोमट या चिकनी मिट्टी (pH 6.0 - 7.5)", "care": "राइजोबियम से बीजोपचार करें, फूल आते समय नमी बनाए रखें, जलभराव से बचाएं।"},
        "te": {"name": "మినుములు (Blackgram)", "season": "ఖరీఫ్ మరియు వేసవి కాలం.", "soil": "నీరు నిలవని సారవంతమైన నేలలు (pH 6.0 - 7.5)", "care": "రైజోబియం విత్తన శుద్ధి చేయాలి, పూత దశలో తేమ ఉండేలా చూసుకోవాలి."}
    },
    "chickpea": {
        "en": {"name": "Chickpea (Gram)", "season": "Rabi (winter) season with cool, dry weather.", "soil": "Deep well-drained loam or silt loam (pH 6.0 - 7.5)", "care": "Requires minimal nitrogen due to nitrogen fixation; avoid excessive watering."},
        "hi": {"name": "चना (Chickpea)", "season": "रबी (सर्दियों) का मौसम, ठंडी और शुष्क जलवायु।", "soil": "गहरी अच्छी जल निकासी वाली दोमट मिट्टी (pH 6.0 - 7.5)", "care": "नाइट्रोजन स्थिरीकरण के कारण कम यूरिया दें; अधिक सिंचाई से जड़ गलन का खतरा रहता है।"},
        "te": {"name": "శనగలు (Chickpea)", "season": "రబీ (శీతాకాలం) అనువైనది.", "soil": "మంచి నీటి పారుదల గల నేలలు (pH 6.0 - 7.5)", "care": "అధిక నీటిని నివారించాలి, భాస్వరం ఎరువులను సరైన సమయంలో అందించాలి."}
    },
    "coconut": {
        "en": {"name": "Coconut", "season": "Tropical coastal areas, perennial year-round production.", "soil": "Sandy loam, alluvial or coastal red soils (pH 5.2 - 8.0)", "care": "Apply balanced NPK with magnesium and boron; maintain basin irrigation in summer."},
        "hi": {"name": "नारियल (Coconut)", "season": "तटीय उष्णकटिबंधीय क्षेत्रों में साल भर।", "soil": "बलुई दोमट या तटीय लाल मिट्टी (pH 5.2 - 8.0)", "care": "मैग्नीशियम और बोरॉन के साथ संतुलित खाद दें; गर्मियों में थाला सिंचाई करें।"},
        "te": {"name": "కొబ్బరి (Coconut)", "season": "తీర ప్రాంతాలలో ఏడాది పొడవునా సాగు చేయవచ్చు.", "soil": "ఇసుకతో కూడిన ఒండ్రు నేలలు (pH 5.2 - 8.0)", "care": "బోరాన్ మరియు సూక్ష్మ పోషకాలను క్రమం తప్పకుండా అందిస్తూ పాదులలో తేమ ఉంచాలి."}
    },
    "coffee": {
        "en": {"name": "Coffee", "season": "Rainy season planting under shade tree canopies.", "soil": "Porous, rich organic loam (pH 5.5 - 6.5)", "care": "Requires partial shade, leaf litter mulching, and pest management for coffee borer."},
        "hi": {"name": "कॉफ़ी (Coffee)", "season": "छायादार पेड़ों के नीचे वर्षा ऋतु में रोपण।", "soil": "उपजाऊ, जीवांश युक्त दोमट मिट्टी (pH 5.5 - 6.5)", "care": "आंशिक छाया आवश्यक है; पत्तियों की मल्चिंग करें और बोरर कीट पर नियंत्रण रखें।"},
        "te": {"name": "కాఫీ (Coffee)", "season": "నీడ చెట్ల కింద వర్షాకాలంలో నాటడం ఉత్తమం.", "soil": "సేంద్రీయ పోషకాలు సమృద్ధిగా ఉన్న నేలలు (pH 5.5 - 6.5)", "care": "పాక్షిక నీడ మరియు ఆకుల మల్చింగ్ ముఖ్యం; తెగుళ్ల నివారణ చేపట్టాలి."}
    },
    "cotton": {
        "en": {"name": "Cotton", "season": "Kharif season sown after early pre-monsoon rains.", "soil": "Deep black cotton soils (Vertisols) or alluvial loam (pH 6.0 - 7.5)", "care": "Monitor for bollworms and sucking pests, avoid water stagnation, split nitrogen doses."},
        "hi": {"name": "कपास (Cotton)", "season": "खरीफ मौसम, मानसून की पहली बारिश के बाद बुवाई।", "soil": "गहरी काली कपासी मिट्टी या दोमट मिट्टी (pH 6.0 - 7.5)", "care": "गुलाबी सुंडी और रस चूसक कीटों से रक्षा करें; जलभराव से बचें और यूरिया किस्तों में दें।"},
        "te": {"name": "పత్తి (Cotton)", "season": "ఖరీఫ్ కాలం, తొలకరి వర్షాల అనంతరం విత్తడం.", "soil": "లోతైన నల్లరేగడి నేలలు లేదా ఎర్ర నేలలు (pH 6.0 - 7.5)", "care": "రసం పీల్చే పురుగులు మరియు గులాబీ రంగు కాయ తొలిచే పురుగు నివారణ ముఖ్యం."}
    },
    "grapes": {
        "en": {"name": "Grapes", "season": "Subtropical dry climate with distinct winter pruning.", "soil": "Deep, well-drained sandy loam or gravely loam (pH 6.0 - 7.5)", "care": "Train on bower or trellis; practice regular canopy pruning and preventive sprays against downy mildew."},
        "hi": {"name": "अंगूर (Grapes)", "season": "शुष्क उपोष्णकटिबंधीय जलवायु, सर्दियों में विशेष छंटाई।", "soil": "गहरी अच्छी जल निकासी वाली बलुई दोमट मिट्टी (pH 6.0 - 7.5)", "care": "मंडप या ट्रेलिस पर बेल चढ़ाएं; नियमित छंटाई करें और डाउनी फफूंदी से बचाएं।"},
        "te": {"name": "ద్రాక్ష (Grapes)", "season": "శీతోష్ణ మరియు పొడి వాతావరణం అనుకూలం.", "soil": "మంచి నీటి పారుదల గల ఇసుక నేలలు (pH 6.0 - 7.5)", "care": "పందిరి విధానం మరియు సమయానుకూల కత్తిరింపులు దిగుబడిని పెంచుతాయి."}
    },
    "jute": {
        "en": {"name": "Jute", "season": "Pre-monsoon to monsoon warm, humid climate.", "soil": "Fertile alluvial floodplain soil (pH 6.0 - 7.2)", "care": "Maintain soil moisture in early stages; thin seedlings at 3 weeks; retting requires clean water."},
        "hi": {"name": "जूट / पटसन (Jute)", "season": "मानसून पूर्व से मानसूनी गर्म और आर्द्र जलवायु।", "soil": "उपजाऊ जलोढ़ कछारी मिट्टी (pH 6.0 - 7.2)", "care": "शुरुआती अवस्था में मिट्टी में नमी रखें; 3 सप्ताह बाद विरलीकरण करें; सड़ाने हेतु साफ पानी चाहिए।"},
        "te": {"name": "జనపనార (Jute)", "season": "వర్షాకాలంలో వేడి మరియు తేమ గల వాతావరణం.", "soil": "సారవంతమైన ఒండ్రు నేలలు (pH 6.0 - 7.2)", "care": "మొక్కల తొలి దశలో సరైన తేమ అందించాలి మరియు కలుపు నివారణ చేయాలి."}
    },
    "kidneybeans": {
        "en": {"name": "Kidney Beans (Rajma)", "season": "Kharif in hills; Rabi in northern plains.", "soil": "Light rich loam with excellent internal drainage (pH 5.5 - 6.5)", "care": "Sensitive to waterlogging and salinity; apply phosphorus at sowing for strong root nodules."},
        "hi": {"name": "राजमा (Kidney Beans)", "season": "पहाड़ों में खरीफ; उत्तरी मैदानी इलाकों में रबी।", "soil": "उत्कृष्ट जल निकास वाली हल्की उपजाऊ दोमट मिट्टी (pH 5.5 - 6.5)", "care": "जलभराव और खारेपन के प्रति संवेदनशील; जड़ों के विकास हेतु बुवाई के समय फास्फोरस दें।"},
        "te": {"name": "రాజ్మా (Kidney Beans)", "season": "శీతాకాలం లేదా కొండ ప్రాంతాలలో ఖరీఫ్.", "soil": "తేలికపాటి సారవంతమైన నేలలు (pH 5.5 - 6.5)", "care": "నీరు నిలబడకుండా చూడాలి; భాస్వరం ఎరువులను విత్తేటప్పుడే అందించాలి."}
    },
    "lentil": {
        "en": {"name": "Lentil (Masoor)", "season": "Rabi (winter) season pulse crop.", "soil": "Can grow on poor soils; prefers light loamy soil (pH 6.0 - 7.5)", "care": "Low water requirement; requires weed management during the first 45 days after germination."},
        "hi": {"name": "मसूर (Lentil)", "season": "रबी (सर्दियों) की दलहनी फसल।", "soil": "हल्की दोमट मिट्टी उपयुक्त; कम उपजाऊ मिट्टी में भी संभव (pH 6.0 - 7.5)", "care": "कम पानी की आवश्यकता; अंकुरण के पहले 45 दिनों में खरपतवार नियंत्रण अत्यंत आवश्यक है।"},
        "te": {"name": "ఎర్ర కందులు (Lentil)", "season": "రబీ కాలం అనుకూలం.", "soil": "తేలికపాటి గరప నేలలు (pH 6.0 - 7.5)", "care": "తక్కువ నీటితో పండుతుంది; మొదటి 45 రోజులలో కలుపు నివారించాలి."}
    },
    "maize": {
        "en": {"name": "Maize (Corn)", "season": "Kharif and Rabi seasons in warm conditions.", "soil": "Well-drained fertile loam rich in organic matter (pH 5.8 - 7.5)", "care": "Critical irrigation needed at tasseling and silking stages; manage fall armyworm early."},
        "hi": {"name": "मक्का (Maize / Corn)", "season": "खरीफ और रबी दोनों मौसमों में उपयुक्त।", "soil": "जीवांश से भरपूर अच्छी जल निकासी वाली दोमट मिट्टी (pH 5.8 - 7.5)", "care": "मंजरी और भुट्टा बनते समय सिंचाई आवश्यक है; फॉल आर्मीवर्म कीट से सुरक्षा करें।"},
        "te": {"name": "మొక్కజొన్న (Maize)", "season": "ఖరీఫ్ మరియు రబీ రెండు కాలాలలో సాగు చేయవచ్చు.", "soil": "సారవంతమైన ఒండ్రు నేలలు (pH 5.8 - 7.5)", "care": "పూత మరియు గింజ పాలు పోసుకునే దశలలో నీటి తడులు తప్పనిసరి; కత్తెర పురుగు నివారణ ముఖ్యం."}
    },
    "mango": {
        "en": {"name": "Mango", "season": "Tropical and subtropical climates; flowering in winter.", "soil": "Deep rich alluvial or red loamy soil (pH 5.5 - 7.5)", "care": "Stop irrigation prior to flowering; spray against powdery mildew and mango hoppers during flower set."},
        "hi": {"name": "आम (Mango)", "season": "उष्णकटिबंधीय जलवायु; सर्दियों में बौर (फूल) आते हैं।", "soil": "गहरी उपजाऊ जलोढ़ या लाल दोमट मिट्टी (pH 5.5 - 7.5)", "care": "फूल आने से पहले सिंचाई बंद करें; बौर आते समय मधुआ कीट और फफूंद से बचाव करें।"},
        "te": {"name": "మామిడి (Mango)", "season": "ఉష్ణ మరియు సమశీతోష్ణ వాతావరణం; శీతాకాలంలో పూత వస్తుంది.", "soil": "లోతైన సారవంతమైన ఎర్ర నేలలు (pH 5.5 - 7.5)", "care": "పూతకు ముందు నీటి తడులు ఆపాలి; తేనెమంచు పురుగు నివారణకు మందులు పిచికారీ చేయాలి."}
    },
    "mothbeans": {
        "en": {"name": "Mothbeans (Matki)", "season": "Kharif season; highly drought-resistant legume.", "soil": "Sandy or light loam suited for arid tracts (pH 6.5 - 8.0)", "care": "Minimal inputs needed; acts as an excellent soil conservation and nitrogen-enriching crop."},
        "hi": {"name": "मोठ (Mothbeans)", "season": "खरीफ मौसम; अत्यधिक सूखा सहनशील दलहनी फसल।", "soil": "शुष्क क्षेत्रों के लिए उपयुक्त रेतीली या हल्की दोमट (pH 6.5 - 8.0)", "care": "बहुत कम पानी व खाद की जरूरत; मिट्टी संरक्षण और नाइट्रोजन बढ़ाने में मददगार।"},
        "te": {"name": "బొబ్బర్లు / మోత్ బీన్స్", "season": "ఖరీఫ్ కాలం; కరువును తట్టుకునే పప్పుధాన్య పంట.", "soil": "ఇసుక లేదా తేలికపాటి నేలలు (pH 6.5 - 8.0)", "care": "తక్కువ పెట్టుబడితో సాగు చేయవచ్చు; నేల సారాన్ని పెంచుతుంది."}
    },
    "mungbean": {
        "en": {"name": "Mungbean (Green Gram)", "season": "Kharif, Rabi, and summer short-duration pulse.", "soil": "Well-drained loam or sandy loam (pH 6.2 - 7.2)", "care": "Matures in 60-70 days; protect from yellow mosaic virus via whitefly control."},
        "hi": {"name": "मूंग (Mungbean)", "season": "खरीफ, रबी और जायद (गर्मी) की अल्पकालिक फसल।", "soil": "अच्छी जल निकासी वाली दोमट मिट्टी (pH 6.2 - 7.2)", "care": "60-70 दिनों में पकती है; सफेद मक्खी नियंत्रित कर पीला मोज़ेक वायरस से बचाएं।"},
        "te": {"name": "పెసలు (Mungbean)", "season": "ఖరీఫ్, రబీ మరియు వేసవి స్వల్పకాలిక పంట.", "soil": "నీరు నిలవని సారవంతమైన నేలలు (pH 6.2 - 7.2)", "care": "తెల్లదోమ నివారణ ద్వారా పసుపు రంగు వైరస్ తెగులు రాకుండా చూసుకోవాలి."}
    },
    "muskmelon": {
        "en": {"name": "Muskmelon", "season": "Summer warm season with long sunny days.", "soil": "Sandy loam rich in organic matter (pH 6.0 - 7.5)", "care": "Irrigate regularly until fruit setting, then reduce watering to concentrate sweetness."},
        "hi": {"name": "खरबूजा (Muskmelon)", "season": "गर्मी (जायद) का मौसम, धूप भरे लंबे दिन।", "soil": "जीवांश से भरपूर बलुई दोमट मिट्टी (pH 6.0 - 7.5)", "care": "फल लगने तक नियमित पानी दें, फिर मिठास बढ़ाने के लिए सिंचाई कम कर दें।"},
        "te": {"name": "కర్బూజ (Muskmelon)", "season": "వేసవి కాలం అత్యంత అనుకూలం.", "soil": "సేంద్రీయ పదార్థాలు కలిగిన ఇసుక నేలలు (pH 6.0 - 7.5)", "care": "కాయలు ఏర్పడే వరకు తేమ ఉంచాలి, తరువాత తియ్యదనం పెరగడానికి నీరు తగ్గించాలి."}
    },
    "orange": {
        "en": {"name": "Orange (Citrus)", "season": "Subtropical climate with distinct dry and wet spells.", "soil": "Deep, well-aerated sandy loam with no hardpan (pH 6.0 - 7.5)", "care": "Avoid water contact with the tree trunk; apply zinc and iron micronutrients regularly."},
        "hi": {"name": "संतरा (Orange / Citrus)", "season": "उपोष्णकटिबंधीय जलवायु, संतुलित शुष्क और आर्द्र मौसम।", "soil": "गहरी और हवादार बलुई दोमट मिट्टी (pH 6.0 - 7.5)", "care": "पेड़ के तने के सीधे संपर्क में पानी न आने दें; जिंक और आयरन का छिड़काव करें।"},
        "te": {"name": "నారింజ / బత్తాయి (Orange)", "season": "సమశీతోష్ణ మరియు పొడి వాతావరణం.", "soil": "లోతైన గరప లేదా ఎర్ర నేలలు (pH 6.0 - 7.5)", "care": "మొక్క మొదళ్లకు నీరు తగలకుండా పాదులు చేయాలి; జింక్ మరియు ఐరన్ పోషకాలు ఇవ్వాలి."}
    },
    "papaya": {
        "en": {"name": "Papaya", "season": "Tropical frost-free climate, rapid 9-month harvest.", "soil": "Rich loam with superior drainage (pH 6.0 - 7.0)", "care": "Highly vulnerable to water stagnation and collar rot; construct raised beds."},
        "hi": {"name": "पपीता (Papaya)", "season": "उष्णकटिबंधीय पाला-मुक्त मौसम, 9 महीने में फल तैयार।", "soil": "बेहतर जल निकासी वाली उपजाऊ दोमट मिट्टी (pH 6.0 - 7.0)", "care": "जलभराव और तना गलन के प्रति अत्यधिक संवेदनशील; उठी हुई क्यारियों पर लगाएं।"},
        "te": {"name": "బొప్పాయి (Papaya)", "season": "వేడి వాతావరణం, 9-10 నెలల్లో దిగుబడి ప్రారంభం.", "soil": "మంచి నీటి పారుదల గల సారవంతమైన నేలలు (pH 6.0 - 7.0)", "care": "నీరు నిలిస్తే మొదలు కుళ్లు తెగులు వస్తుంది; ఎత్తైన బోదెలపై నాటాలి."}
    },
    "pigeonpeas": {
        "en": {"name": "Pigeonpeas (Arhar / Toor)", "season": "Kharif deep-rooted leguminous crop.", "soil": "Deep loamy or clayey loam with good aeration (pH 6.0 - 7.5)", "care": "Intercrop with cereals; ensure drainage; apply phosphorus fertilizer at sowing."},
        "hi": {"name": "अरहर / तुअर (Pigeonpeas)", "season": "खरीफ मौसम की गहरी जड़ों वाली दलहनी फसल।", "soil": "गहरी दोमट या चिकनी मिट्टी जिसमें हवा का संचार हो (pH 6.0 - 7.5)", "care": "अनाज फसलों के साथ अंतरफसल करें; जल निकास सुनिश्चित करें; बुवाई पर फास्फोरस दें।"},
        "te": {"name": "కందులు (Pigeonpeas / Toor)", "season": "ఖరీఫ్ కాలం, లోతైన వేరు వ్యవస్థ గల పంట.", "soil": "లోతైన సారవంతమైన నేలలు (pH 6.0 - 7.5)", "care": "అంతర పంటగా సాగు చేయవచ్చు; విత్తే సమయంలో భాస్వరం ఎరువులు తప్పనిసరి."}
    },
    "pomegranate": {
        "en": {"name": "Pomegranate", "season": "Semi-arid climate; regulated flowering (Bahar treatment).", "soil": "Light loamy to deep alluvial soils, tolerant of salinity (pH 6.5 - 8.0)", "care": "Prune suckers from base; spray against bacterial blight (Telya) and fruit borer."},
        "hi": {"name": "अनार (Pomegranate)", "season": "अर्ध-शुष्क जलवायु; बहार उपचार द्वारा पुष्पन नियंत्रण।", "soil": "हल्की दोमट से गहरी जलोढ़ मिट्टी, लवणता सहने में सक्षम (pH 6.5 - 8.0)", "care": "जड़ से निकलने वाली शाखाओं को छांटें; तेल्या (बैक्टीरियल ब्लाइट) से बचाव रखें।"},
        "te": {"name": "దానిమ్మ (Pomegranate)", "season": "పొడి మరియు సమశీతోష్ణ ప్రాంతాలు అనుకూలం.", "soil": "తేలికపాటి గరప నేలలు (pH 6.5 - 8.0)", "care": "చెట్టు మొదళ్లలో వచ్చే పిలకలను తొలగించాలి; తెగుళ్ల నివారణకు బోర్డో మిశ్రమం పిచికారీ చేయాలి."}
    },
    "rice": {
        "en": {"name": "Rice (Paddy)", "season": "Kharif monsoon season in warm, water-abundant plains.", "soil": "Clayey loam or alluvial soils capable of holding water (pH 5.5 - 7.0)", "care": "Maintain 2-5 cm standing water during vegetative stage; apply balanced NPK with zinc sulfate."},
        "hi": {"name": "धान / चावल (Paddy / Rice)", "season": "खरीफ मानसूनी मौसम, गर्म और प्रचुर पानी वाले क्षेत्र।", "soil": "चिकनी दोमट या जलोढ़ मिट्टी जो पानी रोक सके (pH 5.5 - 7.0)", "care": "विकास अवस्था में 2-5 सेमी पानी खड़ा रखें; जिंक सल्फेट के साथ संतुलित खाद दें।"},
        "te": {"name": "వరి (Paddy / Rice)", "season": "ఖరీఫ్ మరియు రబీ కాలాలు, సమృద్ధిగా నీరు అవసరం.", "soil": "బంకమన్ను లేదా ఒండ్రు నేలలు (pH 5.5 - 7.0)", "care": "దుబ్బు చేసే దశలో 2-5 సెం.మీ నీరు ఉంచాలి; జింక్ సల్ఫేట్ మరియు యూరియా సమతుల్యంగా వేయాలి."}
    },
    "watermelon": {
        "en": {"name": "Watermelon", "season": "Warm summer season with abundant sun exposure.", "soil": "Sandy loam rich in organic matter with excellent drainage (pH 6.0 - 7.0)", "care": "Mulch beds to conserve moisture and keep fruit clean; taper off watering near harvest."},
        "hi": {"name": "तरबूज (Watermelon)", "season": "गर्म ग्रीष्मकालीन मौसम, प्रचुर धूप की जरूरत।", "soil": "जीवांश युक्त बलुई दोमट मिट्टी, उत्तम जल निकास (pH 6.0 - 7.0)", "care": "नमी बचाने व फलों को साफ रखने के लिए मल्चिंग करें; कटाई से पूर्व सिंचाई कम करें।"},
        "te": {"name": "పుచ్చకాయ (Watermelon)", "season": "ఎండ ఎక్కువగా ఉండే వేసవి కాలం.", "soil": "ఇసుకతో కూడిన సారవంతమైన నేలలు (pH 6.0 - 7.0)", "care": "తేమ కోసం మల్చింగ్ షీట్లు వాడాలి; కోతకు వారం ముందు నీటి తడులు తగ్గించాలి."}
    }
}

# Disease Translations & Rich Pathology (All 29 Classes)
DISEASES_I18N = {
    "Apple - Apple Scab": {
        "en": {
            "name": "Apple - Apple Scab",
            "crop": "Apple",
            "status": "Diseased",
            "cause": "Fungal pathogen Venturia inaequalis. Thrives in cool (13-24°C), wet spring weather with prolonged leaf wetness.",
            "symptoms": "Olive-green to dark brown velvety circular spots on upper leaf surfaces, progressing to puckered leaves and scabby fruit lesions.",
            "treatment": "Apply protective fungicides such as Captan, Mancozeb, or Difenoconazole at green tip stage and repeated after rain events.",
            "organic": "Spray copper hydroxide, liquid sulfur, or neem oil; prune tree canopy to maximize rapid sun drying.",
            "prevention": "Rake and destroy fallen leaves in autumn to eliminate overwintering spores; plant scab-resistant varieties like Liberty or Honeycrisp."
        },
        "hi": {
            "name": "सेब - सेब स्कैब (Apple Scab)",
            "crop": "सेब",
            "status": "रोगग्रस्त",
            "cause": "फफूंद वेंचुरिया इनेक्वलिस (Venturia inaequalis)। ठंडे (13-24°C) और नम मौसम में तेजी से फैलता है।",
            "symptoms": "पत्तियों की ऊपरी सतह पर जैतून जैसे हरे से गहरे भूरे मखमली धब्बे, पत्तियां मुड़ना और फलों पर पपड़ीदार घाव।",
            "treatment": "हरी कली अवस्था में कैप्टन (Captan), मैंकोजेब (Mancozeb) या डाइफेनोकोनाज़ोल कवकनाशी का छिड़काव करें।",
            "organic": "कॉपर हाइड्रोक्साइड, सल्फर या नीम के तेल का छिड़काव करें; धूप और हवा के लिए पेड़ की छंटाई करें।",
            "prevention": "शरद ऋतु में गिरी हुई पत्तियों को इकट्ठा करके नष्ट कर दें; रोग प्रतिरोधी किस्मों की बुवाई करें।"
        },
        "te": {
            "name": "ఆపిల్ - ఆపిల్ స్కాబ్ (Apple Scab)",
            "crop": "ఆపిల్",
            "status": "తెగులు బారిన పడింది",
            "cause": "వెంచురియా ఇనాక్వాలిస్ అనే శిలీంధ్రం వల్ల వస్తుంది. చల్లని, తడి వాతావరణంలో వేగంగా వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై ముదురు ఆకుపచ్చ మరియు గోధుమ రంగు మచ్చలు ఏర్పడి ఆకులు రాలిపోతాయి, కాయలపై పొలుసులు వస్తాయి.",
            "treatment": "క్యాప్టన్ లేదా మాంకోజెబ్ శిలీంధ్ర నాశినిని వర్షాలకు ముందు పిచికారీ చేయాలి.",
            "organic": "కాపర్ హైడ్రాక్సైడ్ లేదా వేప నూనెను ఉపయోగించండి; చెట్లకు గాలి వెలుతురు తగిలేలా కత్తిరించండి.",
            "prevention": "రాలిన ఆకులను నాశనం చేయాలి; తెగులును తట్టుకునే రకాలను ఎంచుకోవాలి."
        }
    },
    "Apple - Black Rot": {
        "en": {
            "name": "Apple - Black Rot",
            "crop": "Apple",
            "status": "Diseased",
            "cause": "Fungus Botryosphaeria obtusa. Enters through bark wounds, dead twigs, and insect damage during warm wet conditions.",
            "symptoms": "Frogeye leaf spots with purple margins and tan centers; trunk cankers; fruit shows firm brown rot expanding in concentric rings.",
            "treatment": "Apply Captan or Thiophanate-methyl sprays from silver tip through petal fall.",
            "organic": "Carefully prune out and burn all dead cankered wood and mummified fruits; spray copper octanoate.",
            "prevention": "Keep trees vigorous with balanced fertilization; sanitize pruning shears between cuts."
        },
        "hi": {
            "name": "सेब - ब्लैक रॉट (Black Rot)",
            "crop": "सेब",
            "status": "रोगग्रस्त",
            "cause": "बोट्रियोस्फेरिया ओब्टुसा फफूंद। छाल के घावों और सूखे टहनियों के माध्यम से प्रवेश करती है।",
            "symptoms": "पत्तियों पर मेढ़क की आंख जैसे धब्बे (बैंगनी किनारे, भूरा केंद्र), तने पर घाव और फलों का काला पड़ना।",
            "treatment": "कैप्टन या थियोफैनेट-मिथाइल फफूंदनाशक का छिड़काव करें।",
            "organic": "संक्रमित टहनियों और सूखे फलों को काटकर जलाएं; कॉपर स्प्रे करें।",
            "prevention": "औजारों को विसंक्रमित रखें और पेड़ों को कीटों के घाव से बचाएं।"
        },
        "te": {
            "name": "ఆపిల్ - బ్లాక్ రాట్ (Black Rot)",
            "crop": "ఆపిల్",
            "status": "తెగులు బారిన పడింది",
            "cause": "బోట్రియోస్ఫేరియా ఒబ్టుసా శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై వలయాకార మచ్చలు, కొమ్మలపై పుండ్లు మరియు కాయలు నల్లగా కుళ్లిపోవడం.",
            "treatment": "క్యాప్టన్ లేదా థియోఫానేట్ మిథైల్ పిచికారీ చేయాలి.",
            "organic": "ఎండిన కొమ్మలను మరియు కుళ్ళిన పండ్లను కత్తిరించి కాల్చివేయాలి.",
            "prevention": "చెట్లను ఆరోగ్యంగా ఉంచాలి మరియు కత్తిరింపు పనిముట్లను శుభ్రపరచాలి."
        }
    },
    "Apple - Cedar Apple Rust": {
        "en": {
            "name": "Apple - Cedar Apple Rust",
            "crop": "Apple",
            "status": "Diseased",
            "cause": "Gymnosporangium juniperi-virginianae. Requires both Eastern red cedar / juniper and apple trees to complete its life cycle.",
            "symptoms": "Bright yellow-orange spots on the upper leaf surface, later developing tiny tube-like fungal projections on the underside.",
            "treatment": "Apply Myclobutanil or Chlorothalonil from cluster bud stage until petal fall.",
            "organic": "Apply sulfur or copper fungicides in early spring; remove nearby wild cedar/juniper galls within 500 meters.",
            "prevention": "Plant rust-immune cultivars (e.g., Redfree, Prima); eliminate volunteer junipers near orchards."
        },
        "hi": {
            "name": "सेब - सीडर रस्ट (Cedar Apple Rust)",
            "crop": "सेब",
            "status": "रोगग्रस्त",
            "cause": "जिम्नोस्पोरेंजियम फफूंद। इस फफूंद को अपना जीवन चक्र पूरा करने के लिए जुनिपर और सेब दोनों की जरूरत होती है।",
            "symptoms": "पत्तियों की ऊपरी सतह पर चमकीले पीले-नारंगी धब्बे और निचली सतह पर छोटे उभार।",
            "treatment": "माइक्लोबुटानिल (Myclobutanil) या क्लोरोथैलोनिल का छिड़काव करें।",
            "organic": "वसंत ऋतु में सल्फर का छिड़काव करें; बगीचे के पास से जुनिपर झाड़ियों को हटाएं।",
            "prevention": "प्रतिरोधी किस्मों का चयन करें और बगीचे के 500 मीटर के दायरे में जुनिपर न उगने दें।"
        },
        "te": {
            "name": "ఆపిల్ - సిడార్ ఆపిల్ రస్ట్ (Cedar Rust)",
            "crop": "ఆపిల్",
            "status": "తెగులు బారిన పడింది",
            "cause": "జిమ్నోస్పోరాంజియం శిలీంధ్రం వల్ల వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై ప్రకాశవంతమైన పసుపు-నారింజ రంగు మచ్చలు ఏర్పడతాయి.",
            "treatment": "మైక్లోబుటానిల్ మందును మొగ్గ దశలో పిచికారీ చేయాలి.",
            "organic": "సల్ఫర్ పిచికారీ చేయండి; తోట పరిసరాల్లో ఉండే జునిపర్ చెట్లను తొలగించండి.",
            "prevention": "తెగులు తట్టుకునే రకాలను నాటండి."
        }
    },
    "Apple - Healthy": {
        "en": {
            "name": "Apple - Healthy",
            "crop": "Apple",
            "status": "Healthy",
            "cause": "No pathogen detected. Foliage displays optimal chlorophyll density and cellular vigor.",
            "symptoms": "Clean, smooth, vibrant green leaves without spotting, wilting, or fungal lesions.",
            "treatment": "No chemical treatment required.",
            "organic": "Maintain balanced organic fertilization, preventive neem sprays, and consistent drip irrigation.",
            "prevention": "Regular orchard hygiene, balanced NPK nutrition, and routine scouting."
        },
        "hi": {
            "name": "सेब - स्वस्थ (Healthy Apple)",
            "crop": "सेब",
            "status": "स्वस्थ",
            "cause": "कोई रोग या रोगाणु नहीं पाया गया। पत्तियां पूरी तरह स्वस्थ और मजबूत हैं।",
            "symptoms": "साफ, चमकदार हरी पत्तियां बिना किसी धब्बे या सिकुड़न के।",
            "treatment": "किसी भी रासायनिक उपचार की आवश्यकता नहीं है।",
            "organic": "नियमित जैविक खाद दें और कीटों से सुरक्षा हेतु नीम के तेल का छिड़काव रखें।",
            "prevention": "उचित जल निकासी, संतुलित खाद और बगीचे की नियमित सफाई बनाए रखें।"
        },
        "te": {
            "name": "ఆపిల్ - ఆరోగ్యకరమైనది (Healthy Apple)",
            "crop": "ఆపిల్",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదా వ్యాధి కారకాలు లేవు.",
            "symptoms": "ఆకులు ఎటువంటి మచ్చలు లేకుండా పచ్చగా, కాంతివంతంగా ఉన్నాయి.",
            "treatment": "ఎటువంటి మందులు అవసరం లేదు.",
            "organic": "సమతుల్య ఎరువులు మరియు వేప కషాయం పిచికారీతో మొక్కను కాపాడుకోండి.",
            "prevention": "సరిపడా నీరు మరియు పోషకాలను క్రమం తప్పకుండా అందించండి."
        }
    },
    "Bell Pepper - Bacterial Spot": {
        "en": {
            "name": "Bell Pepper - Bacterial Spot",
            "crop": "Bell Pepper",
            "status": "Diseased",
            "cause": "Bacterium Xanthomonas campestris pv. vesicatoria. Spread via splashing rain, contaminated seeds, and handling wet plants.",
            "symptoms": "Small, water-soaked, dark brown blistering spots on leaves and fruit, causing severe defoliation and sunscald.",
            "treatment": "Apply fixed copper bactericides mixed with Mancozeb to enhance bacterial inhibition.",
            "organic": "Spray copper sulfate or Bacillus subtilis bio-formulations; remove diseased plants immediately.",
            "prevention": "Use hot water-treated certified disease-free seed; avoid overhead sprinkler irrigation; practice 3-year crop rotation."
        },
        "hi": {
            "name": "शिमला मिर्च - जीवाणु धब्बा (Bacterial Spot)",
            "crop": "शिमला मिर्च",
            "status": "रोगग्रस्त",
            "cause": "जैंथोमोनास बैक्टीरिया। बारिश की बूंदों और संक्रमित बीजों द्वारा फैलता है।",
            "symptoms": "पत्तियों और फलों पर गहरे भूरे रंग के पानीदार उभरे हुए धब्बे, पत्तियां गिरना।",
            "treatment": "कॉपर ऑक्सीक्लोराइड और मैंकोजेब के मिश्रण का छिड़काव करें।",
            "organic": "बेसिलस सबटिलिस (Bacillus subtilis) या कॉपर सल्फेट का छिड़काव करें; संक्रमित पौधे हटाएं।",
            "prevention": "प्रमाणित बीजों का प्रयोग करें; ड्रिप सिंचाई अपनाएं और 3 साल का फसल चक्र रखें।"
        },
        "te": {
            "name": "బెల్ పెప్పర్ - బాక్టీరియల్ స్పాట్",
            "crop": "బెల్ పెప్పర్",
            "status": "తెగులు బారిన పడింది",
            "cause": "జాంతోమోనాస్ బాక్టీరియా వల్ల వ్యాపిస్తుంది. వర్షపు తుంపర్ల ద్వారా వ్యాప్తి చెందుతుంది.",
            "symptoms": "ఆకులపై చిన్న చిన్న ముదురు గోధుమ రంగు నీటి మచ్చలు ఏర్పడతాయి.",
            "treatment": "కాపర్ ఆక్సిక్లోరైడ్ మరియు మాంకోజెబ్ కలిపి పిచికారీ చేయాలి.",
            "organic": "బాసిల్లస్ సబ్టిలిస్ జీవ నియంత్రణ మందులు వాడాలి; రాలిన ఆకులను తీసివేయాలి.",
            "prevention": "శుద్ధి చేసిన విత్తనాలు వాడాలి; పైనుంచి నీరు చల్లే పద్ధతిని నివారించాలి."
        }
    },
    "Bell Pepper - Healthy": {
        "en": {
            "name": "Bell Pepper - Healthy",
            "crop": "Bell Pepper",
            "status": "Healthy",
            "cause": "No pathogen detected. Vigorous vegetative structure with balanced nutrition.",
            "symptoms": "Uniform deep green leaves, firm stems, and normal blossom development.",
            "treatment": "No treatment required.",
            "organic": "Maintain mulch cover, foliar seaweed extract sprays, and consistent soil moisture.",
            "prevention": "Monitor for aphids and mites; provide calcium to prevent blossom end rot."
        },
        "hi": {
            "name": "शिमला मिर्च - स्वस्थ (Healthy Bell Pepper)",
            "crop": "शिमला मिर्च",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं। पौधा स्वस्थ और पूर्ण विकसित है।",
            "symptoms": "गहरे हरे रंग की पत्तियां, मजबूत तना और स्वस्थ फूल।",
            "treatment": "किसी दवा की आवश्यकता नहीं है।",
            "organic": "नियमित जैविक खाद और समुद्री शैवाल (सीवीड) अर्क का छिड़काव करें।",
            "prevention": "कैल्शियम की कमी न होने दें और माहू (एफिड्स) पर नजर रखें।"
        },
        "te": {
            "name": "బెల్ పెప్పర్ - ఆరోగ్యకరమైనది",
            "crop": "బెల్ పెప్పర్",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదు. మొక్క పచ్చగా బలంగా ఉంది.",
            "symptoms": "ముదురు ఆకుపచ్చ రంగు ఆకులు మరియు ఆరోగ్యకరమైన పూత.",
            "treatment": "మందుల పిచికారీ అవసరం లేదు.",
            "organic": "సేంద్రీయ ఎరువులు మరియు క్రమబద్ధమైన నీటి యాజమాన్యం చేపట్టాలి.",
            "prevention": "రసం పీల్చే పురుగుల బారిన పడకుండా పసుపు జిగురు బోర్డులను వాడాలి."
        }
    },
    "Cherry - Healthy": {
        "en": {
            "name": "Cherry - Healthy",
            "crop": "Cherry",
            "status": "Healthy",
            "cause": "No pathogen detected. Healthy canopy with robust vascular activity.",
            "symptoms": "Glossy green leaves free of shot holes, powdery mildew, or yellowing.",
            "treatment": "No treatment required.",
            "organic": "Compost mulch, beneficial insect companion plants, and routine horticultural oils.",
            "prevention": "Ensure good air circulation through summer pruning; avoid trunk water splashing."
        },
        "hi": {
            "name": "चेरी - स्वस्थ (Healthy Cherry)",
            "crop": "चेरी",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं पाया गया। पत्तियां स्वस्थ और चमकदार हैं।",
            "symptoms": "चमकदार हरी पत्तियां बिना किसी छेद या धब्बे के।",
            "treatment": "उपचार की आवश्यकता नहीं है।",
            "organic": "कम्पोस्ट खाद दें और मित्र कीटों को बढ़ावा दें।",
            "prevention": "गर्मियों में हल्की छंटाई कर हवा का संचार बनाए रखें।"
        },
        "te": {
            "name": "చెర్రీ - ఆరోగ్యకరమైనది",
            "crop": "చెర్రీ",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "మొక్క ఆరోగ్యంగా ఉంది.",
            "symptoms": "ఆకులు ఎటువంటి మచ్చలు లేకుండా మెరుస్తూ ఉన్నాయి.",
            "treatment": "మందులు అవసరం లేదు.",
            "organic": "సహజ ఎరువులను వాడండి.",
            "prevention": "సూర్యరశ్మి మరియు గాలి తగిలేలా కొమ్మలను ఉంచాలి."
        }
    },
    "Cherry - Powdery Mildew": {
        "en": {
            "name": "Cherry - Powdery Mildew",
            "crop": "Cherry",
            "status": "Diseased",
            "cause": "Fungus Podosphaera clandestina. Favored by warm days, cool humid nights, and lush shade.",
            "symptoms": "White talcum powder-like fungal patches on young leaves and fruit stems, leading to curling and crinkling.",
            "treatment": "Apply myclobutanil, trifloxystrobin, or propiconazole at shuck fall stage.",
            "organic": "Spray potassium bicarbonate (3g/L), wettable sulfur, or 10% milk-water solution in sunlight.",
            "prevention": "Prune interior canopy for sunlight penetration; avoid excessive nitrogen fertilizer that spurs overly tender growth."
        },
        "hi": {
            "name": "चेरी - चूर्णिल आसिता (Powdery Mildew)",
            "crop": "चेरी",
            "status": "रोगग्रस्त",
            "cause": "पोडोस्फेरा कवक (Podosphaera)। गर्म दिन, ठंडी रातें और नमी इसके लिए अनुकूल हैं।",
            "symptoms": "पत्तियों और डंठल पर सफेद पाउडर जैसा लेप, पत्तियों का मुड़ना और सूखना।",
            "treatment": "माइक्लोबुटानिल या प्रोपिकोनाज़ोल का छिड़काव करें।",
            "organic": "पोटेशियम बाइकार्बोनेट या घुलनशील गंधक (सल्फर) का छिड़काव करें।",
            "prevention": "अत्यधिक यूरिया न दें और पेड़ के बीच से टहनियों की छंटाई करें ताकि धूप पहुंच सके।"
        },
        "te": {
            "name": "చెర్రీ - బూడిద తెగులు (Powdery Mildew)",
            "crop": "చెర్రీ",
            "status": "తెగులు బారిన పడింది",
            "cause": "పోడోస్ఫేరా శిలీంధ్రం వల్ల వస్తుంది. రాత్రి వేళల్లో తేమ ఉన్నప్పుడు వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై తెల్లటి బూడిద వంటి పొర ఏర్పడి ఆకులు ముడుచుకుపోతాయి.",
            "treatment": "మైక్లోబుటానిల్ లేదా ప్రొపికోనజోల్ పిచికారీ చేయాలి.",
            "organic": "పొటాషియం బైకార్బోనేట్ లేదా గంధకం పొడిని పిచికారీ చేయాలి.",
            "prevention": "సూర్యకాంతి సరిగ్గా తగిలేలా కొమ్మలను పలుచగా చేయాలి."
        }
    },
    "Corn (Maize) - Cercospora Leaf Spot": {
        "en": {
            "name": "Corn (Maize) - Cercospora Leaf Spot (Gray Leaf Spot)",
            "crop": "Maize",
            "status": "Diseased",
            "cause": "Fungus Cercospora zeae-maydis. Prospers in humid weather (>90% RH) with warm temperatures (25-30°C).",
            "symptoms": "Rectangular, tan-to-gray lesions restricted by leaf veins, expanding parallel along leaf length.",
            "treatment": "Foliar fungicide application with Pyraclostrobin, Azoxystrobin, or Propiconazole at tasseling stage.",
            "organic": "Rotate with non-host crops like legumes; spray bio-fungicide Trichoderma viride.",
            "prevention": "Till under infected crop residue to accelerate fungal decomposition; choose resistant corn hybrids."
        },
        "hi": {
            "name": "मक्का - सर्कोस्पोरा पत्ती धब्बा (Gray Leaf Spot)",
            "crop": "मक्का",
            "status": "रोगग्रस्त",
            "cause": "सर्कोस्पोरा फफूंद। उच्च नमी और 25-30°C तापमान में तेजी से फैलता है।",
            "symptoms": "नसों के बीच आयताकार, भूरे-धूसर रंग के धब्बे जो पत्ती की लंबाई में समानांतर फैलते हैं।",
            "treatment": "एज़ोक्सीस्ट्रोबिन या प्रोपिकोनाज़ोल फफूंदनाशक का छिड़काव करें।",
            "organic": "ट्राइकोडर्मा विरिडी जैव कवकनाशी का प्रयोग करें; दलहनी फसलों के साथ फसल चक्र अपनाएं।",
            "prevention": "फसल के अवशेषों को जुताई कर मिट्टी में दबा दें और रोग-प्रतिरोधी संकर बीज बोएं।"
        },
        "te": {
            "name": "మొక్కజొన్న - సెర్కోస్పోరా ఆకుమచ్చ తెగులు",
            "crop": "మొక్కజొన్న",
            "status": "తెగులు బారిన పడింది",
            "cause": "సెర్కోస్పోరా జియే-మేడిస్ శిలీంధ్రం వల్ల వస్తుంది. అధిక తేమ దీనికి అనుకూలం.",
            "symptoms": "ఆకు ఈనెల మధ్య దీర్ఘచతురస్రాకార బూడిద రంగు మచ్చలు ఏర్పడతాయి.",
            "treatment": "అజాక్సిస్ట్రోబిన్ లేదా ప్రొపికోనజోల్ మందును పిచికారీ చేయాలి.",
            "organic": "ట్రైకోడెర్మా విరిడి వంటి జీవ శిలీంధ్ర నాశినులను వాడాలి.",
            "prevention": "పంట మార్పిడి పాటించాలి; తెగులును తట్టుకునే విత్తనాలను నాటాలి."
        }
    },
    "Corn (Maize) - Common Rust": {
        "en": {
            "name": "Corn (Maize) - Common Rust",
            "crop": "Maize",
            "status": "Diseased",
            "cause": "Fungus Puccinia sorghi. Airborne urediniospores spread over vast distances in moderate temps (16-25°C).",
            "symptoms": "Golden-brown to cinnamon-colored powdery pustules scattered on both upper and lower leaf surfaces.",
            "treatment": "Apply Mancozeb, Azoxystrobin, or Tebuconazole if rust appears prior to tasseling stage.",
            "organic": "Foliar spray with neem cake extract or sulfur dust; encourage biocontrol with Bacillus subtilis.",
            "prevention": "Plant rust-resistant hybrids bearing the Rp gene; early season planting."
        },
        "hi": {
            "name": "मक्का - सामान्य रतुआ / रस्ट (Common Rust)",
            "crop": "मक्का",
            "status": "रोगग्रस्त",
            "cause": "पक्सीनिया सोरघाई फफूंद (Puccinia sorghi)। हवा द्वारा इसके बीजाणु दूर-दूर तक फैलते हैं।",
            "symptoms": "पत्ती की दोनों सतहों पर दालचीनी जैसे भूरे-सुनहरे रंग के उभरे हुए पाउडर वाले दाने।",
            "treatment": "टैबुकोनाज़ोल या मैंकोजेब कवकनाशी का छिड़काव करें।",
            "organic": "नीम की खली का अर्क या सल्फर का बुरकाव करें।",
            "prevention": "Rp जीन युक्त रतुआ-प्रतिरोधी संकर किस्में लगाएं; समय पर बुवाई करें।"
        },
        "te": {
            "name": "మొక్కజొన్న - కుంకుమ తెగులు (Common Rust)",
            "crop": "మొక్కజొన్న",
            "status": "తెగులు బారిన పడింది",
            "cause": "పక్సీనియా సోర్గి శిలీంధ్రం వల్ల గాలి ద్వారా వ్యాపిస్తుంది.",
            "symptoms": "ఆకుల రెండు వైపులా ఇటుక రంగు లేదా గోధుమ రంగు పొక్కులు ఏర్పడతాయి.",
            "treatment": "టెబుకొనజోల్ లేదా మాంకోజెబ్ పిచికారీ చేయాలి.",
            "organic": "వేప కషాయం లేదా గంధకం పొడిని వాడాలి.",
            "prevention": "తెగులును తట్టుకునే రకాలను ఎంచుకోవాలి."
        }
    },
    "Corn (Maize) - Healthy": {
        "en": {
            "name": "Corn (Maize) - Healthy",
            "crop": "Maize",
            "status": "Healthy",
            "cause": "No pathogen detected. Vigorous vegetative growth with strong stalk and clean green leaf blades.",
            "symptoms": "Broad, vibrant green leaves with crisp edges and no discoloration or pustules.",
            "treatment": "No treatment required.",
            "organic": "Side-dress with vermicompost; apply seaweed extract during knee-high stage.",
            "prevention": "Maintain soil moisture at flowering; scout weekly for fall armyworm."
        },
        "hi": {
            "name": "मक्का - स्वस्थ (Healthy Corn)",
            "crop": "मक्का",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं। फसल स्वस्थ और मजबूत है।",
            "symptoms": "चौड़ी, हरी पत्तियां बिना किसी धब्बे या कीट के नुकसान के।",
            "treatment": "दवा की आवश्यकता नहीं है।",
            "organic": "वर्मीकम्पोस्ट (केंचुआ खाद) दें और जैविक वृद्धि वर्धक का प्रयोग करें।",
            "prevention": "घुटने तक की ऊंचाई पर यूरिया या खाद दें और कीटों की निगरानी रखें।"
        },
        "te": {
            "name": "మొక్కజొన్న - ఆరోగ్యకరమైనది",
            "crop": "మొక్కజొన్న",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "మొక్క ఆరోగ్యంగా ఉంది.",
            "symptoms": "ఆకులు ఎటువంటి తెగులు మచ్చలు లేకుండా పచ్చగా, బలంగా ఉన్నాయి.",
            "treatment": "ఎటువంటి మందులు అవసరం లేదు.",
            "organic": "వర్మీ కంపోస్ట్ ఎరువును అందించండి.",
            "prevention": "నీటి తడులు సమయానికి అందిస్తూ పంటను గమనించండి."
        }
    },
    "Corn (Maize) - Northern Leaf Blight": {
        "en": {
            "name": "Corn (Maize) - Northern Leaf Blight",
            "crop": "Maize",
            "status": "Diseased",
            "cause": "Fungus Exserohilum turcicum. Thrives in cool to moderate temperatures (18-27°C) and heavy dew.",
            "symptoms": "Long, cigar-shaped, grayish-green to tan lesions (2 to 15 cm long) beginning on lower leaves.",
            "treatment": "Apply foliar sprays of Azoxystrobin + Difenoconazole or Mancozeb at early onset.",
            "organic": "Crop rotation with legumes or oilseeds; foliar application of Trichoderma harzianum.",
            "prevention": "Plant resistant hybrids; plow down previous crop residue deep into the soil."
        },
        "hi": {
            "name": "मक्का - उत्तरी पत्ती झुलसा (Northern Leaf Blight)",
            "crop": "मक्का",
            "status": "रोगग्रस्त",
            "cause": "एक्सरोहिलम टर्सिकम फफूंद (Exserohilum turcicum)। मध्यम तापमान और भारी ओस में पनपता है।",
            "symptoms": "सिगार के आकार के लंबे, धूसर-भूरे रंग के धब्बे (2 से 15 सेमी लंबे), जो निचली पत्तियों से शुरू होते हैं।",
            "treatment": "एज़ोक्सीस्ट्रोबिन + डाइफेनोकोनाज़ोल का छिड़काव करें।",
            "organic": "ट्राइकोडर्मा हर्ज़िएनम का छिड़काव करें; दलहनी फसलों के साथ चक्र अपनाएं।",
            "prevention": "रोगरोधी हाइब्रिड बीज बोएं और पिछली फसल के अवशेषों को गहरी जुताई कर दबाएं।"
        },
        "te": {
            "name": "మొక్కజొన్న - నార్తర్న్ లీఫ్ బ్లైట్ (ఆకు ఎండు తెగులు)",
            "crop": "మొక్కజొన్న",
            "status": "తెగులు బారిన పడింది",
            "cause": "ఎక్సెరోహిలమ్ టర్సికమ్ శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై చుట్ట (సిగార్) ఆకారంలో పొడవాటి బూడిద-గోధుమ రంగు మచ్చలు వస్తాయి.",
            "treatment": "అజాక్సిస్ట్రోబిన్ + డైఫెనోకోనజోల్ మందును పిచికారీ చేయాలి.",
            "organic": "ట్రైకోడెర్మా జీవ శిలీంధ్ర నాశినిని వాడాలి.",
            "prevention": "తెగులును తట్టుకునే రకాలను సాగు చేయాలి; లోతు దుక్కులు చేయాలి."
        }
    },
    "Grape - Black Rot": {
        "en": {
            "name": "Grape - Black Rot",
            "crop": "Grape",
            "status": "Diseased",
            "cause": "Fungus Guignardia bidwellii. Spread by rain splash during warm, wet spring weather.",
            "symptoms": "Reddish-brown circular spots on leaves with black fruiting specks; berries shrivel into black, wrinkled mummies.",
            "treatment": "Apply Mancozeb, Myclobutanil, or Kresoxim-methyl from bud break to 4 weeks post-bloom.",
            "organic": "Remove all mummified fruit clusters during winter; apply copper hydroxide or lime-sulfur during dormancy.",
            "prevention": "Prune for open trellis canopy to accelerate drying; destroy vineyard floor debris."
        },
        "hi": {
            "name": "अंगूर - ब्लैक रॉट (Grape Black Rot)",
            "crop": "अंगूर",
            "status": "रोगग्रस्त",
            "cause": "गुइग्नार्डिया फफूंद। गर्म और बारिश वाले वसंत मौसम में तेजी से फैलता है।",
            "symptoms": "पत्तियों पर लाल-भूरे गोल धब्बे और अंगूर के दाने सूखकर काले, झुर्रीदार मम्मी जैसे बन जाना।",
            "treatment": "मैंकोजेब, माइक्लोबुटानिल या क्रेसोक्सिम-मिथाइल का छिड़काव करें।",
            "organic": "सर्दियों में सूखे व सड़े हुए अंगूर के गुच्छों को नष्ट करें; कॉपर हाइड्रोक्साइड का छिड़काव करें।",
            "prevention": "कैनोपी की छंटाई करें ताकि धूप और हवा मिले; जमीन पर गिरे कचरे को साफ करें।"
        },
        "te": {
            "name": "ద్రాక్ష - బ్లాక్ రాట్ (Black Rot)",
            "crop": "ద్రాక్ష",
            "status": "తెగులు బారిన పడింది",
            "cause": "గుయిగ్నార్డియా శిలీంధ్రం వల్ల వర్షపు నీటి ద్వారా వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై ఎరుపు-గోధుమ రంగు మచ్చలు, కాయలు నల్లగా ఎండిపోయి రాలిపోతాయి.",
            "treatment": "మాంకోజెబ్ లేదా మైక్లోబుటానిల్ పిచికారీ చేయాలి.",
            "organic": "ఎండిపోయిన కాయల గుత్తులను తొలగించి కాల్చాలి; కాపర్ పిచికారీ చేయాలి.",
            "prevention": "పందిరిలో గాలి వెలుతురు ఉండేలా కొమ్మలను సరిచేయాలి."
        }
    },
    "Grape - Esca (Black Measles)": {
        "en": {
            "name": "Grape - Esca (Black Measles)",
            "crop": "Grape",
            "status": "Diseased",
            "cause": "Complex of wood-rotting fungi (Phaeoacremonium, Fomitiporia). Enters through large pruning cuts.",
            "symptoms": "'Tiger-stripe' interveinal chlorosis and necrosis on leaves; dark purple spotting on berries; sudden vine apoplexy.",
            "treatment": "No curative chemical exists. Protect fresh pruning cuts immediately with pruning wound sealant containing tebuconazole.",
            "organic": "Apply Trichoderma-based pruning wound paste; avoid pruning during wet rainy conditions.",
            "prevention": "Sanitize pruning tools with 10% bleach between vines; remove and burn dead diseased vines."
        },
        "hi": {
            "name": "अंगूर - एस्का / ब्लैक मीजल्स (Esca)",
            "crop": "अंगूर",
            "status": "रोगग्रस्त",
            "cause": "लकड़ी सड़ाने वाले कवकों का समूह। छंटाई के बड़े घावों से बेल में प्रवेश करता है।",
            "symptoms": "पत्तियों पर 'बाघ की धारियों' जैसे पीले-भूरे निशान; अंगूर के दानों पर गहरे बैंगनी धब्बे।",
            "treatment": "इसका कोई सीधा रासायनिक इलाज नहीं है। छंटाई के तुरंत बाद घाव पर फफूंदनाशक पेस्ट लगाएं।",
            "organic": "ट्राइकोडर्मा युक्त घाव-लेप का प्रयोग करें; बारिश में कभी भी छंटाई न करें।",
            "prevention": "छंटाई के औजारों को विसंक्रमित करें; अत्यधिक संक्रमित बेलों को उखाड़कर नष्ट करें।"
        },
        "te": {
            "name": "ద్రాక్ష - ఎస్కా / బ్లాక్ మీజిల్స్ (Esca)",
            "crop": "ద్రాక్ష",
            "status": "తెగులు బారిన పడింది",
            "cause": "కొయ్యను కుళ్ళింపజేసే శిలీంధ్రాల వల్ల వస్తుంది. కత్తిరింపు గాయాల ద్వారా ప్రవేశిస్తుంది.",
            "symptoms": "ఆకులపై పులి చారల వంటి పసుపు-గోధుమ చారలు ఏర్పడతాయి, కాయలపై మచ్చలు వస్తాయి.",
            "treatment": "కత్తిరింపు గాయాలపై తక్షణమే శిలీంధ్ర నాశిని పేస్ట్ రాయాలి.",
            "organic": "ట్రైకోడెర్మా పేస్ట్ రాయాలి; వర్షంలో కత్తిరింపులు చేయకూడదు.",
            "prevention": "కత్తిరింపు పనిముట్లను శానిటైజ్ చేయాలి."
        }
    },
    "Grape - Healthy": {
        "en": {
            "name": "Grape - Healthy",
            "crop": "Grape",
            "status": "Healthy",
            "cause": "No pathogen detected. Vigorous vine canopy with active tendril growth and clean foliage.",
            "symptoms": "Lush green lobed leaves with intact margins and smooth surfaces.",
            "treatment": "No chemical treatment required.",
            "organic": "Maintain regular canopy management, organic compost, and preventive potassium silicate sprays.",
            "prevention": "Routine preventive scouting; balanced drip fertigation."
        },
        "hi": {
            "name": "अंगूर - स्वस्थ (Healthy Grape)",
            "crop": "अंगूर",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं मिला। बेल स्वस्थ और मजबूत है।",
            "symptoms": "चमकदार हरी, बिना किसी दाग या धब्बे वाली स्वस्थ पत्तियां।",
            "treatment": "उपचार की आवश्यकता नहीं है।",
            "organic": "जैविक खाद दें और हल्की छंटाई से धूप बनाए रखें।",
            "prevention": "संतुलित ड्रिप सिंचाई और नियमित फसल निरीक्षण जारी रखें।"
        },
        "te": {
            "name": "ద్రాక్ష - ఆరోగ్యకరమైనది",
            "crop": "ద్రాక్ష",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదు.",
            "symptoms": "ఆకులు ఎటువంటి మచ్చలు లేకుండా పచ్చగా, కాంతివంతంగా ఉన్నాయి.",
            "treatment": "మందులు అవసరం లేదు.",
            "organic": "సేంద్రీయ ఎరువులతో పోషకాలు అందించాలి.",
            "prevention": "డ్రిప్ ద్వారా క్రమబద్ధమైన నీటిని అందించాలి."
        }
    },
    "Grape - Leaf Blight": {
        "en": {
            "name": "Grape - Leaf Blight (Isariopsis Clavispora)",
            "crop": "Grape",
            "status": "Diseased",
            "cause": "Fungus Pseudocercospora vitis / Isariopsis. Favored by warm, moist tropical and subtropical conditions late in the season.",
            "symptoms": "Irregular large dark reddish-brown blotches on leaves that dry out, turn brittle, and cause premature defoliation.",
            "treatment": "Spray Carbendazim, Mancozeb, or Pyraclostrobin upon early symptom appearance.",
            "organic": "Foliar spray of 1% Bordeaux mixture or copper oxychloride; remove heavily blighted leaves.",
            "prevention": "Improve airflow within the canopy; avoid overhead irrigation; clean fallen leaves."
        },
        "hi": {
            "name": "अंगूर - पत्ती झुलसा (Leaf Blight)",
            "crop": "अंगूर",
            "status": "रोगग्रस्त",
            "cause": "स्यूडोसर्कोस्पोरा / इसारिओप्सिस कवक। मौसम के अंत में गर्म और आर्द्र परिस्थितियों में फैलता है।",
            "symptoms": "पत्तियों पर अनियमित बड़े लाल-भूरे धब्बे, पत्तियां सूखकर कुरकुरी होना और समय से पहले गिरना।",
            "treatment": "कार्बेन्डाजिम या मैंकोजेब का छिड़काव करें।",
            "organic": "1% बोर्डो मिश्रण (Bordeaux mixture) या कॉपर ऑक्सीक्लोराइड का छिड़काव करें।",
            "prevention": "कैनोपी में हवा का संचार बढ़ाएं और ड्रिप सिंचाई का प्रयोग करें।"
        },
        "te": {
            "name": "ద్రాక్ష - ఆకు ఎండు తెగులు (Leaf Blight)",
            "crop": "ద్రాక్ష",
            "status": "తెగులు బారిన పడింది",
            "cause": "సూడోసెర్కోస్పోరా శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై పెద్ద ఎరుపు-గోధుమ రంగు మచ్చలు ఏర్పడి ఆకులు ఎండి రాలిపోతాయి.",
            "treatment": "కార్బెండజిమ్ లేదా మాంకోజెబ్ పిచికారీ చేయాలి.",
            "organic": "బోర్డో మిశ్రమం (1%) పిచికారీ చేయాలి.",
            "prevention": "చెట్లలో గాలి వెలుతురు ఉండేలా చూసుకోవాలి."
        }
    },
    "Peach - Bacterial Spot": {
        "en": {
            "name": "Peach - Bacterial Spot",
            "crop": "Peach",
            "status": "Diseased",
            "cause": "Bacterium Xanthomonas arboricola pv. pruni. Spread by rain, wind, and humid coastal climates.",
            "symptoms": "Angular purple-black spots on leaves that drop out producing a 'shot-hole' effect; sunken pitting on fruit.",
            "treatment": "Apply copper sprays during dormancy and low rates of oxytetracycline during the growing season.",
            "organic": "Dormant copper octanoate sprays; prune to promote fast foliage drying.",
            "prevention": "Plant resistant peach varieties (e.g., Candor, Biscoe); avoid planting in extremely sandy, nutrient-leached soils."
        },
        "hi": {
            "name": "आड़ू - जीवाणु धब्बा (Bacterial Spot)",
            "crop": "आड़ू",
            "status": "रोगग्रस्त",
            "cause": "जैंथोमोनास बैक्टीरिया। बारिश और हवा के माध्यम से तेजी से फैलता है।",
            "symptoms": "पत्तियों पर कोणीय बैंगनी-काले धब्बे जो सूखकर गिर जाते हैं और छर्रे जैसे छेद (shot-hole) बन जाते हैं।",
            "treatment": "सुप्तावस्था में कॉपर और विकास के समय ऑक्सीटेट्रासाइक्लिन का छिड़काव करें।",
            "organic": "सर्दियों में कॉपर ऑक्टानोएट स्प्रे करें; धूप हेतु पेड़ की छंटाई करें।",
            "prevention": "रोग प्रतिरोधी किस्में लगाएं और संतुलित पोषण बनाए रखें।"
        },
        "te": {
            "name": "పీచ్ - బాక్టీరియల్ స్పాట్",
            "crop": "పీచ్",
            "status": "తెగులు బారిన పడింది",
            "cause": "జాంతోమోనాస్ బాక్టీరియా వల్ల వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై కోణీయ మచ్చలు ఏర్పడి ఆకులు తూట్లు పడతాయి.",
            "treatment": "కాపర్ మందులు లేదా ఆక్సిటెట్రాసైక్లిన్ పిచికారీ చేయాలి.",
            "organic": "శీతాకాలంలో కాపర్ పిచికారీ చేయాలి.",
            "prevention": "తెగులు తట్టుకునే రకాలను నాటాలి."
        }
    },
    "Peach - Healthy": {
        "en": {
            "name": "Peach - Healthy",
            "crop": "Peach",
            "status": "Healthy",
            "cause": "No pathogen detected. Vigorous shoot growth with healthy linear foliage.",
            "symptoms": "Long, glossy lanceolate leaves with serrated margins and vibrant green color.",
            "treatment": "No treatment required.",
            "organic": "Balanced compost tea, trunk white-washing against sunscald, and organic mulching.",
            "prevention": "Scout for peach tree borers and oriental fruit moth; maintain uniform watering."
        },
        "hi": {
            "name": "आड़ू - स्वस्थ (Healthy Peach)",
            "crop": "आड़ू",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं पाया गया। पेड़ पूरी तरह स्वस्थ है।",
            "symptoms": "लंबी, चमकदार हरी पत्तियां बिना किसी छेद या धब्बे के।",
            "treatment": "दवा की आवश्यकता नहीं है।",
            "organic": "कम्पोस्ट खाद दें और तने पर सफेदी लगाएं ताकि धूप से नुकसान न हो।",
            "prevention": "तना छेदक कीट पर नजर रखें और उचित सिंचाई बनाए रखें।"
        },
        "te": {
            "name": "పీచ్ - ఆరోగ్యకరమైనది",
            "crop": "పీచ్",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదు.",
            "symptoms": "ఆకులు పొడవుగా, పచ్చగా ఆరోగ్యంగా ఉన్నాయి.",
            "treatment": "మందులు అవసరం లేదు.",
            "organic": "సేంద్రీయ ఎరువులను వాడండి.",
            "prevention": "బోదె పురుగులు ఆశించకుండా జాగ్రత్త పడాలి."
        }
    },
    "Potato - Early Blight": {
        "en": {
            "name": "Potato - Early Blight",
            "crop": "Potato",
            "status": "Diseased",
            "cause": "Fungus Alternaria solani. Favored by warm temperatures (24-29°C) and alternating wet and dry periods.",
            "symptoms": "Dark brown circular spots with distinct concentric rings ('target-board' pattern) on older leaves, surrounded by yellow chlorotic halos.",
            "treatment": "Apply Chlorothalonil, Mancozeb, or Azoxystrobin every 7-10 days under disease pressure.",
            "organic": "Spray copper hydroxide or Bacillus amyloliquefaciens; strip lower infected leaves.",
            "prevention": "Practice 3-year rotation with non-solanaceous crops; maintain optimal plant vigor with balanced nitrogen."
        },
        "hi": {
            "name": "आलू - अगेती झुलसा (Potato Early Blight)",
            "crop": "आलू",
            "status": "रोगग्रस्त",
            "cause": "अल्टरनेरिया सोलानी फफूंद। गर्म तापमान (24-29°C) और सूखे-गीले मौसम में फैलता है।",
            "symptoms": "पुरानी पत्तियों पर गोल भूरे धब्बे जिनमें 'लक्ष्य-पट्ट' (target board) जैसी संकेंद्री वलय होती हैं और पीला घेरा होता है।",
            "treatment": "क्लोरोथैलोनिल, मैंकोजेब या एज़ोक्सीस्ट्रोबिन का छिड़काव 7-10 दिनों के अंतराल पर करें।",
            "organic": "कॉपर हाइड्रोक्साइड या बेसिलस का छिड़काव करें; निचली संक्रमित पत्तियों को तोड़ें।",
            "prevention": "3 साल का फसल चक्र अपनाएं; अत्यधिक या असंतुलित यूरिया से बचें।"
        },
        "te": {
            "name": "బంగాళాదుంప - ప్రారంభ తెగులు (Early Blight)",
            "crop": "బంగాళాదుంప",
            "status": "తెగులు బారిన పడింది",
            "cause": "ఆల్టర్నేరియా సోలాని శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై వలయాకారపు గోధుమ రంగు మచ్చలు (టార్గెట్ బోర్డ్ ఆకారం) ఏర్పడతాయి.",
            "treatment": "క్లోరోథలోనిల్ లేదా మాంకోజెబ్ మందును పిచికారీ చేయాలి.",
            "organic": "కాపర్ లేదా జీవ శిలీంధ్ర నాశిని వాడాలి; కింది ఆకులను తొలగించాలి.",
            "prevention": "పంట మార్పిడి పాటించాలి; మొక్కలను ఆరోగ్యంగా ఉంచాలి."
        }
    },
    "Potato - Healthy": {
        "en": {
            "name": "Potato - Healthy",
            "crop": "Potato",
            "status": "Healthy",
            "cause": "No pathogen detected. Vigorous tuberizing canopy with rich dark foliage.",
            "symptoms": "Even dark green compound leaves, firm upright haulms, and clean foliage.",
            "treatment": "No treatment required.",
            "organic": "Hill up soil around stems; apply compost and neem cake to boost immunity.",
            "prevention": "Maintain consistent hilling to shield tubers from sunlight; monitor for Colorado potato beetle."
        },
        "hi": {
            "name": "आलू - स्वस्थ (Healthy Potato)",
            "crop": "आलू",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं मिला। पौधे स्वस्थ हैं और कंद निर्माण अच्छा हो रहा है।",
            "symptoms": "गहरे हरे रंग की संयुक्त पत्तियां, मजबूत तना और स्वस्थ पौधे।",
            "treatment": "दवा की आवश्यकता नहीं है।",
            "organic": "पौधों पर मिट्टी चढ़ाएं और नीम की खली व कम्पोस्ट खाद दें।",
            "prevention": "कंदों को धूप से बचाने के लिए अच्छी मिट्टी चढ़ाएं और कीटों पर नज़र रखें।"
        },
        "te": {
            "name": "బంగాళాదుంప - ఆరోగ్యకరమైనది",
            "crop": "బంగాళాదుంప",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదు.",
            "symptoms": "ఆకులు ముదురు ఆకుపచ్చగా ఆరోగ్యంగా ఉన్నాయి.",
            "treatment": "మందులు అవసరం లేదు.",
            "organic": "మొక్క మొదళ్లలో మట్టిని ఎగదోయాలి మరియు సేంద్రీయ ఎరువులు వేయాలి.",
            "prevention": "దుంపలకు ఎండ తగలకుండా మట్టిని కప్పి ఉంచాలి."
        }
    },
    "Potato - Late Blight": {
        "en": {
            "name": "Potato - Late Blight",
            "crop": "Potato",
            "status": "Diseased",
            "cause": "Oomycete Phytophthora infestans. Catastrophic water mold favored by cool (10-21°C), damp, foggy weather with continuous leaf wetness.",
            "symptoms": "Rapidly expanding water-soaked dark lesions on leaf tips/margins, with white velvety fungal growth on the underside during humid mornings.",
            "treatment": "Apply systemic fungicides like Metalaxyl-Mancozeb, Cymoxanil, or Dimethomorph immediately upon first warning.",
            "organic": "Preventive copper sulfate sprays (Bordeaux mixture); destroy infected cull piles; harvest only during dry weather.",
            "prevention": "Plant certified late-blight-resistant seed tubers; avoid overhead irrigation; destroy volunteer potato plants."
        },
        "hi": {
            "name": "आलू - पछेती झुलसा (Potato Late Blight)",
            "crop": "आलू",
            "status": "रोगग्रस्त",
            "cause": "फाइटोफ्थोरा इन्फेस्टन्स (Phytophthora infestans)। ठंडा (10-21°C), कोहरे और नमी वाला मौसम इसके लिए अत्यंत अनुकूल है।",
            "symptoms": "पत्तियों के किनारों पर तेजी से फैलते हुए पानीदार काले-भूरे धब्बे, सुबह के समय निचली सतह पर सफेद मखमली फफूंद।",
            "treatment": "मेटालेक्सिल + मैंकोजेब (Metalaxyl-Mancozeb) या साइमोक्सानिल का तुरंत छिड़काव करें।",
            "organic": "बोर्डो मिश्रण का निवारक छिड़काव करें; संक्रमित पौधों को उखाड़कर नष्ट करें।",
            "prevention": "प्रमाणित रोगरोधी बीज आलू लगाएं; ड्रिप सिंचाई अपनाएं और खेतों में पानी न रुकने दें।"
        },
        "te": {
            "name": "బంగాళాదుంప - లేట్ బ్లైట్ (చివరి దశ తెగులు)",
            "crop": "బంగాళాదుంప",
            "status": "తెగులు బారిన పడింది",
            "cause": "ఫైటోఫ్తోరా ఇన్ఫెస్టాన్స్ అనే శిలీంధ్రం వల్ల వస్తుంది. చల్లని, తేమతో కూడిన వాతావరణంలో పంటను పూర్తిగా నాశనం చేస్తుంది.",
            "symptoms": "ఆకుల అంచులపై నల్లటి నీటి మచ్చలు ఏర్పడి, ఉదయం వేళల్లో ఆకు వెనుక తెల్లటి బూజు కనిపిస్తుంది.",
            "treatment": "మెటలాక్సిల్ + మాంకోజెబ్ లేదా డైమెథోమార్ఫ్ తక్షణమే పిచికారీ చేయాలి.",
            "organic": "బోర్డో మిశ్రమం పిచికారీ చేయాలి; తెగులు సోకిన మొక్కలను నాశనం చేయాలి.",
            "prevention": "ధృవీకరించిన విత్తన దుంపలను మాత్రమే వాడాలి; పైనుంచి నీరు చల్లకూడదు."
        }
    },
    "Strawberry - Healthy": {
        "en": {
            "name": "Strawberry - Healthy",
            "crop": "Strawberry",
            "status": "Healthy",
            "cause": "No pathogen detected. Vigorous trifoliate foliage with balanced crown development.",
            "symptoms": "Bright glossy green trifoliate leaves with serrated margins and no leaf spotting.",
            "treatment": "No treatment required.",
            "organic": "Pine needle or straw mulching, compost tea, and biofertilizers.",
            "prevention": "Ensure bed renovation after harvest; maintain drip irrigation under plastic mulch."
        },
        "hi": {
            "name": "स्ट्रॉबेरी - स्वस्थ (Healthy Strawberry)",
            "crop": "स्ट्रॉबेरी",
            "status": "स्वस्थ",
            "cause": "कोई रोग नहीं मिला। पौधे स्वस्थ और फलने-फूलने के लिए तैयार हैं।",
            "symptoms": "चमकदार हरी तीन-पत्ती वाली पत्तियां बिना किसी दाग या झुलसन के।",
            "treatment": "दवा की आवश्यकता नहीं है।",
            "organic": "पुआल या चीड़ की पत्तियों की मल्चिंग करें और जैविक खाद दें।",
            "prevention": "ड्रिप सिंचाई का प्रयोग करें ताकि पत्तियां गीली न रहें।"
        },
        "te": {
            "name": "స్ట్రాబెర్రీ - ఆరోగ్యకరమైనది",
            "crop": "స్ట్రాబెర్రీ",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదు.",
            "symptoms": "ఆకులు ఎటువంటి మచ్చలు లేకుండా పచ్చగా, కాంతివంతంగా ఉన్నాయి.",
            "treatment": "మందులు అవసరం లేదు.",
            "organic": "గడ్డితో మల్చింగ్ చేయాలి.",
            "prevention": "డ్రిప్ పద్ధతిలో నీరు అందిస్తూ ఆకులు తడవకుండా చూడాలి."
        }
    },
    "Strawberry - Leaf Scorch": {
        "en": {
            "name": "Strawberry - Leaf Scorch",
            "crop": "Strawberry",
            "status": "Diseased",
            "cause": "Fungus Diplocarpon earlianum. Spread through splashing rain and favored by extended leaf wetness.",
            "symptoms": "Numerous small, irregular purple to dark brownish blotches that coalesce until the entire leaf turns brown, curls upward, and scorches.",
            "treatment": "Apply protective fungicides like Captan, Thiophanate-methyl, or Pyraclostrobin.",
            "organic": "Mow and bury old leaves after harvest; spray copper soap or potassium bicarbonate.",
            "prevention": "Space plants generously on raised beds; remove old infected foliage; use drip tape under mulch."
        },
        "hi": {
            "name": "स्ट्रॉबेरी - पत्ती झुलसा (Leaf Scorch)",
            "crop": "स्ट्रॉबेरी",
            "status": "रोगग्रस्त",
            "cause": "डिप्लोकार्पोन अर्लियानम फफूंद (Diplocarpon earlianum)। बारिश की बूंदों और नमी से फैलता है।",
            "symptoms": "पत्तियों पर छोटे बैंगनी-भूरे धब्बे जो आपस में मिलकर पूरी पत्ती को भूरा और झुलसा हुआ बना देते हैं।",
            "treatment": "कैप्टन या थियोफैनेट-मिथाइल फफूंदनाशक का छिड़काव करें।",
            "organic": "कटाई के बाद पुरानी पत्तियों को हटा दें; कॉपर सोप या पोटेशियम बाइकार्बोनेट का छिड़काव करें।",
            "prevention": "उठी हुई क्यारियों पर उचित दूरी पर पौधे लगाएं और प्लास्टिक मल्च का उपयोग करें।"
        },
        "te": {
            "name": "స్ట్రాబెర్రీ - ఆకు మాకుడు తెగులు (Leaf Scorch)",
            "crop": "స్ట్రాబెర్రీ",
            "status": "తెగులు బారిన పడింది",
            "cause": "డిప్లోకార్పన్ ఎర్లియానం శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై చిన్న ఊదా రంగు మచ్చలు ఏర్పడి క్రమంగా ఆకు మొత్తం ఎండిపోతుంది.",
            "treatment": "క్యాప్టన్ లేదా థియోఫానేట్ మిథైల్ పిచికారీ చేయాలి.",
            "organic": "పాత ఆకులను కత్తిరించి నాశనం చేయాలి; కాపర్ పిచికారీ చేయాలి.",
            "prevention": "మొక్కల మధ్య సరైన దూరం పాటించాలి; డ్రిప్ ఇరిగేషన్ వాడాలి."
        }
    },
    "Tomato - Bacterial Spot": {
        "en": {
            "name": "Tomato - Bacterial Spot",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Bacterium Xanthomonas vesicatoria. Survives in crop debris and seed; spreads via rain splash and touching wet foliage.",
            "symptoms": "Small, dark, greasy water-soaked spots with yellow halos on leaves; raised, scabby circular spots on green fruit.",
            "treatment": "Apply preventive copper bactericide tank-mixed with Mancozeb.",
            "organic": "Foliar application of Bacillus subtilis or copper hydroxide; prune lower suckers for ventilation.",
            "prevention": "Use certified hot water-treated seed; stake plants; practice 3-year crop rotation avoiding all nightshades."
        },
        "hi": {
            "name": "टमाटर - जीवाणु धब्बा (Tomato Bacterial Spot)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "जैंथोमोनास बैक्टीरिया (Xanthomonas)। संक्रमित बीज और बारिश की फुहारों से फैलता है।",
            "symptoms": "पत्तियों पर छोटे काले-भूरे पानीदार धब्बे जिनके चारों ओर पीला घेरा होता है; कच्चे फलों पर उभरे हुए खुरदुरे धब्बे।",
            "treatment": "कॉपर ऑक्सीक्लोराइड को मैंकोजेब के साथ मिलाकर छिड़काव करें।",
            "organic": "बेसिलस सबटिलिस जैव कीटनाशक का छिड़काव करें; नीचे की संक्रमित शाखाएं काटें।",
            "prevention": "प्रमाणित बीजों का ही प्रयोग करें; पौधों को बांस से सहारा दें; 3 साल का फसल चक्र रखें।"
        },
        "te": {
            "name": "టమోటా - బాక్టీరియల్ స్పాట్",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "జాంతోమోనాస్ బాక్టీరియా వల్ల వర్షపు తుంపర్ల ద్వారా వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై చిన్న చిన్న నల్లటి మచ్చలు ఏర్పడతాయి; కాయలపై గరుకు మచ్చలు వస్తాయి.",
            "treatment": "కాపర్ ఆక్సిక్లోరైడ్ మరియు మాంకోజెబ్ కలిపి పిచికారీ చేయాలి.",
            "organic": "జీవ బాక్టీరియా నాశినులను వాడాలి; రాలిన ఆకులను తీసివేయాలి.",
            "prevention": "మొక్కలను కర్రలతో కట్టాలి; రాత్రి వేళల్లో తడి ఉండకుండా చూడాలి."
        }
    },
    "Tomato - Early Blight": {
        "en": {
            "name": "Tomato - Early Blight",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Fungus Alternaria solani. Survives in soil and old solanaceous residue; spreads under warm, wet weather.",
            "symptoms": "Concentric ring 'target' spots on lower, older leaves, accompanied by surrounding chlorosis and premature leaf drop.",
            "treatment": "Apply Chlorothalonil, Mancozeb, or Azoxystrobin every 7 to 14 days.",
            "organic": "Mulch soil surface with straw or black plastic to stop soil splash; spray copper fungicide or neem oil.",
            "prevention": "Prune bottom 12 inches of foliage; stake tomatoes for airflow; rotate crops annually."
        },
        "hi": {
            "name": "टमाटर - अगेती झुलसा (Tomato Early Blight)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "अल्टरनेरिया सोलानी कवक (Alternaria solani)। मिट्टी और पुरानी पत्तियों में जीवित रहता है।",
            "symptoms": "निचली पत्तियों पर छल्लेदार (target) गोल भूरे धब्बे, पत्तियों का पीला पड़ना और गिरना।",
            "treatment": "क्लोरोथैलोनिल या मैंकोजेब का 7-10 दिनों के अंतराल पर छिड़काव करें।",
            "organic": "जमीन पर पुआल की मल्चिंग करें ताकि मिट्टी पत्तियों पर न उछले; नीम का तेल छिड़कें।",
            "prevention": "पौधे के नीचे की 1 फीट पत्तियों को काट दें; पौधों को सहारा दें और हर साल फसल बदलें।"
        },
        "te": {
            "name": "టమోటా - ప్రారంభ తెగులు (Early Blight)",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "ఆల్టర్నేరియా సోలాని శిలీంధ్రం వల్ల వస్తుంది. నేలలోని తేమ ద్వారా వ్యాపిస్తుంది.",
            "symptoms": "కింది ఆకులపై వలయాకార మచ్చలు ఏర్పడి ఆకులు పసుపు రంగులోకి మారి రాలిపోతాయి.",
            "treatment": "క్లోరోథలోనిల్ లేదా మాంకోజెబ్ మందును పిచికారీ చేయాలి.",
            "organic": "నేలపై మల్చింగ్ షీట్ లేదా గడ్డి పరచాలి; వేపనూనె పిచికారీ చేయాలి.",
            "prevention": "కింది భాగంలోని ఆకులను కత్తిరించాలి; కర్రల సహాయంతో మొక్కలను నిలబెట్టాలి."
        }
    },
    "Tomato - Healthy": {
        "en": {
            "name": "Tomato - Healthy",
            "crop": "Tomato",
            "status": "Healthy",
            "cause": "No pathogen detected. Vigorous plant architecture with vibrant green foliage and stout stems.",
            "symptoms": "Clean, fragrant compound leaves without spotting, curling, mosaic patterns, or blight lesions.",
            "treatment": "No chemical treatment required.",
            "organic": "Maintain regular watering, organic compost, calcium-rich soil amendments to prevent blossom end rot.",
            "prevention": "Scout for whiteflies, hornworms, and spider mites; stake and prune regularly."
        },
        "hi": {
            "name": "टमाटर - स्वस्थ (Healthy Tomato)",
            "crop": "टमाटर",
            "status": "स्वस्थ",
            "cause": "कोई रोग या कवक नहीं है। पौधा पूरी तरह स्वस्थ और मजबूत है।",
            "symptoms": "स्वच्छ, सुगंधित हरी पत्तियां बिना किसी धब्बे, मोज़ेक या सड़न के।",
            "treatment": "किसी दवा की जरूरत नहीं है।",
            "organic": "नियमित जैविक खाद दें और फल गलन से बचाव हेतु कैल्शियम युक्त चूना या राख दें।",
            "prevention": "सफेद मक्खी और इल्लियों की निगरानी रखें; पौधों को सहारा दें।"
        },
        "te": {
            "name": "టమోటా - ఆరోగ్యకరమైనది",
            "crop": "టమోటా",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎటువంటి తెగులు లేదు.",
            "symptoms": "ఆకులు ఎటువంటి మచ్చలు లేదా ముడతలు లేకుండా పచ్చగా ఉన్నాయి.",
            "treatment": "మందులు అవసరం లేదు.",
            "organic": "సమతుల్య సేంద్రీయ ఎరువులు మరియు కాల్షియం అందించాలి.",
            "prevention": "తెల్లదోమ మరియు ఇతర పురుగులను గమనిస్తూ ఉండాలి."
        }
    },
    "Tomato - Late Blight": {
        "en": {
            "name": "Tomato - Late Blight",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Phytophthora infestans. Devastating water mold that spreads during cool, wet, cloudy, rainy periods.",
            "symptoms": "Rapidly spreading greasy, dark water-soaked lesions on leaves and stems; white fuzzy mold on underside; brown greasy rot on fruits.",
            "treatment": "Apply Cymoxanil, Dimethomorph, or Metalaxyl-Mancozeb immediately at first sign.",
            "organic": "Apply copper sulfate (Bordeaux mixture); immediately uproot and bag severely blighted plants to stop spore drift.",
            "prevention": "Plant late-blight-resistant varieties (e.g., Defiant, Mountain Merit); do not overhead irrigate."
        },
        "hi": {
            "name": "टमाटर - पछेती झुलसा (Tomato Late Blight)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "फाइटोफ्थोरा इन्फेस्टन्स फफूंद। ठंडे, बादल छाए और बारिश वाले मौसम में यह कुछ ही दिनों में पूरी फसल नष्ट कर सकता है।",
            "symptoms": "पत्तियों और तने पर तेजी से फैलते हुए पानीदार काले धब्बे, पत्ती के नीचे सफेद फफूंद और फलों का सड़ना।",
            "treatment": "साइमोक्सानिल या मेटालेक्सिल-मैंकोजेब का तुरंत छिड़काव करें।",
            "organic": "बोर्डो मिश्रण का छिड़काव करें; गंभीर रूप से बीमार पौधों को तुरंत उखाड़कर नष्ट करें।",
            "prevention": "रोगरोधी किस्में लगाएं और शाम के समय पौधों पर पानी का छिड़काव न करें।"
        },
        "te": {
            "name": "టమోటా - చివరి దశ తెగులు (Late Blight)",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "ఫైటోఫ్తోరా ఇన్ఫెస్టాన్స్ అనే శిలీంధ్రం వల్ల వస్తుంది. చల్లని, తడి వాతావరణంలో పంటను వేగంగా నాశనం చేస్తుంది.",
            "symptoms": "ఆకులు, కాండంపై నల్లటి నీటి మచ్చలు ఏర్పడి మొక్క మొత్తం కుళ్ళిపోతుంది.",
            "treatment": "సైమోక్సానిల్ లేదా మెటలాక్సిల్ + మాంకోజెబ్ తక్షణమే పిచికారీ చేయాలి.",
            "organic": "బోర్డో మిశ్రమం పిచికారీ చేయాలి; తెగులు సోకిన మొక్కలను కాల్చివేయాలి.",
            "prevention": "తేమ ఎక్కువగా ఉండకుండా చూసుకోవాలి."
        }
    },
    "Tomato - Septoria Leaf Spot": {
        "en": {
            "name": "Tomato - Septoria Leaf Spot",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Fungus Septoria lycopersici. Overwinters on weed hosts (horsenettle) and tomato residue; spreads via rain splashes.",
            "symptoms": "Numerous small circular spots (1-3 mm) with dark brown borders and light gray/tan centers speckled with tiny black fruiting bodies.",
            "treatment": "Apply Chlorothalonil or Mancozeb sprays beginning at early fruit cluster formation.",
            "organic": "Prune out affected lower leaves; spray liquid copper fungicide; mulch around plant base.",
            "prevention": "Avoid handling wet tomato foliage; practice strict weed control around plots; 2-year crop rotation."
        },
        "hi": {
            "name": "टमाटर - सेप्टोरिया पत्ती धब्बा (Septoria Leaf Spot)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "सेप्टोरिया लाइकोपरसिकी फफूंद। पुरानी पत्तियों और खरपतवारों में रहता है और बारिश की बूंदों से फैलता है।",
            "symptoms": "पत्तियों पर असंख्य छोटे गोल धब्बे (1-3 मिमी) जिनके किनारे गहरे भूरे और केंद्र में हल्का धूसर रंग होता है।",
            "treatment": "क्लोरोथैलोनिल या मैंकोजेब का छिड़काव करें।",
            "organic": "संक्रमित निचली पत्तियों को तोड़ें; कॉपर फफूंदनाशक का छिड़काव करें; मल्चिंग करें।",
            "prevention": "गीले पौधों को न छुएं; खेत में खरपतवार न पनपने दें और 2 साल का फसल चक्र रखें।"
        },
        "te": {
            "name": "టమోటా - సెప్టోరియా ఆకుమచ్చ తెగులు",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "సెప్టోరియా లైకోపెర్సికి శిలీంధ్రం వల్ల వస్తుంది. వర్షపు తుంపర్ల ద్వారా వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై చిన్న చిన్న గుండ్రని మచ్చలు (మధ్యలో బూడిద రంగు, చుట్టూ ముదురు గోధుమ రంగు) ఏర్పడతాయి.",
            "treatment": "క్లోరోథలోనిల్ లేదా మాంకోజెబ్ మందును పిచికారీ చేయాలి.",
            "organic": "తెగులు సోకిన ఆకులను తీసివేయాలి; కాపర్ పిచికారీ చేయాలి.",
            "prevention": "పొలంలో కలుపు లేకుండా చూసుకోవాలి; మొక్కలను తడి ఉన్నప్పుడు తాకకూడదు."
        }
    },
    "Tomato - Yellow Leaf Curl Virus": {
        "en": {
            "name": "Tomato - Yellow Leaf Curl Virus",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Begomovirus (TYLCV). Exclusively transmitted by the silverleaf whitefly (Bemisia tabaci).",
            "symptoms": "Severe upward leaf curling, yellowing of leaf margins, thick leathery texture, severe plant stunting, and flower abortion.",
            "treatment": "No cure for viral infection. Immediately control the whitefly vector using Imidacloprid, Acetamiprid, or Spirotetramat.",
            "organic": "Install yellow sticky cards; spray neem oil (10,000 ppm) or insecticidal soap; remove and bag infected plants.",
            "prevention": "Use 50-mesh insect-proof netting in nurseries; grow resistant tomato varieties (e.g., Tygress, Grandela)."
        },
        "hi": {
            "name": "टमाटर - पीला पत्ती मरोड़ वायरस (Yellow Leaf Curl Virus)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "बेगोमोवायरस (TYLCV)। यह सफेद मक्खी (Whitefly) कीट द्वारा फैलता है।",
            "symptoms": "पत्तियां ऊपर की ओर मुड़ना (कटोरीनुमा), किनारों से पीला पड़ना, पौधे का कद छोटा रह जाना और फूल गिरना।",
            "treatment": "वायरस का कोई सीधा इलाज नहीं है। सफेद मक्खी को मारने के लिए इमिडाक्लोप्रिड या एसिटामिप्रिड का छिड़काव करें।",
            "organic": "पीले चिपचिपे कार्ड (Yellow Sticky Traps) लगाएं; नीम का तेल स्प्रे करें; रोगग्रस्त पौधों को उखाड़कर नष्ट करें।",
            "prevention": "नर्सरी में 50-मेश जाली का उपयोग करें; वायरस-प्रतिरोधी किस्मों की बुवाई करें।"
        },
        "te": {
            "name": "టమోటా - ఆకు ముడుత వైరస్ (Yellow Leaf Curl)",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "తెల్లదోమ (వైట్‌ఫ్లై) ద్వారా వ్యాపించే వైరస్ తెగులు.",
            "symptoms": "ఆకులు పైకి దోనె వలె ముడుచుకుపోవడం, పసుపు రంగులోకి మారడం, మొక్క ఎదుగుదల ఆగిపోవడం.",
            "treatment": "వైరస్ నివారణకు మందులు లేవు. తెల్లదోమ నివారణకు ఇమిడాక్లోప్రిడ్ పిచికారీ చేయాలి.",
            "organic": "పసుపు జిగురు అట్టలను ఏర్పాటు చేయాలి; వేప నూనెను పిచికారీ చేయాలి; తెగులు సోకిన మొక్కలను పీకివేయాలి.",
            "prevention": "తెగులును తట్టుకునే రకాలను నాటాలి; నర్సరీ దశలో రక్షణ వలలను వాడాలి."
        }
    },
    "Blueberry - Healthy": {
        "en": {
            "name": "Blueberry - Healthy",
            "crop": "Blueberry",
            "status": "Healthy",
            "cause": "No pathogen detected. The foliage shows normal physiological condition.",
            "symptoms": "Vibrant foliage, robust shoots, normal leaf turgor and color.",
            "treatment": "No treatment required. Maintain acidic soil (pH 4.5-5.5) and adequate pine bark or peat mulch.",
            "organic": "Compost with ericaceous mulch, rainwater irrigation.",
            "prevention": "Annual pruning of oldest stems and consistent soil moisture."
        },
        "hi": {
            "name": "ब्लूबेरी - स्वस्थ (Healthy)",
            "crop": "ब्लूबेरी",
            "status": "स्वस्थ",
            "cause": "पौधा पूरी तरह स्वस्थ है।",
            "symptoms": "चमकदार हरी पत्तियां और मजबूत विकास।",
            "treatment": "किसी उपचार की आवश्यकता नहीं है। मिट्टी का pH 4.5-5.5 बनाए रखें।",
            "organic": "अम्लीय कम्पोस्ट और पाइन छाल का उपयोग करें।",
            "prevention": "नियमित छंटाई और उचित नमी बनाए रखें।"
        },
        "te": {
            "name": "బ్లూబెర్రీ - ఆరోగ్యకరమైనది",
            "crop": "బ్లూబెర్రీ",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "మొక్క ఆరోగ్యంగా ఉంది, ఎలాంటి తెగులు లేదు.",
            "symptoms": "ఆకులు పచ్చగా, బలంగా ఉన్నాయి.",
            "treatment": "చికిత్స అవసరం లేదు. నేల pH 4.5-5.5 ఉండేలా చూసుకోవాలి.",
            "organic": "సేంద్రియ ఎరువులు మరియు తగినంత తేమ అందించాలి.",
            "prevention": "ఎండిన కొమ్మలను తొలగించి క్రమబద్ధమైన నీటిపారుదల చేయాలి."
        }
    },
    "Orange - Huanglongbing (Citrus Greening)": {
        "en": {
            "name": "Orange - Huanglongbing (Citrus Greening)",
            "crop": "Orange",
            "status": "Diseased",
            "cause": "Bacterium Candidatus Liberibacter asiaticus, vectored by Asian citrus psyllid (Diaphorina citri).",
            "symptoms": "Blotchy mottle yellowing across leaf veins, small lopsided bitter fruits remaining green at base, twig dieback.",
            "treatment": "No cure once infected. Aggressively manage psyllid vectors using Thiamethoxam or Imidacloprid.",
            "organic": "Remove and destroy infected trees immediately; spray horticultural mineral oils; release Tamarixia radiata parasitoid wasps.",
            "prevention": "Plant certified disease-free nursery stock and establish protective windbreaks."
        },
        "hi": {
            "name": "संतरा - सिट्रस ग्रीनिंग (Huanglongbing)",
            "crop": "संतरा",
            "status": "रोगग्रस्त",
            "cause": "कैंडिडेटस लिबेरीबैक्टर जीवाणु। यह एशियाई सिट्रस सिलिड कीट द्वारा फैलता है।",
            "symptoms": "पत्तियों की नसों पर असमान पीलापन, फल छोटे और कड़वे रहना, टहनियां सूखना।",
            "treatment": "बीमारी का कोई सीधा इलाज नहीं है। वाहक सिलिड कीट को नियंत्रित करने के लिए थियामेथोक्सम का छिड़काव करें।",
            "organic": "संक्रमित पेड़ों को काटकर जलाएं; नीम तेल व मिनरल ऑयल स्प्रे करें।",
            "prevention": "प्रमाणित रोगमुक्त पौधे लगाएं और नियमित निगरानी करें।"
        },
        "te": {
            "name": "నారింజ - సిట్రస్ గ్రీనింగ్ తెగులు",
            "crop": "నారింజ",
            "status": "తెగులు బారిన పడింది",
            "cause": "సిట్రస్ సిల్లిడ్ అనే కీటం ద్వారా వ్యాపించే బ్యాక్టీరియా తెగులు.",
            "symptoms": "ఆకుల ఈనెల మధ్య పసుపు పచ్చని మచ్చలు, కాయలు వంకరగా మారి చేదుగా ఉండడం.",
            "treatment": "ఈ తెగులుకు నివారణ లేదు. సిల్లిడ్ కీటకాల నివారణకు థయామెథోక్సామ్ పిచికారీ చేయాలి.",
            "organic": "బాధిత చెట్లను తీసివేసి నాశనం చేయాలి; వేప నూనె వాడాలి.",
            "prevention": "ధృవీకరించబడిన ఆరోగ్యకరమైన మొక్కలను మాత్రమే నాటాలి."
        }
    },
    "Raspberry - Healthy": {
        "en": {
            "name": "Raspberry - Healthy",
            "crop": "Raspberry",
            "status": "Healthy",
            "cause": "No pathogen detected. Vigorous vegetative growth.",
            "symptoms": "Deep green leaves, strong cane development, no cane lesions or leaf discoloration.",
            "treatment": "No treatment needed. Maintain trellis support and balanced watering.",
            "organic": "Apply composted wood chips, ensure good air circulation.",
            "prevention": "Prune floricanes after harvest."
        },
        "hi": {
            "name": "रास्पबेरी - स्वस्थ (Healthy)",
            "crop": "रास्पबेरी",
            "status": "स्वस्थ",
            "cause": "पौधा पूरी तरह स्वस्थ है।",
            "symptoms": "गहरी हरी पत्तियां और मजबूत शाखाएं।",
            "treatment": "किसी उपचार की आवश्यकता नहीं है।",
            "organic": "उचित कम्पोस्ट और मल्चिंग करें।",
            "prevention": "फसल के बाद पुरानी टहनियों की छंटाई करें।"
        },
        "te": {
            "name": "రాస్ప్బెర్రీ - ఆరోగ్యకరమైనది",
            "crop": "రాస్ప్బెర్రీ",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "ఎలాంటి తెగులు సోకలేదు.",
            "symptoms": "పచ్చని ఆరోగ్యవంతమైన ఆకులు మరియు కాండం.",
            "treatment": "చికిత్స అవసరం లేదు.",
            "organic": "సేంద్రియ ఎరువులు వేయాలి.",
            "prevention": "పాత కొమ్మలను తొలగించాలి."
        }
    },
    "Soybean - Healthy": {
        "en": {
            "name": "Soybean - Healthy",
            "crop": "Soybean",
            "status": "Healthy",
            "cause": "No pathogen detected. Crop is thriving.",
            "symptoms": "Uniform trifoliate foliage, vigorous growth, healthy nodulation.",
            "treatment": "No treatment needed.",
            "organic": "Rhizobium biofertilizer inoculation.",
            "prevention": "Rotate with corn or grasses."
        },
        "hi": {
            "name": "सोयाबीन - स्वस्थ (Healthy)",
            "crop": "सोयाबीन",
            "status": "स्वस्थ",
            "cause": "फसल पूर्णतः स्वस्थ है।",
            "symptoms": "समान हरी पत्तियां और स्वस्थ विकास।",
            "treatment": "उपचार की आवश्यकता नहीं।",
            "organic": "राइजोबियम कल्चर का उपयोग करें।",
            "prevention": "मक्का या ज्वार के साथ फसल चक्र अपनाएं।"
        },
        "te": {
            "name": "సోయాబీన్ - ఆరోగ్యకరమైనది",
            "crop": "సోయాబీన్",
            "status": "ఆరోగ్యంగా ఉంది",
            "cause": "మొక్క ఆరోగ్యంగా ఉంది.",
            "symptoms": "ఆకులు ఆరోగ్యంగా, పచ్చగా ఉన్నాయి.",
            "treatment": "చికిత్స అవసరం లేదు.",
            "organic": "రైజోబియం వాడాలి.",
            "prevention": "పంట మార్పిడి పాటించాలి."
        }
    },
    "Squash - Powdery Mildew": {
        "en": {
            "name": "Squash - Powdery Mildew",
            "crop": "Squash",
            "status": "Diseased",
            "cause": "Fungus Podosphaera xanthii. Flourishes in warm, dry weather with dense canopy shading.",
            "symptoms": "White talcum-powder-like fungal patches on upper and lower leaf surfaces, leading to yellowing and premature drying.",
            "treatment": "Apply Azoxystrobin, Triflumizole, or Myclobutanil at first sign of white spots.",
            "organic": "Spray potassium bicarbonate (3g/L), diluted milk spray (40% milk, 60% water), or neem oil.",
            "prevention": "Choose resistant squash varieties and increase plant spacing for airflow."
        },
        "hi": {
            "name": "कद्दू/लौकी - चूर्णी फफूंद (Powdery Mildew)",
            "crop": "कद्दू/लौकी",
            "status": "रोगग्रस्त",
            "cause": "पोडोस्फेरा जैन्थी फफूंद। गर्म और शुष्क मौसम में तेजी से पनपता है।",
            "symptoms": "पत्तियों पर सफेद पाउडर जैसे धब्बे, पत्तियां पीली पड़कर सूखना।",
            "treatment": "एज़ोक्सीस्ट्रोबिन (Azoxystrobin) या माइक्लोबुटानिल का छिड़काव करें।",
            "organic": "पोटेशियम बाइकार्बोनेट या नीम के तेल (3%) का स्प्रे करें।",
            "prevention": "पौधों के बीच पर्याप्त दूरी रखें ताकि धूप और हवा मिले।"
        },
        "te": {
            "name": "గుమ్మడి/దోస - బూడిద తెగులు (Powdery Mildew)",
            "crop": "గుమ్మడి",
            "status": "తెగులు బారిన పడింది",
            "cause": "పోడోస్ఫెరా జాంతి శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై బూడిద వంటి తెల్లని పొర ఏర్పడి ఆకులు ఎండిపోతాయి.",
            "treatment": "అజోక్సిస్ట్రోబిన్ లేదా మైక్లోబ్యుటానిల్ పిచికారీ చేయాలి.",
            "organic": "పొటాషియం బైకార్బోనేట్ లేదా వేప నూనె పిచికారీ చేయాలి.",
            "prevention": "మొక్కల మధ్య తగినంత గాలి వెలుతురు ఉండేలా నాటాలి."
        }
    },
    "Tomato - Leaf Mold": {
        "en": {
            "name": "Tomato - Leaf Mold",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Fungus Passalora fulva (Cladosporium fulvum). Highly prevalent in high-humidity (>85%) greenhouse conditions.",
            "symptoms": "Pale green to yellowish spots on upper leaf surfaces, with olive-green to grayish velvety mold on the undersides.",
            "treatment": "Apply Chlorothalonil, Mancozeb, or Copper sulfate at early symptoms.",
            "organic": "Spray biofungicides containing Bacillus amyloliquefaciens; drastically improve greenhouse ventilation.",
            "prevention": "Maintain relative humidity below 80% and avoid overhead watering."
        },
        "hi": {
            "name": "टमाटर - पत्ती का फफूंद (Leaf Mold)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "क्लैडोस्पोरियम फफूंद। अत्यधिक नमी (>85%) और पॉलीहाउस में तेजी से फैलता है।",
            "symptoms": "पत्तियों की ऊपरी सतह पर पीले धब्बे और निचली सतह पर जैतून जैसा मखमली फफूंद।",
            "treatment": "क्लोरोथैलोनिल या मैंकोजेब का छिड़काव करें।",
            "organic": "ग्रीनहाउस में वेंटिलेशन बढ़ाएं; कॉपर कवकनाशी स्प्रे करें।",
            "prevention": "नमी 80% से कम रखें और ड्रिप सिंचाई का उपयोग करें।"
        },
        "te": {
            "name": "టమోటా - ఆకు బూజు తెగులు (Leaf Mold)",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "పాసలోరా ఫుల్వా శిలీంధ్రం వల్ల వస్తుంది. అధిక తేమ ఉన్నప్పుడు వ్యాపిస్తుంది.",
            "symptoms": "ఆకుల పైభాగంలో పసుపు మచ్చలు, అడుగు భాగంలో ఆలివ్ ఆకుపచ్చ రంగు బూజు.",
            "treatment": "క్లోరోథలోనిల్ లేదా మాంకోజెబ్ మందును పిచికారీ చేయాలి.",
            "organic": "గాలి వెలుతురు పెంచాలి; కాపర్ పిచికారీ చేయాలి.",
            "prevention": "పంటలో అధిక తేమ లేకుండా చూసుకోవాలి."
        }
    },
    "Tomato - Spider Mites (Two-spotted spider mite)": {
        "en": {
            "name": "Tomato - Spider Mites (Two-spotted spider mite)",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Tetranychus urticae (Arachnid mite pest). Proliferates rapidly under hot, dry, dusty conditions.",
            "symptoms": "Fine yellow-white stippling on leaf surfaces, bronzing and drying of leaves, and visible fine webbing covering shoots.",
            "treatment": "Apply acaricides/miticides such as Abamectin, Bifenazate, or Spiromesifen.",
            "organic": "Spray insecticidal soap, rosemary oil, or neem oil; introduce predatory mites (Phytoseiulus persimilis).",
            "prevention": "Keep soil adequately watered; wash dust off field foliage regularly."
        },
        "hi": {
            "name": "टमाटर - लाल मकड़ी (Spider Mites)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "टेट्रानिचस अर्टिके (Spider Mite)। गर्म, शुष्क और धूल भरे मौसम में तेजी से बढ़ता है।",
            "symptoms": "पत्तियों पर पीले-सफेद बारीक बिंदु (Stippling), पत्तियों पर बारीक जाले और पत्तियों का सूखना।",
            "treatment": "एबामेक्टिन (Abamectin) या स्पाइरोमेसिफेन माइटिसाइड का छिड़काव करें।",
            "organic": "नीम का तेल (5 मिली/लीटर) या साबुन के घोल का छिड़काव करें।",
            "prevention": "खेत को नम रखें और धूल जमा न होने दें।"
        },
        "te": {
            "name": "టమోటా - నల్లి/సాలీడు పురుగు (Spider Mites)",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "ఎర్ర నల్లి లేదా సాలీడు పురుగు ఆకుల రసాన్ని పీల్చడం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై చిన్న చిన్న పసుపు రంగు చుక్కలు, ఆకుల అడుగున సన్నని తెల్లని బూజు/జాలాలు.",
            "treatment": "అబామెక్టిన్ లేదా స్పైరోమెసిఫెన్ పిచికారీ చేయాలి.",
            "organic": "వేప నూనె లేదా సబ్బు ద్రావణం పిచికారీ చేయాలి.",
            "prevention": "పొలంలో దుమ్ము లేకుండా మరియు తగినంత తేమ ఉంచాలి."
        }
    },
    "Tomato - Target Spot": {
        "en": {
            "name": "Tomato - Target Spot",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Fungus Corynespora cassiicola. Thrives in warm, humid tropical and subtropical climates.",
            "symptoms": "Small pinpoint brown spots on foliage enlarging into concentric circular lesions resembling a bullseye/target.",
            "treatment": "Apply Azoxystrobin + Difenoconazole or Boscalid + Pyraclostrobin.",
            "organic": "Spray copper hydroxide or Bacillus subtilis bio-fungicide; remove lower infected leaves.",
            "prevention": "Maintain wide row spacing to promote canopy drying; avoid overhead irrigation."
        },
        "hi": {
            "name": "टमाटर - टारगेट स्पॉट (Target Spot)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "कोरीनेस्पोरा कैसीकोला फफूंद। गर्म और अत्यधिक आर्द्र मौसम में फैलता है।",
            "symptoms": "पत्तियों पर लक्ष्य (Bullseye/Target) जैसे गोल चक्राकार भूरे धब्बे, पत्तियां गिरना।",
            "treatment": "एज़ोक्सीस्ट्रोबिन या पाइराक्लोस्ट्रोबिन कवकनाशी का छिड़काव करें।",
            "organic": "कॉपर हाइड्रोक्साइड या बैसिलस सबटिलिस का छिड़काव करें; निचली रोगग्रस्त पत्तियों को हटाएं।",
            "prevention": "पौधों के बीच दूरी रखें और टपक सिंचाई करें।"
        },
        "te": {
            "name": "టమోటా - టార్గెట్ స్పాట్ (లక్ష్యపు మచ్చ తెగులు)",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "కోరినెస్‌స్పోరా కాసికోలా శిలీంధ్రం వల్ల వస్తుంది.",
            "symptoms": "ఆకులపై చక్రాల వంటి గుండ్రని ముదురు గోధుమ రంగు మచ్చలు (టార్గెట్ బోర్డు వలె).",
            "treatment": "అజోక్సిస్ట్రోబిన్ లేదా మాంకోజెబ్ పిచికారీ చేయాలి.",
            "organic": "కాపర్ హైడ్రాక్సైడ్ స్ప్రే చేయాలి.",
            "prevention": "పైనుండి నీరు పోయకుండా డ్రిప్ పద్ధతి వాడాలి."
        }
    },
    "Tomato - Tomato Mosaic Virus": {
        "en": {
            "name": "Tomato - Tomato Mosaic Virus",
            "crop": "Tomato",
            "status": "Diseased",
            "cause": "Tobamovirus (ToMV). Extremely stable mechanically transmitted virus via hands, tools, and infected seeds.",
            "symptoms": "Mottling with alternating light green and dark green mosaic patterns on foliage, distorted 'shoestring' leaves.",
            "treatment": "No cure for viral disease. Disinfect all tools with 20% nonfat dry milk or 10% trisodium phosphate (TSP).",
            "organic": "Immediately rogue and burn infected plants; wash hands thoroughly before touching healthy plants.",
            "prevention": "Use certified virus-free seed; avoid tobacco use near plants; plant resistant hybrid varieties."
        },
        "hi": {
            "name": "टमाटर - मोजेक वायरस (Tomato Mosaic Virus)",
            "crop": "टमाटर",
            "status": "रोगग्रस्त",
            "cause": "टोबामोवायरस (ToMV)। यह हाथों, औजारों और संक्रमित बीजों के माध्यम से आसानी से फैलता है।",
            "symptoms": "पत्तियों पर हल्के और गहरे हरे रंग के मोजेक जैसे धब्बे, पत्तियां विकृत होना।",
            "treatment": "वायरस का कोई इलाज नहीं है। औजारों को ट्राइसोडियम फॉस्फेट या दूध के घोल से साफ करें।",
            "organic": "संक्रमित पौधों को उखाड़कर तुरंत नष्ट करें; हाथों को साबुन से धोएं।",
            "prevention": "रोग-प्रतिरोधी बीज लगाएं; तंबाकू का उपयोग करने वालों को पौधों को छूने न दें।"
        },
        "te": {
            "name": "టమోటా - మొజాయిక్ వైరస్ తెగులు",
            "crop": "టమోటా",
            "status": "తెగులు బారిన పడింది",
            "cause": "టోబామోవైరస్ వల్ల వస్తుంది. తాకడం, పనిముట్లు మరియు విత్తనాల ద్వారా వ్యాపిస్తుంది.",
            "symptoms": "ఆకులపై లేత మరియు ముదురు ఆకుపచ్చని చారల మచ్చలు, ఆకులు సన్నగా ముడుచుకుపోవడం.",
            "treatment": "చికిత్స లేదు. పనిముట్లను క్రిమిసంహారక ద్రావణంతో కడగాలి.",
            "organic": "తెగులు సోకిన మొక్కలను తీసివేసి తగులబెట్టాలి.",
            "prevention": "వైరస్ లేని విత్తనాలను వాడాలి మరియు తోటలో ధూమపానం చేయకూడదు."
        }
    }
}


def get_ui_text(key: str, lang: str = "en") -> str:
    """Retrieve UI string by key in requested language with English fallback."""
    lang_dict = STRINGS.get(lang, STRINGS["en"])
    return lang_dict.get(key, STRINGS["en"].get(key, key))


def get_crop_translation(crop_name: str, lang: str = "en") -> dict:
    """Retrieve translated crop details."""
    crop_key = crop_name.lower().strip()
    crop_info = CROPS_I18N.get(crop_key, {})
    
    if not crop_info:
        return {
            "name": crop_name.title(),
            "season": "Season data not available.",
            "soil": "Soil data not available.",
            "care": "Provide regular care, balanced NPK nutrients, and appropriate irrigation."
        }
    
    return crop_info.get(lang, crop_info.get("en", {
        "name": crop_name.title(),
        "season": "Season data not available.",
        "soil": "Soil data not available.",
        "care": "Provide regular care, balanced NPK nutrients, and appropriate irrigation."
    }))


def get_disease_translation(disease_name: str, lang: str = "en") -> dict:
    """Retrieve translated disease details with fallback."""
    disease_info = DISEASES_I18N.get(disease_name, {})
    
    if not disease_info:
        # Case-insensitive fallback lookup
        for d_key, data in DISEASES_I18N.items():
            if d_key.lower() == disease_name.lower():
                disease_info = data
                break
                
    if not disease_info:
        is_healthy = "healthy" in disease_name.lower()
        return {
            "name": disease_name,
            "crop": disease_name.split(" - ")[0] if " - " in disease_name else "Plant",
            "status": "Healthy" if is_healthy else "Diseased",
            "cause": "No pathogen detected." if is_healthy else "Pathogen information pending confirmation.",
            "symptoms": "Clean foliage." if is_healthy else "Visible leaf abnormalities observed.",
            "treatment": "No treatment required." if is_healthy else "Consult local agricultural extension.",
            "organic": "Maintain balanced organic nutrition." if is_healthy else "Use neem-based bio-pesticide.",
            "prevention": "Regular scouting and balanced fertilization."
        }
        
    return disease_info.get(lang, disease_info.get("en", {}))
