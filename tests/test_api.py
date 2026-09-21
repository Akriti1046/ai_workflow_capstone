from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_predict_with_features_list():
    r = client.post("/predict", json={"features": [2, 200]})
    assert r.status_code == 200
    assert "prediction" in r.json()

def test_predict_with_named_fields():
    r = client.post("/predict", json={"feature1": 2, "feature2": 200})
    assert r.status_code == 200
    assert "prediction" in r.json()

def test_predict_all():
    r = client.get("/predict_all")
    assert r.status_code == 200
    data = r.json()
    assert "predictions" in data
    assert isinstance(data["predictions"], list)
