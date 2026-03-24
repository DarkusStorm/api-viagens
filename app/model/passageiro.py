from sqlalchemy import BigInteger, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.model.usuario import UsuarioModel

class PassageiroModel(UsuarioModel):
    __tablename__ = "passageiro"

    id_passageiro: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True, autoincrement=True)
    id_usuario: Mapped[int] = mapped_column(BigInteger, ForeignKey('usuario.id_usuario', ondelete="CASCADE"), unique=True, nullable=False)

    media_avaliacao: Mapped[Numeric] = mapped_column(Numeric(10, 1))