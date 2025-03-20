from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    username: str
    password: str
    email: Optional[str] = None

class Dispositivo(BaseModel):
    id: Optional[int] = None
    nombre: Optional[str]
    active: bool = False
    usuario_id: Optional[int] = None


class Registro(BaseModel):
    id: Optional[int] = None
    fecha: datetime
    coordenadas: str
    dispositivo_id: int