import csv
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field, HttpUrl
from src.analisador_llm import carregar_modelo, processar_texto, conversar

BASE = Path(__file__).resolve().parent.parent
ARQUIVO = BASE / "data" / "sample" / "empregabilidade_jovem.csv"
ARQUIVO_NOTICIAS_API = BASE / "data" / "processed" / "noticias_api.csv"
ARQUIVO_NOTICIAS = BASE / "data" / "processed" / "noticias_empregabilidade.csv"

modelo_disponivel = False
erro_modelo = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global modelo_disponivel, erro_modelo

    try:
        carregar_modelo()
        modelo_disponivel = True
        erro_modelo = None
        print("Modelo LLM carregado com sucesso.")
    except Exception as erro:
        modelo_disponivel = False
        erro_modelo = str(erro)
        print("Falha ao carregar modelo:", erro_modelo)

    yield

app = FastAPI(
    title="API de Empregabilidade Jovem no Brasil",
    description="API para consulta de indicadores e processamento de textos com LLM local.",
    version="2.0",
    lifespan=lifespan
)

class NoticiaEntrada(BaseModel):
    titulo: str = Field(min_length=1)
    data: str = Field(min_length=1)
    url: HttpUrl
    fonte: str = Field(min_length=1)

class TextoEntrada(BaseModel):
    texto: str = Field(min_length=20)

class ResultadoAnalise(BaseModel):
    tipo_analise: str
    texto_original: str
    resultado: str
    modelo: str

class MensagemConversa(BaseModel):
    role: str
    content: str

class ConversaEntrada(BaseModel):
    pergunta: str = Field(min_length=2)
    historico: list[MensagemConversa] = Field(default_factory=list)

class ResultadoConversa(BaseModel):
    resposta: str
    modelo: str

def carregar_dados():
    dados = []

    with open(ARQUIVO, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            linha["taxa_desocupacao"] = float(linha["taxa_desocupacao"])
            dados.append(linha)

    return dados

def carregar_noticias_api():
    noticias = []

    if ARQUIVO_NOTICIAS_API.exists():
        with open(ARQUIVO_NOTICIAS_API, "r", encoding="utf-8-sig") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                noticias.append(linha)

    return noticias

@app.get("/", summary="Início")
def inicio():
    return {"mensagem": "API de Empregabilidade Jovem no Brasil"}

@app.get("/saude", summary="Verificar estado da API")
def saude():
    return {
        "api": "online",
        "modelo_llm": "carregado" if modelo_disponivel else "indisponivel",
        "erro_modelo": erro_modelo
    }

@app.get("/indicadores", summary="Consultar indicadores")
def indicadores(regiao: str | None = Query(default=None)):
    dados = carregar_dados()

    if regiao is not None:
        dados = [linha for linha in dados if linha["regiao"].lower() == regiao.lower()]

    return {"quantidade": len(dados), "dados": dados}

@app.get("/indicadores/{uf}", summary="Consultar indicador por UF")
def indicador_uf(uf: str):
    dados = carregar_dados()
    resultado = [linha for linha in dados if linha["uf"].upper() == uf.upper()]

    if not resultado:
        raise HTTPException(status_code=404, detail="UF não encontrada.")

    return {"uf": uf.upper(), "quantidade": len(resultado), "dados": resultado}

@app.get("/noticias", summary="Consultar notícias enviadas pela API")
def listar_noticias():
    noticias = carregar_noticias_api()
    return {"quantidade": len(noticias), "dados": noticias}

@app.post("/noticias", summary="Enviar nova notícia", status_code=201)
def adicionar_noticia(noticia: NoticiaEntrada):
    ARQUIVO_NOTICIAS_API.parent.mkdir(parents=True, exist_ok=True)
    arquivo_novo = not ARQUIVO_NOTICIAS_API.exists() or ARQUIVO_NOTICIAS_API.stat().st_size == 0

    with open(ARQUIVO_NOTICIAS_API, "a", encoding="utf-8-sig", newline="") as arquivo:
        campos = ["titulo", "data", "url", "fonte"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        if arquivo_novo:
            escritor.writeheader()

        escritor.writerow({
            "titulo": noticia.titulo,
            "data": noticia.data,
            "url": str(noticia.url),
            "fonte": noticia.fonte
        })

    return {"mensagem": "Notícia adicionada com sucesso.","dados": {"titulo": noticia.titulo, "data": noticia.data,
            "url": str(noticia.url), "fonte": noticia.fonte}}

@app.post("/processar_texto", response_model=ResultadoAnalise, summary="Processar texto com LLM local")
def analisar_texto(entrada: TextoEntrada):
    if not modelo_disponivel:
        raise HTTPException(status_code=503, detail="Modelo LLM indisponível.")

    try:
        resultado = processar_texto(entrada.texto)

        return ResultadoAnalise(
            tipo_analise="resumo",
            texto_original=entrada.texto,
            resultado=resultado,
            modelo="Qwen/Qwen2.5-1.5B-Instruct"
        )

    except Exception as erro:
        raise HTTPException(status_code=500, detail=f"Erro ao processar texto: {erro}")

@app.post("/conversa", response_model=ResultadoConversa, summary="Conversa com memória")
def rota_conversa(entrada: ConversaEntrada):
    if not modelo_disponivel: raise HTTPException(status_code=503, detail="Modelo LLM indisponível.")

    try:
        historico = [{"role": mensagem.role, "content": mensagem.content} for mensagem in entrada.historico]
        resposta = conversar(entrada.pergunta, historico, montar_contexto())
        return ResultadoConversa(resposta=resposta, modelo="Qwen/Qwen2.5-1.5B-Instruct")
    except Exception as erro:
        raise HTTPException(status_code=500, detail=f"Erro ao processar conversa: {erro}")



def montar_contexto():
    dados = carregar_dados()
    arquivo_noticias = BASE / "data" / "processed" / "noticias_empregabilidade.csv"
    noticias = []

    if arquivo_noticias.exists():
        with open(arquivo_noticias, "r", encoding="utf-8-sig") as arquivo:
            noticias = list(csv.DictReader(arquivo))

    indicadores = [f'{linha["uf"]} - {linha["estado"]} - {linha["regiao"]}: taxa de desocupação {linha["taxa_desocupacao"]}%' for linha in dados]
    noticias_texto = [f'{linha["titulo"]} | {linha["data"]} | {linha["fonte"]}' for linha in noticias]

    return "INDICADORES DO PROJETO:\n" + "\n".join(indicadores) + "\n\nNOTÍCIAS COLETADAS POR WEB SCRAPING:\n" + ("\n".join(noticias_texto) if noticias_texto else "Nenhuma notícia disponível.")
