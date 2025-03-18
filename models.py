from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base
from typing import List
from sqlalchemy.orm import Mapped, mapped_column

# Modelo para la tabla 'usuarios'
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    role = Column(String, unique=True)
    password = Column(String)

    # Relación con dispositivos
    dispositivos = relationship("Dispositivo", back_populates="owner")

# Modelo para la tabla 'registros'
class Registro(Base):
    __tablename__ = 'registros'

    id = Column(Integer, primary_key=True, index=True)
    dispositivo_id = Column(Integer, ForeignKey('dispositivos.id'))
    descripcion = Column(String)
    date = Column(Date)

    # Relación con dispositivo
    dispositivo = relationship("Dispositivo", back_populates="registros")
    dispositivo: Mapped['Dispositivo'] = relationship("Dispositivo", back_populates="registros")

# Modelo para la tabla 'dispositivos'
class Dispositivo(Base):
    __tablename__ = 'dispositivos'

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    nombre = Column(String)


    # Relación con registros
    registros = relationship("Registro", back_populates="dispositivo")

    # Relación con usuario
    owner = relationship("Usuario", back_populates="dispositivos")
    registros: Mapped[List['Registro']] = relationship("Registro", back_populates="dispositivo")



