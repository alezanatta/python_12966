
from typing import List
from datetime import date

from factory.engine import get_session
from models.produto import Produto
from schemas.produto import ProdutoOutput, ProdutoInput

session = get_session()


def get_produtos() -> List[ProdutoOutput]:
    results = session.query(Produto).all()
    produtos = []
    for r in results:
        produto = ProdutoOutput(
            cd_produto=r.cd_produto,
            nm_produto=r.nm_produto,
            dt_validade=r.dt_validade,
            tp_produto=r.tp_produto,
            preco=r.preco
        )
        produtos.append(produto)
    return produtos


def create_produto(r: ProdutoInput):
    produto = Produto(
        nm_produto=r.nm_produto,
        dt_validade=r.dt_validade,
        tp_produto=r.tp_produto,
        preco=r.preco
    )
    session.add(produto)
    session.commit()
