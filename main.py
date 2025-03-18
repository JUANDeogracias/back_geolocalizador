from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario, Dispositivo, Registro
from schemas import UsuarioCreate, UsuarioResponse, DispositivoCreate, DispositivoResponse, RegistroBase, RegistroCreate, RegistroResponse

app = FastAPI()

# ---------------------- USUARIOS ----------------------
@app.post("/api/usuarios/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = Usuario(
        username=usuario.username,
        password=usuario.password,
        role=usuario.role
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@app.get("/api/usuarios/", response_model=list[UsuarioResponse])
def obtener_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

# ---------------------- DISPOSITIVOS ----------------------
@app.post("/api/dispositivos/", response_model=DispositivoResponse)
def crear_dispositivo(dispositivo: DispositivoCreate, db: Session = Depends(get_db)):
    nuevo_dispositivo = Dispositivo(
        nombre=dispositivo.nombre,
        usuario_id=dispositivo.usuario_id
    )
    db.add(nuevo_dispositivo)
    db.commit()
    db.refresh(nuevo_dispositivo)
    return nuevo_dispositivo

@app.get("/api/dispositivos/", response_model=list[DispositivoResponse])
def obtener_dispositivos(db: Session = Depends(get_db)):
    return db.query(Dispositivo).all()

# ---------------------- REGISTROS ----------------------
@app.post("/api/registros/", response_model=RegistroResponse)
def crear_activacion(activacion: RegistroCreate, db: Session = Depends(get_db)):
    nueva_activacion = Registro(
        date=activacion.date,
        descripcion=activacion.descripcion,
        dispositivo_id=activacion.dispositivo_id
    )
    db.add(nueva_activacion)
    db.commit()
    db.refresh(nueva_activacion)
    return nueva_activacion

@app.get("/api/registros/", response_model=list[RegistroResponse])
def obtener_activaciones(db: Session = Depends(get_db)):
    return db.query(Registro).all()
