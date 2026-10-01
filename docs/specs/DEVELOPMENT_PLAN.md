# DEVELOPMENT PLAN: Servicio de Verificación de Estado

## 1. ARCHITECTURE OVERVIEW
Servicio backend mínimo implementado en Python con FastAPI y servido mediante Uvicorn, sin dependencias de base de datos, capas de autenticación ni componentes de frontend. Expone una única ruta `GET /ping` configurada para devolver el estado de salud del servicio con código HTTP 200 y cuerpo JSON `{"status": "ok"}`. Los métodos HTTP no permitidos sobre la ruta responden automáticamente con código HTTP 405. Las pruebas unitarias están implementadas con Pytest y el cliente de pruebas `TestClient` de FastAPI.

## 2. ACCEPTANCE CRITERIA
1. El endpoint `GET /ping` responde con código de estado HTTP 200 y carga útil JSON `{"status": "ok"}` sin requerir autenticación.
2. Cualquier método HTTP distinto de `GET` (por ejemplo, `POST`, `PUT`, `DELETE`) hacia `/ping` responde con código de estado HTTP 405 Method Not Allowed.
3. Las pruebas unitarias en `test_main.py` verifican con Pytest la respuesta 200 y el cuerpo esperado para `GET /ping`, así como el código 405 ante métodos HTTP no permitidos.

## TEAM SCOPE (MANDATORY — PARSED BY THE PIPELINE)
Use one backend_developer role (`role-be`) for all items.

## 3. EXECUTABLE ITEMS

### ITEM 1: Implementación del servicio de health-check y suite de pruebas unitarias
**Goal:** Crear la aplicación mínima en FastAPI con el endpoint `GET /ping` y su respectiva suite de pruebas unitarias cubriendo los códigos de respuesta 200 y 405.
**Files to create:**
- requirements.txt
- main.py
- test_main.py
**Dependencies:** None
**Validation:** Ejecutar `pytest test_main.py` y verificar que todas las pruebas pasen exitosamente validando el retorno de código 200 con `{"status": "ok"}` en `GET /ping` y código 405 en solicitudes con métodos no permitidos.
**Role:** role-be (backend_developer)