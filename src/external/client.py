
import httpx
from typing import Optional, Dict, Any


class UserClient:
    def __init__(self, base_url: str):
        # Normaliza la URL base para evitar dobles '/' al construir endpoints.
        self.base_url = base_url.rstrip("/")

    def fetch_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        # Construye la ruta del recurso de usuario usando el ID recibido.
        url = f"{self.base_url}/users/{user_id}"

        # Solicita JSON al servicio externo y limita el tiempo de espera a 5s.
        r = httpx.get(url, headers={"Accept": "application/json"}, timeout=5.0)

        # Solo retorna datos cuando la respuesta es exitosa.
        if r.status_code == 200:
            return r.json()

        # Si el usuario no existe o hay otro estado HTTP, retorna None.
        return None
