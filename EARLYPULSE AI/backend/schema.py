from pydantic import BaseModel


class PatientRequest(BaseModel):

    age: int
    sex: str

    bmi: float

    smoking: str
    alcohol: str
    exercise_level: str

    heart_rate: int
    systolic_bp: int
    diastolic_bp: int

    blood_sugar: float
    cholesterol: float

    family_history: str

    fatigue: str
    fever: str


class PredictionResponse(BaseModel):

    risk_prediction: int
    confidence: float