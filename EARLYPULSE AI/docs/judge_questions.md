# Likely Judge Questions

---

## Q1: Is this a medical diagnosis system?

Answer:

No.

This is an educational prototype for risk estimation and preventive awareness.

It is not clinically validated and cannot replace healthcare professionals.

---

## Q2: Which models are used?

Answer:

We compare:

- Random Forest
- XGBoost

The best-performing model is automatically selected.

---

## Q3: Why use SHAP?

Answer:

Healthcare requires transparency.

SHAP helps explain which features influenced the prediction.

---

## Q4: How is patient privacy handled?

Answer:

The prototype stores minimal data locally in SQLite.

Production systems would include:

- Encryption
- Authentication
- HIPAA compliance

---

## Q5: Can it predict multiple diseases?

Answer:

The architecture is modular and can be extended to support multiple diseases.

---

## Q6: Why did you choose this stack?

Answer:

We used open-source technologies:

- Python
- FastAPI
- Streamlit
- XGBoost
- SHAP

They enable rapid development and deployment.

---

## Q7: How can this scale?

Answer:

The backend is API-driven and can scale with:

- Docker
- Kubernetes
- Cloud databases
- Load balancers

---

## Q8: What is the biggest limitation?

Answer:

The dataset is synthetic and not clinically validated.

Future work requires collaboration with medical experts.
