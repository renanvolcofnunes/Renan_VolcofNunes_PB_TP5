import streamlit as st

st.title("Sobre o Projeto")

st.subheader("Fontes e Referências")

st.markdown("""
- [IBGE / SIDRA](https://sidra.ibge.gov.br/)
- [Ministério do Trabalho e Emprego](https://www.gov.br/trabalho-e-emprego/)
- [Agência Brasil](https://agenciabrasil.ebc.com.br/)
- [Painel das Juventudes da Bahia](https://infovis.sei.ba.gov.br/juventudes/)
""")

st.subheader("Evolução para o TP4")

st.write("O projeto integra Streamlit e FastAPI por requisições HTTP e utiliza um modelo de linguagem executado localmente para processamento de textos.")

st.write("A página Analisador LLM envia textos para a rota POST /processar_texto e apresenta o resultado retornado pelo modelo Qwen/Qwen2.5-1.5B-Instruct.")
