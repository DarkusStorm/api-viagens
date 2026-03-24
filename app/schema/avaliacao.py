from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class AvaliacaoSchema(BaseModel):
    
    id_avaliacao: int

    nota_passageiro: Optional[int]
    nota_motorista: Optional[int]
    datahora_limite: Optional[datetime]

    class Config:
        from_attributes = True

class AvaliacaoUpdateSchema(BaseModel):
    id_avaliacao: Optional[int]

    nota_passageiro: Optional[int]
    nota_motorista: Optional[int]
    datahora_limite: Optional[datetime]

    class Config:
        from_attributes = True