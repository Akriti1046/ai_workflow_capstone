from app.model import load_model, predict

def test_model_load():
    m = load_model()
    assert m is not None

def test_prediction_output_type():
    m = load_model()
    y = predict(m, [2, 200])
    assert isinstance(y, float)
