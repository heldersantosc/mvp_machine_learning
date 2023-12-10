from flask import Flask, request, jsonify
from flask_cors import CORS

from app.models import BMI_Calculator, ObesityModel


app = Flask(__name__)
cors = CORS(app)

# Instancia a classe ObesityModel
model = ObesityModel("app/ml/classifier_model.pkl", "app/ml/standard_scaler.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Recebe os dados do POST em formato JSON
        data = request.get_json()

        data["bmi"] = BMI_Calculator.calculate_batch(data["weight"], data["height"])

        prediction = model.predict(data)

        # Retorna a previsão como JSON
        return jsonify(prediction)
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
