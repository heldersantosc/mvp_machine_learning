from app.models import ObesityModel

model_path = "app/ml/classifier_model.pkl"
scaler_path = "app/ml/standard_scaler.pkl"

# Dados de exemplo para teste
test_data = {
    "Age": [30, 21],
    "Gender": [0, 1],
    "Height": [172, 155],
    "Weight": [119, 53],
    "BMI": [40.22, 22.94],
}


def test_predict_valid_output():
    model = ObesityModel(model_path, scaler_path)

    result = model.predict(test_data)
    assert isinstance(result, dict)
    assert "prediction" in result
    assert isinstance(result["prediction"], list)
    assert all(isinstance(pred, str) for pred in result["prediction"])


def test_predict_with_test_data():
    model = ObesityModel(model_path, scaler_path)

    result = model.predict(test_data)
    assert isinstance(result, dict)
    assert "prediction" in result
    assert isinstance(result["prediction"], list)
    assert all(isinstance(pred, str) for pred in result["prediction"])

    expected_predictions = ["obeso", "normal"]
    assert result["prediction"] == expected_predictions
