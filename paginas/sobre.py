import streamlit as st

st.title("Sobre o Projeto")

st.subheader("Empregabilidade Jovem no Brasil")

st.write("O projeto integra coleta, processamento, análise, visualização de dados e uso de um modelo de linguagem local para apoiar a interpretação de informações relacionadas à empregabilidade jovem.")

st.subheader("Ciclo de Ciência de Dados")

st.markdown("""
- Coleta e organização dos dados.
- Processamento dos indicadores e conteúdos textuais.
- Visualização em dashboard interativo.
- Disponibilização de dados por FastAPI.
- Processamento com modelo LLM local.
- Memória conversacional utilizando os dados do projeto.
""")

st.subheader("ESG e ODS")

st.write("No contexto do projeto, a relação com ESG está principalmente na dimensão social, por meio da análise de informações relacionadas à empregabilidade jovem e às diferenças entre estados e regiões.")

st.write("O alinhamento com os ODS ocorre pelo uso de dados sobre trabalho e juventude para apoiar a compreensão da inserção dos jovens no mercado de trabalho.")

st.subheader("Memória Conversacional")

st.write("A página Conversa utiliza o modelo local Qwen/Qwen2.5-1.5B-Instruct e mantém o contexto entre várias interações.")

st.write("Os indicadores estruturados e as notícias coletadas pelo projeto são utilizados como contexto para as respostas.")

st.subheader("Fontes e Referências")

st.markdown("""
- [IBGE / SIDRA](https://sidra.ibge.gov.br/)
- [Ministério do Trabalho e Emprego](https://www.gov.br/trabalho-e-emprego/)
- [Agência Brasil](https://agenciabrasil.ebc.com.br/)
- [Painel das Juventudes da Bahia](https://infovis.sei.ba.gov.br/juventudes/)
""")
