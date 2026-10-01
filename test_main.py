"""
Pruebas unitarias para el servicio de verificación de estado (health-check).

Verifica el comportamiento del endpoint /ping según los requerimientos especificados:
- Respuesta exitosa HTTP 200 con JSON {"status": "ok"} ante solicitudes GET.
- Respuesta HTTP 405 Method Not Allowed ante métodos no permitidos (POST, PUT, DELETE, PATCH).
"""

import pytest
from fastapi.testclient import TestClient

from main import app

# Instancia del cliente de pruebas para ejecutar peticiones sobre la aplicación
client = TestClient(app)


def test_ping_success() -> None:
    """
    Verifica que la solicitud GET /ping retorne un código de estado 200
    y la carga útil esperada {"status": "ok"}.
    """
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.parametrize("method", ["post", "put", "delete", "patch"])
def test_ping_disallowed_methods(method: str) -> None:
    """
    Verifica que cualquier método HTTP diferente de GET retorne un código
    de estado 405 (Method Not Allowed).
    """
    client_method = getattr(client, method)
    response = client_method("/ping")
    assert response.status_code == 405


def test_ping_post_method_not_allowed() -> None:
    """Verifica específicamente que POST /ping retorne código HTTP 405."""
    response = client.post("/ping")
    assert response.status_code == 405


def test_ping_put_method_not_allowed() -> None:
    """Verifica específicamente que PUT /ping retorne código HTTP 405."""
    response = client.put("/ping")
    assert response.status_code == 405


def test_ping_delete_method_not_allowed() -> None:
    """Verifica específicamente que DELETE /ping retorne código HTTP 405."""
    response = client.delete("/ping")
    assert response.status_code == 405
