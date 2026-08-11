from fastapi import FastAPI

app = FastAPI(
    title="ShoopTree - Serviço de Pagamentos",
    description="Microsserviço responsável pelo gerenciamento de pagamentos.",
    version="1.0.0"
)

pagamentos = []


@app.get("/pagamentos")
def listar_pagamentos():
    return pagamentos


@app.post("/pagamentos")
def cadastrar_pagamento(pagamento: dict):
    pagamentos.append(pagamento)
    return pagamento