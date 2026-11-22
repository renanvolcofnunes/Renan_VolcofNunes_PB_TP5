import os
import requests
import streamlit as st

API_URL = os.getenv("EMPREGABILIDADE_API_URL", "http://127.0.0.1:8000")

st.title("Analisador com LLM Local")
st.write("Envie um texto sobre empregabilidade jovem para processamento pelo modelo local.")

texto = st.text_area("Texto:", height=180)

if st.button("Processar texto"):
    if len(texto.strip()) < 20:
        st.warning("Digite um texto com pelo menos 20 caracteres.")
    else:
        try:
            resposta = requests.post(f"{API_URL}/processar_texto", json={"texto": texto}, timeout=120)

            if resposta.ok:
                dados = resposta.json()
                st.success("Texto processado com sucesso!")
                st.subheader("Resumo")
                st.write(dados["resultado"])
                st.caption(f'Modelo: {dados["modelo"]}')
            elif resposta.status_code == 503:
                st.error("O modelo LLM não está disponível.")
            elif resposta.status_code == 422:
                st.error("O texto enviado não atende aos requisitos.")
            else:
                st.error(f"Erro da API: {resposta.status_code}")

        except requests.RequestException:
            st.warning("A API não está disponível. Execute o FastAPI com Uvicorn.")
