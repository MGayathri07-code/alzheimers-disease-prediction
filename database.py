import sqlite3
from datetime import datetime

# DATABASE CONFIGURATION

DATABASE_NAME = "alzheimers.db"

# GET DATABASE CONNECTION

def get_connection():

    conn = sqlite3.connect(
        DATABASE_NAME,
        check_same_thread=False
    )

    return conn

# INITIALIZE DATABASE

def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    # USERS TABLE

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            role TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    # PREDICTIONS TABLE

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            patient_id INTEGER NOT NULL,

            prediction TEXT NOT NULL,

            confidence REAL NOT NULL,

            alzheimer_probability REAL NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (patient_id)
                REFERENCES users(id)

        )
    """)

    conn.commit()
    conn.close()

# CREATE USER

def create_user(username, password, role):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users
            (
                username,
                password,
                role
            )

            VALUES (?, ?, ?)
            """,
            (
                username,
                password,
                role
            )
        )

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


# VERIFY LOGIN

def verify_login(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            username,
            password,
            created_at,
            role

        FROM users

        WHERE username = ?
        AND password = ?
        """,
        (
            username,
            password
        )
    )

    user = cursor.fetchone()

    conn.close()

    return user

# GET USER BY ID

def get_user_by_id(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            username,
            password,
            created_at,
            role

        FROM users

        WHERE id = ?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# =========================================================
# SAVE PREDICTION
# =========================================================

def save_prediction(
    patient_id,
    prediction,
    confidence,
    alzheimer_probability
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO predictions
        (
            patient_id,
            prediction,
            confidence,
            alzheimer_probability,
            created_at
        )

        VALUES (?, ?, ?, ?, ?)
        """,
        (
            patient_id,
            prediction,
            confidence,
            alzheimer_probability,
            datetime.now()
        )
    )

    conn.commit()
    conn.close()


# =========================================================
# GET PATIENT PREDICTION HISTORY
# =========================================================

def get_prediction_history(patient_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            prediction,
            confidence,
            created_at

        FROM predictions

        WHERE patient_id = ?

        ORDER BY created_at DESC
        """,
        (patient_id,)
    )

    history = cursor.fetchall()

    conn.close()

    return history


# =========================================================
# GET ALL PREDICTIONS
# FOR DOCTOR DASHBOARD
# =========================================================

def get_all_predictions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            predictions.id,
            users.username,
            predictions.prediction,
            predictions.confidence,
            predictions.alzheimer_probability,
            predictions.created_at

        FROM predictions

        JOIN users
        ON predictions.patient_id = users.id

        ORDER BY predictions.created_at DESC
        """
    )

    predictions = cursor.fetchall()

    conn.close()

    return predictions


# =========================================================
# GET ALL PATIENTS
# =========================================================

def get_all_patients():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            username,
            created_at

        FROM users

        WHERE role = 'Patient'

        ORDER BY created_at DESC
        """
    )

    patients = cursor.fetchall()

    conn.close()

    return patients


# =========================================================
# INITIALIZE DATABASE
# =========================================================

initialize_database()