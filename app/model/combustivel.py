from sqlalchemy import Integer, VARCHAR, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class CombustivelModel(Base):
    __tablename__ = "combustivel"

    id_combustivel: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)

    descricao: Mapped[str] = mapped_column(VARCHAR(45))
    fator_carbono: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)