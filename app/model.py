import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path("models/model.pkl")

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Run train.py first.")
    return joblib.load(MODEL_PATH)

def predict(model, features):
    arr = np.array(features, dtype=float).reshape(1, -1)
    pred = model.predict(arr)[0]
    # Cast to float for JSON serialization
    try:
        return float(pred)
    except Exception:
        return float(pred.item())
