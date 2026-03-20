TRANSLATIONS = {
    "en": {
        "title":      "🌾 Kisan Mitra | किसान मित्र",
        "best_crop":  "Best Crop for Your Farm",
        "fertilizer": "Fertilizer Recommendation",
        "tip":        "Farming Tip",
        "confidence": "Confidence",
        "alt_crops":  "Alternative Crops",
        "enter_farm": "Enter Farm Details",
        "soil":       "Soil",
        "weather":    "Weather",
        "location":   "Location",
    },
    "hi": {
        "title":      "🌾 किसान मित्र",
        "best_crop":  "आपकी फसल के लिए सर्वोत्तम फसल",
        "fertilizer": "उर्वरक अनुशंसा",
        "tip":        "खेती की सलाह",
        "confidence": "विश्वसनीयता",
        "alt_crops":  "वैकल्पिक फसलें",
        "enter_farm": "खेत की जानकारी दर्ज करें",
        "soil":       "मिट्टी",
        "weather":    "मौसम",
        "location":   "स्थान",
    },
    "mr": {
        "title":      "🌾 किसान मित्र",
        "best_crop":  "तुमच्या शेतासाठी सर्वोत्तम पीक",
        "fertilizer": "खत शिफारस",
        "tip":        "शेती टिप्स",
        "confidence": "विश्वासार्हता",
        "alt_crops":  "पर्यायी पिके",
        "enter_farm": "शेताचा तपशील भरा",
        "soil":       "माती",
        "weather":    "हवामान",
        "location":   "स्थान",
    },
}

def t(key: str, lang: str = "en") -> str:
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, key)
