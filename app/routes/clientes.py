from app.db.session import get_db
from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.schemas.cliente import ClienteCreate, ClienteRead
from app.services.cliente import criar_cliente as create

router_clientes = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@router_clientes.get('/')
def listar_clientes():
    return {
        'cliente1': 'pedro'
    }


@router_clientes.post('/', response_model=ClienteRead, status_code=status.HTTP_201_CREATED)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    try:
        customer = create(db, cliente)
    except IntegrityError:
        raise HTTPException(status_code=409, detail='Insira um email válido.')
    return customer
