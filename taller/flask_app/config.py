"""
    Variables globales de configuración
    para el consumo del servicio web de Django.
"""

# URL base del servicio web de Django (proyecto taller13)
API_URL = "http://localhost:8000/api"

# Token del usuario que consume la API.
# Se genera en Django con: python manage.py shell
# o revisando /admin/authtoken/tokenproxy/
TOKEN = "d779aa429f31953756382a6672d9ae53f32087cd"

HEADERS = {
    "Authorization": f"Token {TOKEN}",
    "Content-Type": "application/json",
}
