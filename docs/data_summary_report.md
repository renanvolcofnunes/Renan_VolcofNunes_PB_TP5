# Data Summary Report - Empregabilidade Jovem no Brasil

## Visão Geral

O projeto utiliza dados estruturados e conteúdos textuais relacionados à empregabilidade jovem no Brasil.

## Indicadores de Empregabilidade

### Fonte

IBGE / SIDRA.

### Arquivo

`data/sample/empregabilidade_jovem.csv`

### Principais Campos

- `uf`
- `estado`
- `regiao`
- `taxa_desocupacao`

Os dados são utilizados para filtros, comparações, gráficos e consultas pela API FastAPI.

## Notícias sobre Empregabilidade

### Fonte

Agência Brasil.

### Arquivo

`data/processed/noticias_empregabilidade.csv`

As notícias são coletadas com Requests e BeautifulSoup.

## Dados Recebidos pela API

A rota POST de notícias armazena os registros em:

`data/processed/noticias_api.csv`

## Coleta Dinâmica

O Selenium acessa o Painel das Juventudes da Bahia e salva o conteúdo coletado em:

`data/processed/painel_juventudes_trabalho.txt`

## Processamento de Texto com Modelo Local

O TP4 utiliza o modelo:

`Qwen/Qwen2.5-1.5B-Instruct`

O modelo é executado localmente e recebe textos enviados pela aplicação Streamlit.

A rota:

`POST /processar_texto`

retorna:

- tipo de análise;
- texto original;
- resultado;
- modelo utilizado.

O processamento atual realiza resumo de textos relacionados à empregabilidade jovem.

## Ambiente de Execução

- PyTorch 2.15.0+cpu
- Transformers 5.23.0
- Execução em CPU
- RAM do ambiente testado: 15,91 GB
- Modelo local: aproximadamente 3,10 GB
- Tempo de inferência medido: aproximadamente 19,19 segundos

## Qualidade e Limitações

Os indicadores do IBGE são a principal referência quantitativa.

As notícias e os conteúdos coletados na Web possuem finalidade complementar.

O tempo de processamento do modelo depende do hardware disponível.

O modelo precisa estar previamente baixado para que a rota de processamento esteja disponível.
