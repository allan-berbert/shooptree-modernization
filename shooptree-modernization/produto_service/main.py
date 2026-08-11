from fastapi import FastAPI

app = FastAPI(
    title="ShoopTree - Serviço de Produtos",
    description="Microsserviço responsável pelo gerenciamento de produtos.",
    version="1.0.0"
)

produtos = []


@app.get("/produtos")
def listar_produtos():
    return produtos


@app.post("/produtos")
def cadastrar_produto(produto: dict):
    produtos.append(produto)
    return produto


@app.delete("/produtos")
def apagar_produtos():
    produtos.clear()
    return {"mensagem": "Todos os produtos foram removidos"}