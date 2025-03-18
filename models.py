from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base  # Importa la base de datos

class Usuario(Base):
    __tablename__ = "usuarios"  # Nombre de la tabla en la bbdd

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

    dispositivos = relationship("Dispositivo", back_populates="usuario")

class Dispositivo(Base):
    __tablename__ = "dispositivos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    usuario = relationship("Usuario", back_populates="dispositivos")
    registros = relationship("Registro", back_populates="dispositivo")

class Registro(Base):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    descripcion = Column(String, nullable=False)
    dispositivo_id = Column(Integer, ForeignKey("dispositivos.id"), nullable=False)

    dispositivo = relationship("Dispositivo", back_populates="registros")
