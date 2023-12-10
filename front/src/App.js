import "./App.css";

import axios from "axios";
import React, { useState } from "react";

const URL = "http://localhost:5000/predict";

const App = () => {
  const [BMI, setBMI] = useState("-");
  const [error, setError] = useState(false);
  const [formData, setFormData] = useState({
    age: [],
    gender: [],
    height: [],
    weight: [],
  });

  const handleSubmit = async (e) => {
    try {
      e.preventDefault();
      const response = await axios.post(URL, formData);
      setBMI(response.data.prediction[0]);
      setError(false);
    } catch (error) {
      setError(true);
      console.error("Erro na requisição:", error.message);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: [Number(value)] });
  };

  return (
    <div className="container">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="age">Idade</label>
          <input
            min={1}
            type="number"
            name="age"
            value={formData.age}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="gender">Sexo</label>
          <select name="gender" value={formData.gender} onChange={handleChange}>
            <option value="" />
            <option value={0}>Masculino</option>
            <option value={1}>Feminino</option>
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="height">Altura (cm)</label>
          <input
            min={1}
            step={0.01}
            type="number"
            name="height"
            placeholder="0.00"
            value={formData.height}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="weight">Peso</label>
          <input
            min={1}
            step={0.01}
            type="number"
            name="weight"
            placeholder="0.00"
            value={formData.weight}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="BMI">Predição de classificação</label>
          <input
            type="text"
            name="BMI"
            placeholder="BMI"
            value={BMI.toUpperCase()}
            readOnly
            disabled
          />
        </div>
        <button className="button" type="submit">
          Verificar
        </button>
      </form>
      <h5 className="error" hidden={!error}>
        Erro ao realizar classificação!
      </h5>
    </div>
  );
};

export default App;
