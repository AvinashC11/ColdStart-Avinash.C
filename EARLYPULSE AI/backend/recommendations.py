DISCLAIMER = (
    "⚠️ This application is an educational AI prototype and is not "
    "a certified medical device. The results do not constitute a "
    "medical diagnosis or treatment recommendation. Always consult "
    "a qualified healthcare professional."
)


RISK_BADGES = {
    "LOW": "🟢 Low Risk",
    "MEDIUM": "🟠 Moderate Risk",
    "HIGH": "🔴 High Risk",
}


def _risk_level(confidence: float):

    if confidence < 0.40:
        return "LOW"

    elif confidence < 0.75:
        return "MEDIUM"

    return "HIGH"


def generate_recommendations(
    patient_data: dict,
    risk_prediction: int,
    confidence: float,
):

    urgency = _risk_level(confidence)

    patient_advice = []

    doctor_summary = []

    red_flags = []

    lifestyle_score = 100

    # -------------------------
    # General recommendations
    # -------------------------

    patient_advice.extend(
        [
            "Maintain a balanced diet rich in fruits and vegetables.",
            "Sleep for at least 7–8 hours daily.",
            "Drink sufficient water throughout the day.",
            "Engage in regular physical activity.",
        ]
    )

    # -------------------------
    # Lifestyle analysis
    # -------------------------

    if patient_data["smoking"] == "Yes":

        patient_advice.append(
            "Consider reducing or quitting smoking with professional guidance."
        )

        lifestyle_score -= 20

    if patient_data["alcohol"] == "Yes":

        patient_advice.append(
            "Limit alcohol consumption and follow medical guidelines."
        )

        lifestyle_score -= 10

    if patient_data["exercise_level"] == "Low":

        patient_advice.append(
            "Increase physical activity gradually to at least 30 minutes daily."
        )

        lifestyle_score -= 15

    elif patient_data["exercise_level"] == "Medium":

        lifestyle_score -= 5

    # -------------------------
    # Health metrics checks
    # -------------------------

    if patient_data["blood_sugar"] >= 180:

        red_flags.append(
            "Elevated blood sugar level detected."
        )

    if patient_data["cholesterol"] >= 240:

        red_flags.append(
            "High cholesterol level detected."
        )

    if patient_data["systolic_bp"] >= 180:

        red_flags.append(
            "Critically high blood pressure detected."
        )

    if patient_data["heart_rate"] >= 130:

        red_flags.append(
            "Unusually high heart rate detected."
        )

    if patient_data["family_history"] == "Yes":

        patient_advice.append(
            "Schedule regular preventive health check-ups due to family history."
        )

    # -------------------------
    # Urgency recommendations
    # -------------------------

    if urgency == "LOW":

        patient_advice.append(
            "Continue your current healthy lifestyle habits."
        )

        patient_advice.append(
            "Consider an annual preventive health screening."
        )

    elif urgency == "MEDIUM":

        patient_advice.append(
            "Consider consulting a healthcare professional for a preventive check-up."
        )

        patient_advice.append(
            "Monitor blood pressure, sugar, and cholesterol regularly."
        )

    else:

        patient_advice.append(
            "Seek professional medical evaluation as soon as possible."
        )

        patient_advice.append(
            "Do not rely solely on this AI assessment."
        )

    escalation_required = len(red_flags) > 0

    # -------------------------
    # Doctor summary
    # -------------------------

    doctor_summary.extend(
        [
            f"Predicted risk class: {risk_prediction}",
            f"Confidence score: {confidence:.2f}",
            f"Urgency level: {urgency}",
            f"Health score: {lifestyle_score}/100",
        ]
    )

    if red_flags:

        doctor_summary.append(
            "Red flags identified:"
        )

        doctor_summary.extend(red_flags)

    # -------------------------
    # Return response
    # -------------------------

    return {
        "risk_badge": RISK_BADGES[urgency],
        "urgency": urgency,
        "confidence": confidence,
        "health_score": lifestyle_score,
        "patient_advice": patient_advice,
        "doctor_summary": doctor_summary,
        "red_flags": red_flags,
        "escalation_required": escalation_required,
        "disclaimer": DISCLAIMER,
    }