import joblib
from fastapi import APIRouter, HTTPException

CLASSIFIER_PATH = None
CLASSIFIER = None
def load_models(folder):
    global CLASSIFIER, CLASSIFIER_PATH
    # Classifier
    CLASSIFIER_PATH = folder / 'classifier.joblib'
    CLASSIFIER = joblib.load(CLASSIFIER_PATH) if CLASSIFIER_PATH.exists() else None

router = APIRouter(
    prefix="/predict",
    tags=["predict"],
)

@router.get("/client/{client_id}")
def get_client_prediction(client_id: int):
    if client_id == 666:
        raise HTTPException(
            status_code = 404,
            detail = f"Unknown client_id: {client_id}"
        )
    if CLASSIFIER:
        return dict(
            client_id = client_id,
            prediction = CLASSIFIER.predict(client_id)
        )
    raise HTTPException(
        status_code = 404,
        detail = f"No classifier loaded: {CLASSIFIER_PATH}"
    )
