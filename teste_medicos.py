from models.medico import Medico
from models.consulta import Consulta
from models.paciente import Paciente
from models.utilizador import Utilizador
from utils.context_managers import sessao_db

with sessao_db() as sessao:
    medicos = sessao.query(Medico).all()
    print(f"Total: {len(medicos)}")
    for m in medicos:
        print(m)