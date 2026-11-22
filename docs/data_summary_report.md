# Data Summary Report - Empregabilidade Jovem no Brasil

## Visão Geral

O projeto utiliza dados estruturados e conteúdos textuais relacionados à empregabilidade jovem no Brasil.

Os dados são utilizados desde a etapa de coleta e preparação até a visualização no dashboard e o processamento pelo modelo de linguagem local.

## Indicadores de Empregabilidade

### Fonte

IBGE / SIDRA.

### Arquivo

data/sample/empregabilidade_jovem.csv

### Principais Campos

- uf
- estado
- regiao
- taxa_desocupacao

Os dados são utilizados em filtros, comparações, gráficos, consultas pela API e no contexto fornecido ao modelo local.

## Notícias sobre Empregabilidade

### Fonte

Agência Brasil.

### Arquivo

data/processed/noticias_empregabilidade.csv

As notícias são coletadas com Requests e BeautifulSoup e utilizadas como conteúdo complementar no projeto.

## Dados Recebidos pela API

A rota POST de notícias armazena registros em:

data/processed/noticias_api.csv

## Coleta Dinâmica

O Selenium acessa o Painel das Juventudes da Bahia e salva o conteúdo coletado em:

data/processed/painel_juventudes_trabalho.txt

## Processamento com Modelo Local

O projeto utiliza o modelo:

Qwen/Qwen2.5-1.5B-Instruct

O modelo é executado localmente com PyTorch e Transformers.

No TP5, além do processamento de textos, o modelo é utilizado em uma conversa com memória.

## Integração dos Dados com a Conversa

A função montar_contexto da API reúne os indicadores estruturados e as notícias coletadas por Web Scraping.

Esse contexto é enviado ao modelo junto com a pergunta atual e o histórico da conversa.

Os indicadores numéricos são tratados como dados estruturados do projeto. As notícias são utilizadas apenas como conteúdo complementar.

## Memória Conversacional

O histórico da conversa é armazenado no session_state do Streamlit.

A cada nova pergunta, o histórico é enviado para a rota POST /conversa.

O modelo recebe uma janela de até 20 mensagens anteriores, permitindo manter o contexto sem crescimento ilimitado da entrada.

Um teste com 10 interações confirmou que o modelo conseguiu recuperar, na última pergunta, uma informação fornecida na primeira interação.

## Controle das Respostas

O prompt orienta o modelo a utilizar exclusivamente o contexto fornecido pelo projeto e a não inventar indicadores, valores, fontes ou eventos.

Quando uma informação não estiver disponível no contexto, o modelo deve indicar que ela não está presente nos dados fornecidos.

Também foi adicionada uma limpeza de caracteres estrangeiros inesperados na resposta do modelo.

## Ambiente de Execução

- Python 3.14.0
- Streamlit 1.62.0
- FastAPI 0.165.0
- PyTorch 2.15.0+cpu
- Transformers 5.24.0
- Execução em CPU
- RAM disponível no ambiente: aproximadamente 15,91 GB
- Modelo local: aproximadamente 3,10 GB

## Ciclo de Ciência de Dados

1. Coleta dos indicadores e conteúdos externos.
2. Processamento e armazenamento dos dados.
3. Consulta e visualização no dashboard.
4. Disponibilização por API.
5. Integração dos dados ao contexto do LLM.
6. Interação com memória conversacional.
7. Geração de respostas contextualizadas.

## Qualidade e Limitações

Os indicadores estruturados são a principal referência quantitativa do projeto.

As notícias coletadas possuem finalidade complementar.

O modelo pode apresentar limitações próprias de modelos generativos. Por isso, o prompt restringe as respostas aos dados fornecidos.

O tempo de resposta depende do hardware, pois o modelo é executado localmente em CPU.

O histórico utilizado pelo modelo é limitado às últimas 20 mensagens.
