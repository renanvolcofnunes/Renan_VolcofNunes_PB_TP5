from huggingface_hub import snapshot_download

MODELO = "Qwen/Qwen2.5-1.5B-Instruct"
PASTA = "modelos/qwen2.5-1.5b-instruct"

print("Baixando modelo...")

snapshot_download(
    repo_id=MODELO,
    local_dir=PASTA
)

print("Modelo baixado com sucesso!")
print("Pasta:", PASTA)
