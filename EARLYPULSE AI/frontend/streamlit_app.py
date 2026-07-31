import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from backend.inference import predict_risk
from backend.explainability import explain_prediction
from backend.recommendations import generate_recommendations

st.set_page_config(
    page_title="EarlyPulse AI",
    page_icon="🏥",
    layout="wide",
)

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title("🩺 EARLYPULSE AI")

    st.markdown(
        """
        **AI-Powered Preventive Health Screening**

        ✓ Risk Prediction

        ✓ Explainable AI

        ✓ Preventive Guidance

        ✓ Doctor-Friendly Dashboard
        """
    )

    doctor_mode = st.toggle("👨‍⚕️ Doctor Mode")

st.markdown(
    """
    # 💊 EARLYPULSE AI

    ### AI Medical Early Disease Risk Prediction

    

    ---
    """
)

# -----------------------------
# HERO
# -----------------------------
st.image(
    "frontend/assets/hero.jpeg",
    use_container_width=True
)

# =========================
# TITLE
# =========================



st.error(
    "⚠️ Medical Disclaimer: This application is a hackathon prototype and is intended only for educational purposes. It is not a certified medical device and must not be used for diagnosis or treatment."
)




st.error(
    "⚠️ Medical Disclaimer: This is a hackathon prototype and "
    "must not be used for diagnosis or treatment."
)

# -----------------------------
# FORM
# -----------------------------

st.subheader("📋 Patient Information")

with st.form("patient_form"):

    col1, col2 = st.columns(2)

    with col1:

        age = st.slider("Age", 1, 100, 35)

        sex = st.selectbox(
            "Sex",
            ["Male", "Female"]
        )

        bmi = st.number_input(
            "BMI",
            10.0,
            50.0,
            24.5
        )

        smoking = st.selectbox(
            "Smoking",
            ["Yes", "No"]
        )

        alcohol = st.selectbox(
            "Alcohol",
            ["Yes", "No"]
        )

        exercise = st.selectbox(
            "Exercise Level",
            ["Low", "Medium", "High"]
        )

    with col2:

        heart_rate = st.slider(
            "Heart Rate",
            40,
            180,
            80
        )

        systolic = st.slider(
            "Systolic BP",
            80,
            220,
            120
        )

        diastolic = st.slider(
            "Diastolic BP",
            50,
            150,
            80
        )

        sugar = st.slider(
            "Blood Sugar",
            50,
            300,
            100
        )

        cholesterol = st.slider(
            "Cholesterol",
            100,
            350,
            180
        )

    col3, col4, col5 = st.columns(3)

    with col3:

        family = st.selectbox(
            "Family History",
            ["Yes", "No"]
        )

    with col4:

        fatigue = st.selectbox(
            "Fatigue",
            ["Yes", "No"]
        )

    with col5:

        fever = st.selectbox(
            "Fever",
            ["Yes", "No"]
        )

    submit = st.form_submit_button(
        "🚀 Analyze Health Risk"
    )

# -----------------------------
# PREDICTION
# -----------------------------

if submit:

    patient = {

        "age": age,
        "sex": sex,
        "bmi": bmi,
        "smoking": smoking,
        "alcohol": alcohol,
        "exercise_level": exercise,
        "heart_rate": heart_rate,
        "systolic_bp": systolic,
        "diastolic_bp": diastolic,
        "blood_sugar": sugar,
        "cholesterol": cholesterol,
        "family_history": family,
        "fatigue": fatigue,
        "fever": fever,
    }

    prediction = predict_risk(patient)

    explanation = explain_prediction(patient)

    recommendations = generate_recommendations(

        patient,

        prediction["risk_prediction"],

        prediction["confidence"]
    )

    score = prediction["confidence"] * 100

    st.subheader("📊 Risk Dashboard")

    gauge = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            title={"text": "Risk Score"},

            gauge={

                "axis": {

                    "range": [0, 100]
                },

                "steps": [

                    {
                        "range": [0, 40],
                        "color": "lightgreen"
                    },

                    {
                        "range": [40, 75],
                        "color": "orange"
                    },

                    {
                        "range": [75, 100],
                        "color": "red"
                    }
                ]
            }
        )
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Risk Class",
            prediction["risk_prediction"]
        )

    with c2:

        st.metric(
            "Confidence",
            f"{score:.2f}%"
        )

    st.subheader("🧠 AI Explanation")

    st.info(
        explanation["plain_english"]
    )

    if explanation["shap_values"]:

        shap_df = pd.DataFrame(

            {

                "Feature":
                    list(
                        explanation[
                            "shap_values"
                        ].keys()
                    ),

                "Impact":
                    list(
                        explanation[
                            "shap_values"
                        ].values()
                    ),
            }
        )

        chart = px.bar(

            shap_df,

            x="Feature",

            y="Impact",

            title="Top Risk Contributors",
        )

        st.plotly_chart(
            chart,
            use_container_width=True
        )

    st.subheader("✅ Recommendations")

    for item in recommendations["patient_advice"]:

        st.success(item)

    if recommendations["red_flags"]:

        st.subheader("🚨 Red Flags")

        for flag in recommendations["red_flags"]:

            st.error(flag)

    if doctor_mode:

        st.subheader("👨‍⚕️ Doctor Dashboard")

        for item in recommendations["doctor_summary"]:

            st.write("•", item)

    st.subheader("⬇️ Download")

    export = pd.DataFrame([patient])

    csv = export.to_csv(index=False)

    st.download_button(

        "Download Patient Report",

        csv,

        file_name="patient_report.csv",

        mime="text/csv",
    )