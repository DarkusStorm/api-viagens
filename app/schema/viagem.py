from pydantic import BaseModel
from typing import Optional

class ViagemSchema(BaseModel):
    id_viagem: int
    id_avaliacao: int
    id_corrida: int
    id_modelo: int
    id_motorista: int
    id_pagamento: int
    id_passageiro: int
    id_servico: int
    id_veiculo: int

    class Config:
        from_attributes = True

class ViagemUpdateSchema(BaseModel):
    id_viagem: Optional[int]
    id_avaliacao: Optional[int]
    id_corrida: Optional[int]
    id_modelo: Optional[int]
    id_motorista: Optional[int]
    id_pagamento: Optional[int]
    id_passageiro: Optional[int]
    id_servico: Optional[int]
    id_veiculo: Optional[int]