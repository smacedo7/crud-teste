from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ClienteCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    telefone: str | None = Field(None, min_length=10, max_length=15)


class ClienteUpdate(BaseModel):
    nome: str | None = Field(None, min_length=3, max_length=50)
    email: EmailStr | None = None
    telefone: str | None = Field(None, min_length=10, max_length=15)
    ativo: bool | None = None


class ClienteRead(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    # ler dados diretamente dos objetos

    id: int
    nome: str
    email: EmailStr
    telefone: str | None = None
    ativo: bool
    criado_em: datetime


class ClienteDelete(BaseModel):
    pass
