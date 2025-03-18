from typing import List
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, Session
from datetime import datetime

# Crear la base de datos en SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


Base = declarative_base()

# Definir modelos
class Dispositivo(Base):
    __tablename__ = "dispositivos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

    actividades = relationship("Actividad", back_populates="dispositivo")


class Actividad(Base):
    __tablename__ = "actividades"

    id = Column(Integer, primary_key=True, index=True)
    hora = Column(DateTime, default=datetime.utcnow)
    posicion = Column(String)

    dispositivo_id = Column(Integer, ForeignKey("dispositivos.id"))
    dispositivo = relationship("Dispositivo", back_populates="actividades")


# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic Schemas
from pydantic import BaseModel

class ActividadCreate(BaseModel):
    posicion: str
    dispositivo_id: int

class DispositivoCreate(BaseModel):
    nombre: str


# Endpoints
@app.post("/dispositivos/", response_model=DispositivoCreate)
def create_dispositivo(dispositivo: DispositivoCreate, db: Session = Depends(get_db)):
    nuevo_dispositivo = Dispositivo(nombre=dispositivo.nombre)
    db.add(nuevo_dispositivo)
    db.commit()
    db.refresh(nuevo_dispositivo)
    return nuevo_dispositivo


@app.post("/actividades/", response_model=ActividadCreate)
def create_actividad(actividad: ActividadCreate, db: Session = Depends(get_db)):
    dispositivo = db.query(Dispositivo).filter(Dispositivo.id == actividad.dispositivo_id).first()
    if not dispositivo:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")

    nueva_actividad = Actividad(posicion=actividad.posicion, dispositivo_id=actividad.dispositivo_id)
    db.add(nueva_actividad)
    db.commit()
    db.refresh(nueva_actividad)
    return nueva_actividad
