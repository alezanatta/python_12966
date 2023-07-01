
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Carro(Base):
    __tablename__ = "carro"

    cd_carro = Column("cd_carro", Integer, primary_key=True)
    nm_marca = Column("nm_marca", String(50))
    nr_placa = Column("nr_placa", String(10))
    nm_cor = Column("nm_cor", String(10))
