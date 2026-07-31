from backend.inference import predict_risk
from backend.explainability import explain_prediction
from backend.recommendations import generate_recommendations


def test_smoke():

    patient = {

        "age": 45,
        "sex": "Male",
        "bmi": 27.8,
        "smoking": "No",
        "alcohol": "No",
        "exercise_level": "Medium",
        "heart_rate": 82,
        "systolic_bp": 124,
        "diastolic_bp": 81,
        "blood_sugar": 101,
        "cholesterol": 185,
        "family_history": "No",
        "fatigue": "No",
        "fever": "No",
    }

    prediction = predict_risk(patient)

    assert "risk_prediction" in prediction
    assert "confidence" in prediction

    explanation = explain_prediction(patient)

    assert "top_factors" in explanation

    recommendations = generate_recommendations(
        patient,
        prediction["risk_prediction"],
        prediction["confidence"],
    )

    assert "urgency" in recommendations
    assert "patient_advice" in recommendations