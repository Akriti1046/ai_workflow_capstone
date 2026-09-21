from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import time

from app.model import load_model, predict
from app.logger import get_logger

app = FastAPI(title="AI Workflow Capstone API")

class PredictRequest(BaseModel):
    features: Optional[List[float]] = None
    feature1: Optional[float] = None
    feature2: Optional[float] = None

# Load once at startup
try:
    model = load_model()
except Exception:
    model = None

logger = get_logger()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_endpoint(req: PredictRequest):
    global model
    if model is None:
        # Attempt lazy load if not available yet
        model = load_model()

    # Support both {"features": [...]} and {"feature1": x, "feature2": y}
    if req.features is not None:
        features = req.features
    elif req.feature1 is not None and req.feature2 is not None:
        features = [req.feature1, req.feature2]
    else:
        raise HTTPException(status_code=400, detail="Provide 'features' or 'feature1' and 'feature2'.")

    start = time.time()
    try:
        result = predict(model, features)
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    end = time.time()

    logger.info(f"Prediction: {result}")
    logger.info(f"Latency: {end - start}")

    return {"prediction": float(result)}

@app.get("/predict_all")
def predict_all():
    global model
    if model is None:
        model = load_model()

    # Simulated batch (e.g., multiple countries)
    samples = [[1, 100], [2, 200], [3, 300]]
    results = []
    for s in samples:
        try:
            results.append(float(predict(model, s)))
        except Exception as e:
            logger.error(f"Batch prediction error: {e}")
            results.append(None)
    return {"predictions": results}
