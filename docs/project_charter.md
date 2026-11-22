# Project Charter - Empregabilidade Jovem no Brasil

## Problema de Negócio

A inserção de jovens no mercado de trabalho brasileiro apresenta diferenças entre estados e regiões. O projeto organiza e apresenta dados relacionados à empregabilidade jovem de forma acessível, permitindo a comparação de indicadores e o acompanhamento de informações complementares.

## Objetivo Geral

Desenvolver uma aplicação interativa para consulta e comparação de indicadores de empregabilidade jovem no Brasil, integrando dados públicos, coleta Web, API própria e processamento de textos com modelo de linguagem local.

## Objetivos Específicos

- Comparar indicadores entre estados e regiões.
- Apresentar notícias relacionadas à empregabilidade jovem.
- Disponibilizar dados por meio de uma API FastAPI.
- Integrar Streamlit e FastAPI por requisições HTTP.
- Utilizar Web Scraping e Selenium.
- Processar textos com um modelo LLM executado localmente.
- Retornar respostas estruturadas e tratar erros da API.

## Escopo do TP4

O TP4 amplia o projeto com:

- Modelo local `Qwen/Qwen2.5-1.5B-Instruct`.
- Download separado do modelo.
- Execução local com PyTorch e Transformers.
- Rota `POST /processar_texto`.
- Validação de entrada com Pydantic.
- Response Model para o resultado.
- Tratamento de erros HTTP 404, 422, 500 e 503.
- Página Streamlit para envio e processamento de textos.

## Fontes de Dados

- IBGE / SIDRA.
- Agência Brasil.
- Painel das Juventudes da Bahia.
- Arquivos CSV utilizados pela aplicação.

## Tecnologias Utilizadas

- Python
- Streamlit
- FastAPI
- PyTorch
- Transformers
- HuggingFace Hub
- Requests
- BeautifulSoup
- Selenium
- Git e GitHub

## Integração com o Modelo Local

O modelo é armazenado na pasta `modelos/qwen2.5-1.5b-instruct` e carregado localmente pela API.

A rota `POST /processar_texto` recebe um texto, realiza o processamento e retorna o resultado em formato estruturado.

A aplicação Streamlit possui a página **Analisador LLM**, que envia o texto por HTTP ao FastAPI e apresenta o resumo produzido pelo modelo.

## Critérios de Sucesso

O projeto será considerado bem-sucedido quando permitir:

- Navegação entre as páginas.
- Consulta e comparação de indicadores.
- Comunicação entre Streamlit e FastAPI.
- Execução local do modelo.
- Processamento de texto pela rota da API.
- Respostas estruturadas.
- Tratamento adequado de erros.
