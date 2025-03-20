from sqlalchemy import create_engine, Column, String, Boolean, ForeignKey, DateTime, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from uuid import uuid4
import datetime

DATABASE_URL = "sqlite:///./gps3_data.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class UsuarioDB(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True, nullable=True)

class DispositivoDB(Base):
    __tablename__ = "dispositivos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    active = Column(Boolean, default=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

class RegistroDB(Base):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)
    coordenadas = Column(String)
    dispositivo_id = Column(Integer, ForeignKey("dispositivos.id"))

Base.metadata.create_all(bind=engine)