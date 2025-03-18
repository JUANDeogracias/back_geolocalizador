from fastapi import FastAPI
from database import engine
import models
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database
from sqlalchemy.orm import joinedload


# Crear las tablas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de dispositivos"}


# Endpoints

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/dispositivo/{dispositivo_id}", response_model=schemas.Dispositivo)
def get_dispositivo(dispositivo_id: int, db: Session = Depends(get_db)):
    # Ejecutamos la consulta correctamente con .first() para obtener solo un dispositivo
    db_dispositivo = db.query(models.Dispositivo).options(joinedload(models.Dispositivo.registros)).filter(models.Dispositivo.id == dispositivo_id).first()

    # Si no encontramos el dispositivo, lanzamos un error 404
    if db_dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    
    # Devolvemos el dispositivo con todos sus registros asociados
    return db_dispositivo

