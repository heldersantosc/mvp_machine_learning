from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Carrega o modelo com pickle
with open("app/classificador_obesidade.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Recebe os dados do POST em formato JSON
        data = request.get_json()

        # Faz a previsão usando o modelo carregado
        prediction = model.predict([data])

        # Retorna a previsão como JSON
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
