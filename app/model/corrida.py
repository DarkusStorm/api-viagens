# Modelo da Tabela "Corrida" para o banco de dados;

from sqlalchemy import VARCHAR, Numeric, BigInteger, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class CorridaModel(Base):
    __tablename__ = "corrida"

    id_corrida: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True, autoincrement=True)
    id_passageiro: Mapped[int] = mapped_column(BigInteger, ForeignKey('passageiro.id_passageiro', ondelete="CASCADE"), unique=True, nullable=False)
    id_motorista: Mapped[int] = mapped_column(BigInteger, ForeignKey('motorista.id_motorista', ondelete="CASCADE"), unique=True, nullable=False)
    id_servico: Mapped[int] = mapped_column(Integer, ForeignKey('servico.id_servico', ondelete="CASCADE"), unique=True, nullable=False)
    id_avaliacao: Mapped[int] = mapped_column(BigInteger, ForeignKey('avaliacao.id_avaliacao', ondelete="CASCADE"), unique=True, nullable=False)

    datahora_inicio: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    datahora_fim: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    
    local_partida: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    local_destino: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    
    valor_estimado: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    
    status: Mapped[Enum] = mapped_column(Enum("Pendente", "Em andamento", "Concluída", "Cancelada"), default="Pendente", nullable=False)