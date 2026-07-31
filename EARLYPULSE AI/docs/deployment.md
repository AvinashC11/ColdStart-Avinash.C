# Deployment Guide

## Disclaimer

This prototype is not a medical device.

---

# Option 1: Streamlit Cloud

Repository structure:

```text
frontend/
backend/
requirements.txt
```

Steps:

1. Push code to GitHub.
2. Open Streamlit Cloud.
3. Connect repository.
4. Set entry point:

```text
frontend/streamlit_app.py
```

5. Deploy.

---

# Option 2: Hugging Face Spaces

Create:

- Space type: Docker

Upload:

- Dockerfile
- source code

Expose:

```text
8501
```

Launch.

---

# Option 3: Render

Backend:

```text
uvicorn backend.app:app --host 0.0.0.0 --port 8000
```

Frontend:

```text
streamlit run frontend/streamlit_app.py
```

---

# Environment Variables

```text
APP_NAME=AI_Medical_Early_Disease_Risk

DATABASE_URL=sqlite:///medical_risk.db

MODEL_PATH=artifacts/best_model.pkl

RANDOM_STATE=42

TEST_SIZE=0.20
```

---

# Model Handling

Train model:

```bash
python backend/train_model.py
```

Generated:

```text
artifacts/

best_model.pkl
model_metrics.json
```

Ensure the model exists before deployment.

---

# Docker Deployment

Build:

```bash
docker-compose build
```

Run:

```bash
docker-compose up
```

Frontend:

```text
http://localhost:8501
```

Backend:

```text
http://localhost:8000
```
