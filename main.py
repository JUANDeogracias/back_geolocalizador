from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Dispositivos(BaseModel):
    id: int
    nombre: str

@app.get("/api/")
def raiz():
    return {"mensaje": "¡Hola, FastAPI!"}

@app.post("/api/dispositivos/")
def crear_dispositivo(dispositivo: Dispositivos):
    return {
            "id": dispositivo.id,
            "nombre": dispositivo.nombre
            }

@app.get("/api/dispositivos/")
def obtener_dispositivos(dispositivo: Dispositivos):

    return {
            "id": dispositivo.id,
            "nombre": dispositivo.nombre
            }
