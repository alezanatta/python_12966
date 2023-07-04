
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float

Base = declarative_base()


class Produto(Base):
    __tablename__ = "produto"

    cd_produto = Column("cd_produto", Integer, primary_key=True)
    nm_produto = Column("nm_produto", String(40))
    tp_produto = Column("tp_produto", String(40))
    dt_validade = Column("dt_validade", Date)
    preco = Column("preco", Float)
