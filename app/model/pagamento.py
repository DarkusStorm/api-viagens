from sqlalchemy import BigInteger, SmallInteger, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class PagamentoModel(Base):
    __tablename__ = "pagamento"

    id_pagamento: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True, autoincrement=True)
    id_corrida: Mapped[int] = mapped_column(BigInteger, ForeignKey('corrida.id_corrida', ondelete="CASCADE"), unique=True, nullable=False)
    id_metodo_pagamento: Mapped[int] = mapped_column(SmallInteger, ForeignKey('metodo_pagamento.id_metodo_pagamento', ondelete="CASCADE"), unique=True, nullable=False)

    valor: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    datahora_transacao: Mapped[DateTime] = mapped_column(DateTime, nullable=False)