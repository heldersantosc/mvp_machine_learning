# models.py

import pandas as pd
import pickle


class ObesityModel:
    def __init__(self, model_url, scaler_url):
        self.attributes = ["Age", "Gender", "Height", "Weight", "BMI"]

        with open(model_url, "rb") as file:
            self.model = pickle.load(file)

        with open(scaler_url, "rb") as file:
            self.scaler = pickle.load(file)

    def predict(self, data):
        try:
            # Cria um dataframe
            new_entries = pd.DataFrame(data, columns=self.attributes)

            # Seleciona somente os valores
            array_new_entries = new_entries.values
            X_entries = array_new_entries[:, :].astype(float)

            # Padroniza com o scaler previamente treinado
            entries_rescaled_X = self.scaler.transform(X_entries)

            # Realiza a predição baseado no modelo
            prediction = self.model.predict(entries_rescaled_X)

            # Mapeamento dos dados
            obesity_map = {
                0: "abaixo do peso",
                1: "normal",
                2: "acima do peso",
                3: "obeso",
            }

            # Cria uma lista com o resultado em texto
            prediction_response = [obesity_map[val] for val in prediction]

            return {"prediction": prediction_response}
        except Exception as e:
            return {"error": str(e)}
