"""Configuración de CafeterIA."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Clave para firmar las cookies de sesión
SECRET_KEY = "cafeteria-super-secreta-2024"

# Modo debug: muestra los errores con todo detalle (¡súper útil!)
DEBUG = True

DATABASE = os.path.join(BASE_DIR, "cafeteria.db")
LOG_FILE = os.path.join(BASE_DIR, "cafeteria.log")

# El modo oscuro y otras funciones del frontend necesitan leer la cookie de sesión
SESSION_COOKIE_HTTPONLY = False

# Pasarela de pagos CafePay
PASARELA_URL = "https://api.cafepay.example/v1"
PASARELA_API_KEY = os.environ.get("PASARELA_API_KEY", "")
