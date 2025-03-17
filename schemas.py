from pydantic import BaseModel
from datetime import date
from typing import List
class UsuarioBase(BaseModel):
    username: str
    password: str
    role: str
class DispositivoBase(BaseModel):
    nombre: str

class ActivacionBase(BaseModel):
    date: date
    descripcion: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id : int
    dispositivos: List["DispositivoResponse"] = []

    class Config:
        from_attributes = True

class DispositivoCreate(DispositivoBase):
    pass

class DispositivoResponse(DispositivoBase):
    id: int
    usuario_id: int
    activaciones: List["ActivacionResponse"] = []

    class Config:
        from_attributes = True

class ActivacionCreate(ActivacionBase):
    pass

class ActivacionResponse(ActivacionBase):
    id: int
    dispositivo_id: int

    class Config:
        from_attributes = True


