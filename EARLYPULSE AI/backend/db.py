import sqlite3
from pathlib import Path
from datetime import datetime

from backend.config import BASE_DIR

DB_PATH = BASE_DIR / "artifacts" / "med_ai.db"


def get_connection():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    return conn


def init_db():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS predictions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id TEXT,

            age INTEGER,
            sex TEXT,
            bmi REAL,

            smoking TEXT,
            alcohol TEXT,
            exercise_level TEXT,

            heart_rate INTEGER,
            systolic_bp INTEGER,
            diastolic_bp INTEGER,

            blood_sugar REAL,
            cholesterol REAL,

            family_history TEXT,
            fatigue TEXT,
            fever TEXT,

            risk_prediction INTEGER,
            confidence REAL,

            urgency TEXT,

            created_at TEXT

        )
        """
    )

    conn.commit()

    conn.close()


def save_prediction(

    user_id: str,

    patient_data: dict,

    prediction: int,

    confidence: float,

    urgency: str,

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO predictions (

            user_id,

            age,
            sex,
            bmi,

            smoking,
            alcohol,
            exercise_level,

            heart_rate,
            systolic_bp,
            diastolic_bp,

            blood_sugar,
            cholesterol,

            family_history,
            fatigue,
            fever,

            risk_prediction,
            confidence,

            urgency,

            created_at

        )

        VALUES (

            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?

        )
        """,
        (
            user_id,

            patient_data["age"],
            patient_data["sex"],
            patient_data["bmi"],

            patient_data["smoking"],
            patient_data["alcohol"],
            patient_data["exercise_level"],

            patient_data["heart_rate"],
            patient_data["systolic_bp"],
            patient_data["diastolic_bp"],

            patient_data["blood_sugar"],
            patient_data["cholesterol"],

            patient_data["family_history"],
            patient_data["fatigue"],
            patient_data["fever"],

            prediction,
            confidence,

            urgency,

            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        ),
    )

    conn.commit()

    conn.close()


def get_history(user_id: str):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *

        FROM predictions

        WHERE user_id = ?

        ORDER BY created_at DESC
        """,
        (user_id,),
    )

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def get_recent_predictions(limit: int = 10):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *

        FROM predictions

        ORDER BY created_at DESC

        LIMIT ?
        """,
        (limit,),
    )

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def clear_history():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM predictions
        """
    )

    conn.commit()

    conn.close()


if __name__ == "__main__":

    init_db()

    print("✅ Database initialized successfully.")

    print(f"📁 Database location: {DB_PATH}")