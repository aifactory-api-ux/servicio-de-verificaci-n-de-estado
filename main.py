"""
Módulo principal del servicio de verificación de estado (health-check).

Proporciona un endpoint HTTP mínimo para balanceadores de carga u orquestadores,
permitiendo comprobar la disponibilidad del servicio sin requerir autenticación.
"""

from fastapi import FastAPI

# Inicialización de la aplicación FastAPI para el servicio de health-check
app = FastAPI(
    title="Health Check API",
    version="1.0.0",
    description="Servicio mínimo de verificación de estado para balanceadores de carga.",
)


@app.get("/ping")
def ping() -> dict[str, str]:
    """
    Endpoint de comprobación de salud del servicio.

    Responde con código HTTP 200 y un objeto JSON indicando que el servicio
    se encuentra operativo. Cualquier método distinto a GET retornará un código 405.
    """
    return {"status": "ok"}
