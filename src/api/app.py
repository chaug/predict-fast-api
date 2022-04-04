import os
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path

from .routers import predict

port = int(os.environ.get('PORT', 8000))
app = FastAPI(port=port)

#################################################

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://predict-fast-api.herokuapp.com",
        f"http://127.0.0.1:{port}",
        f"http://localhost:{port}",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#################################################

API_SRC_DIR = Path(__file__).parent
PROJECT_DIR = API_SRC_DIR.parent.parent
MODELS_DIR = PROJECT_DIR / "models"

predict.load_models(MODELS_DIR)

app.include_router(predict.router)

@app.get("/")
def versions():
    return {
        "python" : sys.version,
    }
