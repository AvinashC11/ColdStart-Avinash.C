import joblib
import pandas as pd

from backend.config import MODEL_PATH


model = joblib.load(MODEL_PATH)


def predict_risk(patient_data: dict):

    df = pd.DataFrame([patient_data])

    prediction = int(model.predict(df)[0])

    confidence = float(
        max(model.predict_proba(df)[0])
    )

    return {
        "risk_prediction": prediction,
        "confidence": round(confidence, 4),
    }


if __name__ == "__main__":

    sample = {
        "age": 45,
        "sex": "Male",
        "bmi": 28.4,
        "smoking": "Yes",
        "alcohol": "No",
        "exercise_level": "Low",
        "heart_rate": 90,
        "systolic_bp": 140,
        "diastolic_bp": 88,
        "blood_sugar": 135,
        "cholesterol": 225,
        "family_history": "Yes",
        "fatigue": "Yes",
        "fever": "No",
    }

    print(predict_risk(sample))