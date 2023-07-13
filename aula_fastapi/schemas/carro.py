
from pydantic import BaseModel


class CarroInput(BaseModel):
    cor: str
    modelo: str
    ano: int


class CarroOutput(BaseModel):
    cd_carro: int
    cor: str
    modelo: str
    ano: int
