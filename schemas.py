from pydantic import BaseModel
from datetime import date
from typing import List
class UsuarioBase(BaseModel):
    username: str
    password: str
    role: str
class DispositivoBase(BaseModel):
    nombre: str

class RegistroBase(BaseModel):
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
    activaciones: List["RegistroResponse"] = []

    class Config:
        from_attributes = True

class RegistroCreate(RegistroBase):
    pass

class RegistroResponse(RegistroBase):
    id: int
    dispositivo_id: int

    class Config:
        from_attributes = True


