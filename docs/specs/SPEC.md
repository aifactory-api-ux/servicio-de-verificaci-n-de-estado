# SPEC.md

## 1. TECHNOLOGY STACK
- Python 3.11+
- FastAPI (HTTP web framework)
- Uvicorn (ASGI server runtime)
- Pytest (test runner)
- HTTPX (test client dependency for FastAPI `TestClient`)

## 2. DATA CONTRACTS
### Request Model
None

### Response Payload (`GET /ping`)
```json
{
  "status": "ok"
}
```

## 3. API ENDPOINTS
- `GET /ping`
  - Success Response: Status `200 OK`
  - Body: `{"status": "ok"}`
  - Authentication: None
- Any HTTP method other than `GET` on `/ping` (e.g., `POST`, `PUT`, `DELETE`, `PATCH`):
  - Error Response: Status `405 Method Not Allowed`

## 4. FILE STRUCTURE
```
.
├── main.py
├── requirements.txt
└── test_main.py
```

## 5. ENVIRONMENT VARIABLES
None

## 6. IMPORT CONTRACTS
### `main.py`
```python
from fastapi import FastAPI
```

### `test_main.py`
```python
import pytest
from fastapi.testclient import TestClient
from main import app
```

## 10. FUNCTIONAL REQUIREMENTS COVERAGE
| Source Requirement Phrase | Target File | Verification / Implementation Details |
|---|---|---|
| "servicio HTTP mínimo de salud para que nuestro balanceador lo use como health-check. Solo backend, sin interfaz." | `main.py` | Minimal FastAPI application instance exposing HTTP endpoints without graphical interface or template rendering. |
| "Un único endpoint GET /ping que responde 200 con el JSON {\"status\":\"ok\"}, sin autenticación" | `main.py`, `test_main.py` | Route decorator `@app.get("/ping")` returns literal dictionary `{"status": "ok"}` with HTTP 200 and no authentication dependencies; verified via unit test. |
| "cualquier método distinto de GET debe responder 405" | `main.py`, `test_main.py` | FastAPI router automatically emits status 405 Method Not Allowed for non-GET requests to `/ping`; verified via unit tests for `POST`, `PUT`, and `DELETE`. |
| "Debe incluir una prueba unitaria del endpoint." | `test_main.py` | Pytest test functions executing `GET /ping` asserting status code 200 and payload `{"status": "ok"}`, and asserting status code 405 on non-GET calls. |