from fastapi import FastAPI

from backend.schema import PatientRequest
from backend.inference import predict_risk
from backend.explainability import explain_prediction
from backend.recommendations import generate_recommendations
from backend.db import save_prediction

app = FastAPI(
    title="AI Medical Early Disease Risk Prediction API",
    version="1.0.0",
)


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "message": "API is running."
    }


@app.post("/predict")
def predict(request: PatientRequest):

    patient = request.model_dump()

    prediction = predict_risk(patient)

    save_prediction(
        prediction["risk_prediction"],
        prediction["confidence"]
    )

    return prediction


@app.post("/explain")
def explain(request: PatientRequest):

    patient = request.model_dump()

    return explain_prediction(patient)


@app.post("/recommend")
def recommend(request: PatientRequest):

    patient = request.model_dump()

    prediction = predict_risk(patient)

    return generate_recommendations(
        patient_data=patient,
        risk_prediction=prediction["risk_prediction"],
        confidence=prediction["confidence"],
    )


@app.get("/history/{user_id}")
def history(user_id: int):

    return {
        "user_id": user_id,
        "history": [],
        "message": (
            "User-specific history is not enabled "
            "in the current prototype."
        ),
    }