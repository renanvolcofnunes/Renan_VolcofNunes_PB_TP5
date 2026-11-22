import os
import requests
import streamlit as st

API_URL = os.getenv("EMPREGABILIDADE_API_URL", "http://127.0.0.1:8000")

st.title("Conversa sobre Empregabilidade Jovem")
st.write("Converse com o modelo local utilizando os dados do projeto.")

if "historico_conversa" not in st.session_state: st.session_state.historico_conversa = []

for mensagem in st.session_state.historico_conversa:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

pergunta = st.chat_input("Digite sua pergunta:")

if pergunta:
    st.session_state.historico_conversa.append({"role": "user", "content": pergunta})

    with st.chat_message("user"):
        st.write(pergunta)

    try:
        resposta = requests.post(f"{API_URL}/conversa", json={"pergunta": pergunta, "historico": st.session_state.historico_conversa[:-1]}, timeout=120)

        if resposta.ok:
            dados = resposta.json()
            st.session_state.historico_conversa.append({"role": "assistant", "content": dados["resposta"]})

            with st.chat_message("assistant"):
                st.write(dados["resposta"])
                st.caption(f'Modelo: {dados["modelo"]}')
        elif resposta.status_code == 503:
            st.error("O modelo local não está disponível.")
        else:
            st.error(f"Erro da API: {resposta.status_code}")

    except requests.RequestException:
        st.warning("A API não está disponível. Execute o FastAPI com Uvicorn.")

if st.button("Limpar conversa"):
    st.session_state.historico_conversa = []
    st.rerun()
