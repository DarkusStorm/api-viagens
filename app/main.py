from fastapi import FastAPI
from app.database import Base, engine
from app.route.avaliacao import avaliacao
from app.route.classe import classe
from app.route.combustivel import combustivel
from app.route.corrida import corrida
from app.route.metodo_pagamento import metodo_pagamento
from app.route.modelo import modelo
from app.route.motorista_veiculo import motorista_veiculo
from app.route.motorista import motorista
from app.route.pagamento import pagamento
from app.route.passageiro import passageiro
from app.route.servico import servico
from app.route.usuario import usuario
from app.route.veiculo import veiculo
from app.route.viagem import viagem

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(avaliacao, prefix="/avaliacao", tags=["Avaliações"])
app.include_router(classe, prefix="/classe", tags=["Classes"])
app.include_router(combustivel, prefix="/combustivel", tags=["Tipos de Combustível"])
app.include_router(corrida, prefix="/corrida", tags=["Corridas"])
app.include_router(metodo_pagamento, prefix="/metodo_pagamento", tags=["Métodos de Pagamento"])
app.include_router(modelo, prefix="/modelo", tags=["Modelos"])
app.include_router(motorista_veiculo, prefix="/motorista_veiculo", tags=["Vínculos Motorista-Veículo"])
app.include_router(motorista, prefix="/motorista", tags=["Motoristass"])
app.include_router(pagamento, prefix="/pagamento", tags=["Pagamentos"])
app.include_router(passageiro, prefix="/passageiro", tags=["Passageiros"])
app.include_router(servico, prefix="/servico", tags=["Serviços"])
app.include_router(usuario, prefix="/usuario", tags=["Usuários"])
app.include_router(veiculo, prefix="/veiculo", tags=["Veículos"])
app.include_router(viagem, prefix="/viagem", tags=["Viagens"])

@app.get("/")
async def health_check():
    return {"status": "API Online"}