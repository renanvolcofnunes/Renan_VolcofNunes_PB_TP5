# Project Charter - Empregabilidade Jovem no Brasil

## Problema de Negócio

A inserção de jovens no mercado de trabalho brasileiro apresenta diferenças entre estados e regiões. O projeto organiza dados de empregabilidade jovem e conteúdos complementares para facilitar a consulta, comparação e interpretação dessas informações.

## Objetivo Geral

Desenvolver uma aplicação interativa que demonstre o ciclo completo de Ciência de Dados, integrando coleta, processamento, análise, visualização e uso de um modelo de linguagem local para gerar respostas contextualizadas sobre empregabilidade jovem no Brasil.

## Objetivos Específicos

- Comparar indicadores entre estados e regiões.
- Apresentar notícias relacionadas à empregabilidade jovem.
- Disponibilizar dados por meio de uma API FastAPI.
- Integrar Streamlit e FastAPI por requisições HTTP.
- Utilizar dados coletados por Web Scraping e Selenium.
- Processar textos com um modelo LLM executado localmente.
- Implementar memória conversacional.
- Manter o contexto ao longo de várias interações.
- Utilizar os dados do projeto como contexto para as respostas.
- Evitar a geração de indicadores e valores não presentes nos dados disponíveis.

## Escopo do TP5

O TP5 amplia o projeto com memória conversacional utilizando o modelo local Qwen/Qwen2.5-1.5B-Instruct.

A aplicação possui uma página de conversa em Streamlit e uma rota POST /conversa no FastAPI.

O histórico das interações é mantido no session_state do Streamlit e reenviado à API nas novas perguntas. O modelo utiliza uma janela de até 20 mensagens anteriores.

Os indicadores estruturados e as notícias coletadas por Web Scraping são adicionados ao contexto enviado ao modelo.

## Fontes de Dados

- IBGE / SIDRA.
- Agência Brasil.
- Painel das Juventudes da Bahia.
- Arquivos CSV processados pela aplicação.

## Tecnologias Utilizadas

- Python
- Streamlit
- FastAPI
- PyTorch
- Transformers
- Qwen/Qwen2.5-1.5B-Instruct
- Requests
- BeautifulSoup
- Selenium
- Git e GitHub

## Ciclo de Ciência de Dados

1. Coleta de indicadores e conteúdos externos.
2. Organização e processamento dos dados.
3. Disponibilização dos dados no dashboard e na API.
4. Integração dos dados ao contexto do modelo local.
5. Interação conversacional com memória.
6. Geração de respostas e insights a partir das informações disponíveis.

## Memória Conversacional

A memória é implementada por meio do histórico de mensagens armazenado no Streamlit.

Cada nova pergunta envia para a API as mensagens anteriores da conversa. O modelo recebe esse histórico junto com os dados do projeto, permitindo recuperar informações mencionadas anteriormente.

Foi realizado um teste com 10 interações. Na primeira interação foi informado que o estado de interesse era Bahia e, na última, o modelo conseguiu recuperar corretamente essa informação.

## Relação com o Problema de Negócio

A memória conversacional facilita a exploração dos dados porque permite que o usuário faça perguntas sucessivas sem precisar repetir todo o contexto.

Os indicadores permitem observar diferenças de empregabilidade entre estados e regiões, enquanto as notícias complementam a análise com conteúdos relacionados ao tema.

A solução contribui para transformar dados coletados em informações mais acessíveis para análise e interpretação.

## Critérios de Sucesso

- Navegação simples pelo dashboard.
- Consulta e comparação dos indicadores.
- Comunicação entre Streamlit e FastAPI.
- Execução local do modelo.
- Memória funcionando entre diferentes interações.
- Utilização dos dados do projeto no contexto das respostas.
- Respostas em português e sem criação de valores não disponíveis.
- Visualizações e informações organizadas de forma clara.
