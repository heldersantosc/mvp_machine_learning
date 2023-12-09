from flask import Flask, request, jsonify
from app.models import ObesityModel

app = Flask(__name__)

# Instancia a classe ObesityModel
model = ObesityModel("app/ml/classifier_model.pkl", "app/ml/standard_scaler.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Recebe os dados do POST em formato JSON
        data = request.get_json()
        prediction = model.predict(data)

        # Retorna a previsão como JSON
        return jsonify(prediction)
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
