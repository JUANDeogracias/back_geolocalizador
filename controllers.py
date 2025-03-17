from typing import List
from models import Dispositivo  # Aquí importarías tus modelos si los tienes
from schemas import DispositivoCreate, DispositivoResponse

# Función para crear un dispositivo
def crear_dispositivo_controller(dispositivo: DispositivoCreate) -> DispositivoResponse:
    dispositivo_nuevo = Dispositivo(id=dispositivo.id, nombre=dispositivo.nombre)
    return DispositivoResponse(id=dispositivo_nuevo.id, nombre=dispositivo_nuevo.nombre)

# Función para obtener los dispositivos
def obtener_dispositivos_controller() -> List[DispositivoResponse]:
    return [DispositivoResponse(id=d.id, nombre=d.nombre) for d in Dispositivo.all()]