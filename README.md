# Empregabilidade Jovem no Brasil - TP5

Projeto desenvolvido para a disciplina Projeto de Bloco: Inteligência Artificial Aplicada.

O TP5 amplia o projeto com memória conversacional utilizando um modelo LLM local e os dados coletados ao longo das etapas anteriores.

## Funcionalidade escolhida

Opção 1: Implementação de Memória Conversacional com LLMs.

A aplicação possui uma página de conversa em Streamlit e uma rota POST /conversa no FastAPI.

O histórico das mensagens é armazenado no session_state do Streamlit e reenviado à API em cada nova interação.

O modelo utiliza uma janela de até 20 mensagens anteriores para manter o contexto da conversa.

## Modelo LLM

Modelo: Qwen/Qwen2.5-1.5B-Instruct

- PyTorch 2.15.0+cpu
- Transformers 5.24.0
- FastAPI 0.165.0
- Streamlit 1.62.0
- Execução em CPU
- RAM do ambiente: aproximadamente 15,91 GB
- Modelo local: aproximadamente 3,10 GB

O modelo é executado localmente e carregado uma única vez durante a inicialização da API.

## Dados utilizados no contexto

A conversa utiliza dados já coletados e processados pelo projeto:

- indicadores de empregabilidade armazenados em data/sample/empregabilidade_jovem.csv;
- notícias coletadas por Web Scraping em data/processed/noticias_empregabilidade.csv;
- demais dados processados e visualizados no dashboard.

A função montar_contexto da API reúne essas informações antes de enviar a pergunta ao modelo.

## Controle das respostas

O prompt orienta o modelo a:

- utilizar somente o contexto fornecido;
- não inventar indicadores ou valores;
- diferenciar dados estruturados de notícias coletadas;
- informar quando uma resposta não estiver disponível nos dados.

Também foi adicionada uma limpeza de caracteres estrangeiros inesperados na resposta.

## Teste de memória

Foi realizado um teste com 10 interações consecutivas.

Na primeira interação foi informado que o estado de interesse principal era Bahia.

Na décima interação o modelo foi questionado sobre o estado mencionado no início e respondeu corretamente Bahia.

Esse teste demonstrou que a memória conversacional permaneceu disponível ao longo das interações.

## FastAPI

Executar:

```powershell
python -m uvicorn api.main:app
```

Rotas principais:

- GET /
- GET /saude
- GET /indicadores
- GET /indicadores/{uf}
- GET /noticias
- POST /noticias
- POST /processar_texto
- POST /conversa

## Streamlit

Executar em outro terminal:

```powershell
python -m streamlit run app.py
```

A página Conversa permite interagir com o modelo local mantendo o contexto entre perguntas sucessivas.

## Estrutura principal

- api/main.py - API FastAPI
- paginas/conversa.py - interface de conversa
- src/analisador_llm.py - carregamento e uso do modelo
- docs/project_charter.md - Project Charter atualizado
- docs/data_summary_report.md - Data Summary Report atualizado
- docs/escolha_do_modelo.md - justificativa do modelo local

## Ambiente Local

Criar e ativar o ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar as dependências:

```powershell
python -m pip install -r requirements-api.txt
python -m pip install -r requirements-coleta.txt
```

Caso o modelo ainda não esteja disponível localmente:

```powershell
python -m src.baixar_modelo
```

## Autor

Renan Volcof Nunes

## Alinhamento com ESG e ODS

A solução contribui para a dimensão social de ESG ao organizar e facilitar a análise de dados relacionados à empregabilidade jovem e às diferenças observadas entre estados e regiões.

O projeto também se relaciona aos ODS ao utilizar dados sobre trabalho e juventude para apoiar a interpretação da inserção dos jovens no mercado de trabalho.

Os indicadores estruturados fornecem a base quantitativa, as notícias coletadas complementam o contexto e a memória conversacional permite explorar essas informações em perguntas sucessivas.
