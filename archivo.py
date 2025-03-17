import requests
import network
import time

# Configuración de Wi-Fi
SSID = 'ATC'  # Reemplaza con tu SSID
PASSWORD = 'atc-gaac'  # Reemplaza con tu contraseña de Wi-Fi

# Función para hacer una solicitud GET al servidor
def hacer_solicitud_get():
    url = 'http://127.0.0.1:8000/api/'  # Reemplaza con la URL de tu servidor Flask
    try:
        response = requests.get(url)
        print('Respuesta del servidor:', response.json())
    except Exception as e:
        print('Error al hacer la solicitud GET:', e)

# Llamar al endpoint cada 10 segundos
while True:
    print('Haciendo solicitud GET...')
    hacer_solicitud_get()
    time.sleep(10)  # Espera 10 segundos antes de hacer la siguiente solicitud
