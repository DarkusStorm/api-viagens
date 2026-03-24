from typing import Optional
from pydantic import BaseModel

class ClasseSchema (BaseModel):
    id_classe: int

    nome_classe: str
    fator_preco: float
    
    class Config:
        from_attributes = True

class ClasseUpdateSchema (BaseModel):
    id_classe: Optional[int]

    nome_classe: Optional[str]
    fator_preco: Optional[float]

    class Config:
        from_attributes = True