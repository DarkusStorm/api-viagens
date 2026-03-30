from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.motorista_veiculo import MotoristaVeiculoModel
from app.schema.motorista_veiculo import MotoristaVeiculoSchema, MotoristaVeiculoUpdateSchema

motorista_veiculo = APIRouter()

@motorista_veiculo.post("/")
async def criar_motorista_veiculo(dados: MotoristaVeiculoSchema, db: Session = Depends(get_db)):
    novo_motorista_veiculo = MotoristaVeiculoModel(**dados.model_dump())
    db.add(novo_motorista_veiculo)
    db.commit()
    db.refresh(novo_motorista_veiculo)
    return novo_motorista_veiculo

@motorista_veiculo.get("/motoristas_veiculo")
async def listar_motoristas_veiculo(db: Session = Depends(get_db)):
    return db.query(MotoristaVeiculoModel).all()

@motorista_veiculo.get("/motoristas_veiculo/{id}")
async def buscar_motorista_veiculo(id_motorista: int, id_veiculo: int, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id_motorista == id_motorista and MotoristaVeiculoModel.id_veiculo == id_veiculo).first()

    if not motorista_veiculo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Motorista-Veículo com ID de Motorista {id_motorista} e ID de Veículo {id_veiculo} não encontrado."
        )

    return motorista_veiculo

@motorista_veiculo.delete("/motoristas_veiculo/{id_motorista}/{id_veiculo}/delete")
async def deletar_motorista_veiculo(id_motorista: int, id_veiculo: int, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id_motorista == id_motorista and MotoristaVeiculoModel.id_veiculo == id_veiculo).first()

    if not motorista_veiculo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Motorista-Veículo com ID de Motorista {id_motorista} e ID de Veículo {id_veiculo} não encontrado."
        )
    
    db.delete(motorista_veiculo)
    db.commit()
    return {
        "resposta": f"Motorista-Veículo com ID de Motorista {id_motorista} e ID de Veículo {id_veiculo} apagado com sucesso.",
        "motoristas-veiculo": db.query(MotoristaVeiculoModel).all()
    }

@motorista_veiculo.put("/motoristas_veiculo/{id_motorista}/{id_veiculo}/update")
async def atualizar_motorista_veiculo(id_motorista: int, id_veiculo: int, dados: MotoristaVeiculoUpdateSchema, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id_motorista == id_motorista and MotoristaVeiculoModel.id_veiculo == id_veiculo).first()

    if not motorista_veiculo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Motorista-Veículo com ID de Motorista {id_motorista} e ID de Veículo {id_veiculo} não encontrado"
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (motorista_veiculo, campo, valor)

    db.commit()
    db.refresh(motorista_veiculo)

    return motorista_veiculo