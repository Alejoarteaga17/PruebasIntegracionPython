
# Introducción a Pruebas de Integración (Python) — 4 partes

Este repositorio contiene un ejercicio práctico en **Python** para evidenciar 4 tipos de integración:

1) **Por capas** (Controller → Service → Repository in-memory)  
2) **Modular** (un módulo usa a otro)  
3) **Con API externa** (cliente HTTP real contra servidor simulado)  
4) **Con base de datos** (SQLite en memoria)

## Requisitos
- Python 3.11+
- `pip install -r requirements.txt`

## Ejecutar
```bash
pytest -q
```
O por parte:
```bash
pytest -q tests/test_part1_layers.py
pytest -q tests/test_part2_modules.py
pytest -q tests/test_part3_external_api.py
pytest -q tests/test_part4_database.py
```

## Estructura
```
src/
  layers/ (modelo, repositorio in-memory, servicio, controlador)
  modules/ (discount, order)
  external/ (cliente http)
  db/ (repositorio sqlite)
```

## Estructura detallada
.devcontainer/ para abrir en GitHub Codespaces con Python 3.11 y extensiones.
.github/workflows/ci.yml: workflow de Actions que instala deps y ejecuta pytest.
requirements.txt: pytest, httpx, pytest-httpserver.
pytest.ini: configuración para descubrir tests desde src/ y tests/.
src/ con el código de producción:

layers/: modelo User, InMemoryUserRepository, UserService, UserController.
modules/: DiscountEngine + OrderCalculator.
external/: UserClient con httpx.
db/: SQLiteUserRepository con sqlite3 en memoria.


tests/ con 4 archivos:

test_part1_layers.py — por capas.
test_part2_modules.py — modular.
test_part3_external_api.py — API externa con pytest-httpserver.
test_part4_database.py — base de datos (SQLite in‑memory).


README.md con instrucciones ejecutables.

