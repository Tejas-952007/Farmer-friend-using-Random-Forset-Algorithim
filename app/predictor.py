import numpy as np
import joblib
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_model  = None
_scaler = None
_le     = None

SOIL_MAP = {"sandy": 0, "loamy": 1, "clay": 2}

def _load_models():
    """Lazy-load models only when needed (avoids crash on startup if models missing)."""
    global _model, _scaler, _le
    if _model is not None:
        return  # already loaded

    model_path  = os.path.join(BASE, "models", "random_forest_model.pkl")
    scaler_path = os.path.join(BASE, "models", "scaler.pkl")
    le_path     = os.path.join(BASE, "models", "label_encoder.pkl")

    missing = [p for p in [model_path, scaler_path, le_path] if not os.path.exists(p)]
    if missing:
        raise FileNotFoundError(
            "❌ Trained models not found! Please run first:\n\n"
            "  cd scripts && python train_model.py\n\n"
            f"Missing files: {[os.path.basename(p) for p in missing]}"
        )

    _model  = joblib.load(model_path)
    _scaler = joblib.load(scaler_path)
    _le     = joblib.load(le_path)


def predict_crop(N, P, K, temperature, humidity, ph, rainfall, soil_type: str):
    _load_models()
    soil_encoded = SOIL_MAP.get(soil_type.lower(), 1)
    raw    = np.array([[N, P, K, temperature, humidity, ph, rainfall, soil_encoded]])
    scaled = _scaler.transform(raw)
    probs  = _model.predict_proba(scaled)[0]
    top3   = np.argsort(probs)[::-1][:3]
    return [{"crop": _le.classes_[i], "confidence": round(probs[i]*100, 2)} for i in top3]
