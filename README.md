# Empregabilidade Jovem no Brasil - TP4

Projeto desenvolvido para a disciplina Projeto de Bloco: Inteligência Artificial Aplicada.

O TP4 integra um modelo LLM local ao FastAPI para processamento de textos sobre empregabilidade jovem.

## Modelo LLM

Modelo: `Qwen/Qwen2.5-1.5B-Instruct`

- PyTorch 2.15.0+cpu
- Transformers 5.23.0
- HuggingFace Hub 2.4.0
- Execução em CPU
- RAM: 15,91 GB
- Download do modelo: aproximadamente 3,10 GB
- Inferência medida: aproximadamente 19,19 segundos

Baixar o modelo:

```powershell
python -m src.baixar_modelo
```

## FastAPI

Executar:

```powershell
python -m uvicorn api.main:app
```

Rotas principais:

- `GET /saude`
- `GET /indicadores`
- `GET /indicadores/{uf}`
- `GET /noticias`
- `POST /noticias`
- `POST /processar_texto`

A rota `POST /processar_texto` utiliza o LLM local e retorna uma resposta estruturada com Pydantic.

Erros tratados:

- HTTP 422 para entrada inválida.
- HTTP 503 quando o modelo está indisponível.
- HTTP 500 para falha no processamento.
- HTTP 404 para UF inexistente.

## Streamlit

Executar em outro terminal:

```powershell
python -m streamlit run app.py
```

A página **Analisador LLM** envia o texto ao FastAPI por HTTP e apresenta o resultado do modelo local.

## Documentação

A justificativa da escolha do modelo está em:

`docs/escolha_do_modelo.md`

## GitHub

https://github.com/renanvolcofnunes/Renan_VolcofNunes_PB_TP4

## Autor

Renan Volcof Nunes

## Ambiente Local

Ambiente utilizado:

- Python 3.14
- PyTorch 2.15.0+cpu
- Transformers 5.23.0
- HuggingFace Hub 2.4.0
- Execucao em CPU
- RAM: 15,91 GB

Criar e ativar o ambiente virtual:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Instalar as dependencias:

python -m pip install -r requirements-api.txt

Baixar o modelo local:

python -m src.baixar_modelo
