
from factory.engine import get_session
from models.carro import Carro


carro = Carro()
carro.nm_marca = "Chevrolet"
carro.nr_placa = "RHA-0001"
carro.nm_cor = "Laranja"


session = get_session()

session.add(carro)
session.commit()

session.close()
