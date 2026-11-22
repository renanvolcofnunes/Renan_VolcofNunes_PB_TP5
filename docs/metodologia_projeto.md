# Organização do Projeto — CRISP-DM e TDSP

## 1. Método CRISP-DM

### 1.1 Entendimento do Negócio

O projeto busca analisar informações relacionadas à empregabilidade jovem no Brasil, destacando diferenças entre estados e regiões e facilitando a interpretação dos indicadores disponíveis.

### 1.2 Entendimento dos Dados

Foram utilizados dados estruturados de empregabilidade e conteúdos textuais coletados em fontes públicas.

As informações foram avaliadas considerando estrutura, disponibilidade, cobertura e utilidade para o objetivo do projeto.

### 1.3 Preparação dos Dados

Os dados foram organizados, padronizados e preparados para uso no dashboard, nas consultas da API e no contexto fornecido ao modelo local.

### 1.4 Modelagem e Análise

Os indicadores foram organizados e comparados entre estados e regiões.

Também foram utilizados conteúdos coletados por Web Scraping como informação complementar.

O modelo local Qwen/Qwen2.5-1.5B-Instruct foi integrado ao projeto para processamento de textos e memória conversacional.

### 1.5 Avaliação

A solução foi testada por meio da navegação no dashboard, consultas à API, processamento de textos e interações conversacionais.

Foi realizado um teste com 10 interações consecutivas, no qual o modelo conseguiu recuperar ao final uma informação fornecida no início da conversa.

### 1.6 Implantação

O dashboard é executado com Streamlit e a API com FastAPI.

O modelo é executado localmente e carregado durante a inicialização da API.

## 2. Aplicação do TDSP

### 2.1 Business Understanding

O problema de negócio está relacionado à compreensão da empregabilidade jovem e das diferenças observadas entre estados e regiões.

### 2.2 Data Acquisition and Understanding

Os dados do projeto foram obtidos por arquivos estruturados, coleta Web e integração com API.

### 2.3 Modeling

Os dados são utilizados em comparações, visualizações e no contexto enviado ao modelo local.

A memória conversacional permite que o usuário faça perguntas sucessivas mantendo informações mencionadas anteriormente.

### 2.4 Deployment

A solução utiliza Python, Streamlit e FastAPI, com modelo LLM executado localmente.

### 2.5 Customer Acceptance

A aplicação deve permitir navegação simples, consulta dos indicadores, comparação entre estados, visualização das notícias e interação conversacional com contexto.

## 3. Relação com ESG e ODS

O projeto se relaciona principalmente à dimensão social de ESG ao organizar informações relacionadas à empregabilidade jovem.

O alinhamento com os ODS ocorre pelo uso de dados sobre trabalho e juventude para apoiar a interpretação da inserção dos jovens no mercado de trabalho e das diferenças regionais observadas.

## 4. Relação entre CRISP-DM e TDSP

O Entendimento do Negócio do CRISP-DM corresponde ao Business Understanding do TDSP.

As etapas de Entendimento e Preparação dos Dados se relacionam ao Data Acquisition and Understanding.

A etapa de Modelagem corresponde ao Modeling.

As etapas de Avaliação e Implantação se relacionam a Deployment e Customer Acceptance.

Dessa forma, as duas metodologias ajudam a organizar o ciclo completo do projeto, desde a definição do problema até a apresentação e utilização da solução.
