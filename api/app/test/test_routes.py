from app.routes import app
import json


def test_predict_route():
    test_client = app.test_client()

    # Dados de teste no formato JSON
    test_data = {
        "Age": [25],
        "Gender": [0],
        "Height": [155],
        "Weight": [53],
        "BMI": [22.94],
    }

    # Envia uma solicitação POST para a rota /predict
    response = test_client.post("/predict", json=test_data)

    # Verifica se a resposta foi bem-sucedida (código 200) e se a resposta é JSON
    assert response.status_code == 200
    assert response.content_type == "application/json"

    # Verifica se a resposta contém a chave 'prediction'
    data = json.loads(response.data)
    assert "prediction" in data

    expected_predictions = ["normal"]
    assert data["prediction"] == expected_predictions
