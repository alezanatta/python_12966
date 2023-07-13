
from factory.engine import get_session
from models.carro import Carro
from models.produto import Produto

from datetime import date


def insere_carro():
    carro = Carro()
    carro.nm_marca = "Chevrolet"
    carro.nr_placa = "RHA-0001"
    carro.nm_cor = "Laranja"

    session = get_session()

    session.add(carro)
    session.commit()

    session.close()


def insere_produto():
    produto = Produto()
    produto.nm_produto = "Abacate"
    produto.tp_produto = "Fruta"
    produto.dt_validade = date(day=30, month=6, year=2023)
    produto.preco = 10.50

    session = get_session()

    session.add(produto)
    session.commit()

    session.close()


def busca_produto_vencido():

    session = get_session()

    resultados = session.query(Produto) \
                        .filter(Produto.dt_validade < date.today())

    for r in resultados:
        print(r.nm_produto)


busca_produto_vencido()
