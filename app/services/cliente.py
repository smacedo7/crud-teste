from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate


def criar_cliente(db: Session, dados: ClienteCreate) -> Cliente:
    cliente_dict = dados.model_dump()
    cliente = Cliente(**cliente_dict)
    db.add(cliente)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise

    db.refresh(cliente)

    return cliente
