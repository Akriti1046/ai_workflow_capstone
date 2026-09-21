# AI Workflow: AI in Production — Capstone Template

This repository is a minimal, production-style ML project designed to satisfy Coursera peer-review criteria.
## Features
- FastAPI ML API
- Unit tests (API, model, logging)
- Dockerized deployment
- Model comparison
- Data ingestion pipeline
- EDA visualization
- Performance monitoring

## What’s included
- FastAPI API with `/predict` and `/predict_all`
- Model training with comparison (Linear Regression vs Random Forest)
- Logging (file-based) + basic latency monitoring
- Unit tests (API, model, logging)
- Single test runner script
- Data ingestion script
- Dockerfile
- Basic EDA/model comparison plot

## Quickstart

### 1) Install deps
```
pip install -r requirements.txt
```

### 2) Train model
```
python train.py
```

### 3) Run API
```
uvicorn app.main:app --reload
```

### 4) Try it
- Health: GET http://127.0.0.1:8000/
- Predict (list):
```
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"features":[2,200]}'
```
- Predict (named):
```
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"feature1":2,"feature2":200}'
```
- Predict all:
```
curl http://127.0.0.1:8000/predict_all
```

### 5) Run tests (single script)
```
bash run_tests.sh
```

## Docker
```
docker build -t ai-capstone .
docker run -p 8000:8000 ai-capstone
```

## Monitoring
- Logs written to `logs/app.log`
- Per-request latency logged

## Structure
```
app/
tests/
scripts/
models/
logs/
notebooks/
```

## Notes for grading
- Unit tests: API, model, logging ✔
- Single test command: `bash run_tests.sh` ✔
- Monitoring via logs ✔
- Data ingestion script ✔
- Multiple models compared ✔
- Visualization saved (`notebooks/model_comparison.png`) ✔
- Dockerized ✔
