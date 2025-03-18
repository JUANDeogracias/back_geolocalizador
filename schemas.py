from pydantic import BaseModel
from datetime import date
from typing import List, Optional

# Esquema para la creación de un usuario
class UsuarioCreate(BaseModel):
    username: str
    role: str
    password: str

# Esquema para la respuesta del usuario
class Usuario(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        orm_mode = True


# Esquema para la creación de un registro
class RegistroCreate(BaseModel):
    dispositivo_id: int
    descripcion: str
    date: Optional[date] = None

# Esquema para la respuesta del registro
class Registro(BaseModel):
    id: int
    dispositivo_id: int
    descripcion: str
    date: date

    class Config:
        orm_mode = True

# Esquema para la creación de un dispositivo
class DispositivoCreate(BaseModel):
    usuario_id: int
    nombre: str

# Esquema para la respuesta del dispositivo
class Dispositivo(BaseModel):
    id: int
    usuario_id: int
    nombre: str
    registros: List[Registro] 

    class Config:
        orm_mode = True


