
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Produto(Base):
    __tablename__ = "produto"

    cd_produto = Column("cd_produto", Integer, primary_key=True)
    nm_produto = Column("nm_produto", String(50))
    tp_produto = Column("tp_produto", String(50))
    dt_validade = Column("dt_validade", Date)
    preco = Column("preco", Float)
