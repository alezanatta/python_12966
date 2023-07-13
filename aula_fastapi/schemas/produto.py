
from datetime import date
from enum import Enum

from pydantic import BaseModel


class TipoProduto(Enum):
    fruta = "Fruta"
    padaria = "padaria"
    acougue = "açougue"


class ProdutoInput(BaseModel):
    nm_produto: str
    tp_produto: TipoProduto
    dt_validade: date
    preco: float

    class Config:
        orm_mode = True


class ProdutoOutput(BaseModel):
    cd_produto: int
    nm_produto: str
    tp_produto: TipoProduto
    dt_validade: date
    preco: float

    class Config:
        orm_mode = True
