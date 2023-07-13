
from fastapi import FastAPI
from typing import List

from schemas.carro import CarroInput, CarroOutput
from schemas.produto import ProdutoInput, ProdutoOutput
from schemas.default_responses import StatusCodes

from dao.produto import get_produtos, create_produto

app = FastAPI()


@app.get("/")
def root():
    return "Meu primeiro endpoint!"


@app.get("/carro")
def carro(cd_carro: int = 0):
    """Busca e retorna uma lista com carros disponíveis"""
    return {
        "cd_carro": cd_carro,
        "cor": "laranja",
        "modelo": "Logan",
        "ano": 2014
    }


@app.get("/carros")
def carros():
    """Busca e retorna uma lista com carros disponíveis"""
    return {
        "cor": "laranja",
        "modelo": "Logan",
        "ano": 2014
    }


@app.post("/carro")
def cadastra_carro(carro: CarroInput) -> CarroOutput:
    return CarroOutput()


@app.get("/produtos")
def produtos() -> List[ProdutoOutput]:
    """Busca e retorna uma lista com todos os produtos"""
    produtos = get_produtos()
    return produtos


@app.post("/produtos")
def cadastra_produto(produto: ProdutoInput):
    """Cadastra um produto"""
    create_produto(produto)
    return {
        "status": StatusCodes.OK
    }
