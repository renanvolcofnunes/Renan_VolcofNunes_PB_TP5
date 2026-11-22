import streamlit as st

st.title("Empregabilidade Jovem no Brasil")

st.subheader("Problema de Negócio")

st.write("""
O projeto busca analisar informações relacionadas à empregabilidade jovem no Brasil, identificando diferenças entre estados e regiões e facilitando a interpretação dos indicadores disponíveis.
""")

st.subheader("Objetivos do Projeto")

st.markdown("""
- Comparar indicadores de empregabilidade jovem entre estados e regiões brasileiras.
- Identificar diferenças nos indicadores disponíveis.
- Apresentar notícias relacionadas à empregabilidade jovem.
- Integrar os dados coletados a uma API FastAPI.
- Utilizar um modelo local para processamento de textos.
- Permitir interação com memória conversacional utilizando os dados do projeto.
- Apresentar os resultados em um dashboard interativo.
""")

st.subheader("Navegação")

st.page_link("paginas/indicadores.py", label="Indicadores de Empregabilidade")
st.page_link("paginas/comparador.py", label="Comparador de Estados")
st.page_link("paginas/noticias.py", label="Notícias sobre Empregabilidade")
st.page_link("paginas/conversa.py", label="Conversa")
st.page_link("paginas/sobre.py", label="Sobre o Projeto")
