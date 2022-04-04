# Predict with Fast API

## Local Setup

```bash
pip install -r requirements.txt
```

## Local Run

Local run with:

```bash
uvicorn api.app:app --reload --app-dir src --port ${PORT:-8000}
# or
./run-local-api.sh
```
