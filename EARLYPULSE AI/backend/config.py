from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
DOCS_DIR = BASE_DIR / "docs"
ARTIFACTS_DIR = BASE_DIR / "artifacts"

ARTIFACTS_DIR.mkdir(exist_ok=True)

DATA_FILE = DATA_DIR / "sample_input.csv"

MODEL_PATH = ARTIFACTS_DIR / "best_model.pkl"
METRICS_PATH = ARTIFACTS_DIR / "model_metrics.json"

RANDOM_STATE = 42

TEST_SIZE = 0.20

TARGET_COLUMN = "disease_risk"

CATEGORICAL_COLUMNS = [
    "sex",
    "smoking",
    "alcohol",
    "exercise_level",
    "family_history",
    "fatigue",
    "fever",
]

NUMERICAL_COLUMNS = [
    "age",
    "bmi",
    "heart_rate",
    "systolic_bp",
    "diastolic_bp",
    "blood_sugar",
    "cholesterol",
]