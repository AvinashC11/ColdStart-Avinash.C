# AI Medical Early Disease Risk Prediction Architecture

## Disclaimer

This project is a hackathon prototype and not a certified medical device. Predictions are experimental and must not be used for diagnosis or treatment.

---

# High-Level Architecture

```text
Patient Input
      ↓
Streamlit Frontend
      ↓
FastAPI Backend
      ↓
Validation Layer
      ↓
Preprocessing Pipeline
      ↓
ML Model
      ↓
Prediction Engine
      ↓
Explainability Layer
      ↓
Recommendation Engine
      ↓
SQLite Storage
      ↓
Dashboard Output
```

---

# Components

## Frontend Layer

Technology:

- Streamlit
- Plotly

Responsibilities:

- Collect patient information
- Display prediction score
- Show explanations
- Present recommendations
- Export reports

---

## API Layer

Technology:

- FastAPI
- Pydantic

Endpoints:

- POST /predict
- POST /explain
- POST /recommend
- GET /health
- GET /history

Responsibilities:

- Validate requests
- Route business logic
- Return JSON responses

---

## Intelligence Layer

Modules:

- inference.py
- explainability.py
- recommendations.py

Responsibilities:

- Predict disease risk
- Explain predictions
- Generate preventive advice

---

## Machine Learning Layer

Models:

- Random Forest
- XGBoost

Pipeline:

1. Data cleaning
2. Missing-value handling
3. Encoding
4. Training
5. Evaluation
6. Model selection
7. Serialization

---

## Data Layer

Technology:

- SQLite

Stores:

- Prediction results
- Confidence scores
- History records

---

# Data Flow

```text
Patient Form
    ↓
Schema Validation
    ↓
Feature Preprocessing
    ↓
ML Model
    ↓
Prediction
    ↓
SHAP Explanation
    ↓
Recommendations
    ↓
Storage
```

---

# Deployment Flow

```text
GitHub
   ↓
Docker
   ↓
Render / Hugging Face / Streamlit Cloud
   ↓
Public URL
```