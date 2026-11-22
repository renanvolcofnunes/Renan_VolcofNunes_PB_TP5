from pathlib import Path
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

BASE = Path(__file__).resolve().parent.parent
PASTA_MODELO = BASE / "modelos" / "qwen2.5-1.5b-instruct"

tokenizer = None
modelo = None

def carregar_modelo():
    global tokenizer, modelo
    if not PASTA_MODELO.exists(): raise RuntimeError("Modelo local não encontrado. Execute python -m src.baixar_modelo.")

    tokenizer = AutoTokenizer.from_pretrained(PASTA_MODELO, local_files_only=True)
    modelo = AutoModelForCausalLM.from_pretrained(PASTA_MODELO, local_files_only=True, dtype=torch.float32)
    modelo.eval()

def processar_texto(texto):
    if modelo is None or tokenizer is None:
        raise RuntimeError("Modelo não carregado.")

    mensagens = [
        {"role": "system", "content": "Você analisa textos relacionados à empregabilidade jovem no Brasil. Responda em português de forma objetiva."},
        {"role": "user", "content": f"Resuma o texto abaixo destacando as informações principais:\n\n{texto}"}
    ]

    prompt = tokenizer.apply_chat_template(mensagens, tokenize=False, add_generation_prompt=True)
    entradas = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        saida = modelo.generate(**entradas, max_new_tokens=150, do_sample=False, pad_token_id=tokenizer.eos_token_id)

    resposta = saida[0][entradas["input_ids"].shape[1]:]
    return limpar_resposta(tokenizer.decode(resposta, skip_special_tokens=True))



def conversar(pergunta, historico, contexto):
    if modelo is None or tokenizer is None: raise RuntimeError("Modelo não carregado.")

    mensagens = [{"role": "system", "content": f"Você responde perguntas sobre empregabilidade jovem no Brasil usando exclusivamente o contexto fornecido pelo projeto. Responda em português, de forma objetiva. Não invente indicadores, valores, fontes, eventos ou conclusões. Os indicadores numéricos pertencem aos dados estruturados do projeto. As notícias coletadas por web scraping são apenas conteúdo complementar. Se uma informação não estiver no contexto, diga que ela não está disponível nos dados fornecidos. Contexto do projeto:\n\n{contexto}"}]

    for mensagem in historico[-20:]:
        if mensagem["role"] in ["user", "assistant"]: mensagens.append({"role": mensagem["role"], "content": mensagem["content"]})

    mensagens.append({"role": "user", "content": pergunta})

    prompt = tokenizer.apply_chat_template(mensagens, tokenize=False, add_generation_prompt=True)
    entradas = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        saida = modelo.generate(**entradas, max_new_tokens=180, do_sample=False, pad_token_id=tokenizer.eos_token_id)

    resposta = saida[0][entradas["input_ids"].shape[1]:]
    return limpar_resposta(tokenizer.decode(resposta, skip_special_tokens=True))




def limpar_resposta(texto):
    return re.sub(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af]', '', texto).strip()

