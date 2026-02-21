#POR TERMINAR

# Uni  (Generador de Horarios Universitarios)

Sistema completo para generar horarios académicos para **Ingeniería**, **Ciencias** y **Letras** con reglas:
- Ventana: 07:00–20:00, resolución 30 min.
- Aulas teóricas (60) y laboratorios (15) con división automática de grupos.
- Semestre **Abril–Agosto** = ciclos **impares**; **Agosto–Diciembre** = ciclos **pares** (bloqueo duro).
- Profesores con disponibilidad y tope de **6 h/día** (incluye labs).
- Heurística por fases: **Labs → Teóricos → Validaciones**.
- Exporta **Excel** y **PDF** de alertas.

## Requisitos
```bash
python >= 3.10
pip install -r requirements.txt
```

## CLI (rápido)
```bash
python app_cli.py --semester "Agosto-Diciembre" --export
# Salida: horarios.xlsx y alertas.pdf en el directorio actual
```

## API (FastAPI)
```bash
uvicorn app_api:app --reload --port 8000
# Abrir: http://127.0.0.1:8000/docs
```

Endpoints clave:
- `POST /schedule` → genera horarios desde JSON (rooms, professors, courses).
- `GET /sample` → dataset de ejemplo.
- `GET /health` → ping.

## Estructura
```
uni_scheduler_project/
├─ requirements.txt
├─ README.md
├─ app_cli.py
├─ app_api.py
└─ src/uni_scheduler/
   ├─ __init__.py
   ├─ models.py
   ├─ utils.py
   ├─ scheduler.py
   └─ data_example.py
```

## Ejemplo mínimo
Para probar rápido, usa:
```bash
python app_cli.py --semester "Agosto-Diciembre" --export
```
Luego revisa `horarios.xlsx` y `alertas.pdf`.
