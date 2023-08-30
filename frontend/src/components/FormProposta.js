import React, { useEffect, useState } from "react";
import api from "../services/api";

import './FormProposta.css';

export default function FormProposta() {
    const [perguntas, setPerguntas] = useState([]);
    const [respostas, setRespostas] = useState({});

  useEffect(() => {
    api
      .get("/campo-proposta/")
      .then((response) => setPerguntas(response.data))
      .catch((err) => {
        console.error("ops! ocorreu um erro" + err);
      });
  }, []);
  
  const handleChange = (perguntaId, resposta) => {
    setRespostas(prevState => ({
      ...prevState,
      [perguntaId]: resposta,
    }));
  };

  const handleSubmit = async (e) => {
    console.log('Respostas:', respostas);
    const getNome = perguntas.map((pergunta) => {
        if (pergunta.nome === "Nome") {
          return pergunta.id;
        } else {
          return null;
        }})[0]
    const indiceDoObjeto = perguntas.findIndex(objeto => objeto.id === getNome);

    if (indiceDoObjeto !== -1) {
        perguntas.splice(indiceDoObjeto, 1);
    }
    const dadosFormatados = {
        "nome": respostas[getNome],
        "campos_valores": perguntas.map((pergunta) => ({
          "campo": pergunta.id,
          "texto": respostas[pergunta.id] || "",
        })),
    };
    console.log(getNome)
    console.log(dadosFormatados)
  
    try {
        const response = await api.post("/register/", dadosFormatados);
        console.log("Resposta da API:", response.data);
    } catch (error) {
        console.error("Erro ao enviar dados:", error);
    }
  };
  return (
    <div className="formulario-container">
      <h1>Faça Sua Proposta Aqui </h1>
      <form onSubmit={handleSubmit}>
        {perguntas.map(pergunta => (
          <div key={pergunta.id} className="pergunta-container">
            <p>{pergunta.nome}</p>
            <input
              type="text"
              value={respostas[pergunta.id] || ''}
              onChange={e => handleChange(pergunta.id, e.target.value)}
            />
          </div>
        ))}
        <button type="submit" onSubmit={e => handleSubmit(e)}>Enviar</button>
      </form>
    </div>
  );
}
