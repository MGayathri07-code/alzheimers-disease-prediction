import streamlit as st
import pandas as pd

from database import (
    get_all_patients,
    get_all_predictions
)


# =========================================================
# DOCTOR DASHBOARD
# =========================================================

def show():

    # =====================================================
    # CHECK LOGIN
    # =====================================================

    if not st.session_state.get("logged_in", False):

        st.error("Please log in first.")
        st.stop()


    # =====================================================
    # CHECK ROLE
    # =====================================================

    if st.session_state.get("role") != "Doctor":

        st.error("Access denied. Doctor access required.")
        st.stop()


    # =====================================================
    # SESSION STATE
    # =====================================================

    if "doctor_page" not in st.session_state:

        st.session_state.doctor_page = "dashboard"


    # =====================================================
    # SIDEBAR
    # =====================================================

    with st.sidebar:

        st.title("🧠 Alzheimer's System")

        st.markdown("---")

        st.write(
            f" **Dr. {st.session_state.username}**"
        )

        st.write("Role: **Doctor**")

        st.markdown("---")


        # -------------------------------------------------
        # DASHBOARD
        # -------------------------------------------------

        if st.button(
            " Dashboard",
            use_container_width=True
        ):

            st.session_state.doctor_page = "dashboard"
            st.rerun()


        # -------------------------------------------------
        # PATIENTS
        # -------------------------------------------------

        if st.button(
            " Patients",
            use_container_width=True
        ):

            st.session_state.doctor_page = "patients"
            st.rerun()


        # -------------------------------------------------
        # PREDICTIONS
        # -------------------------------------------------

        if st.button(
            " All Predictions",
            use_container_width=True
        ):

            st.session_state.doctor_page = "predictions"
            st.rerun()


        st.markdown("---")


        # -------------------------------------------------
        # LOGOUT
        # -------------------------------------------------

        if st.button(
            " Logout",
            use_container_width=True
        ):

            st.session_state.logged_in = False
            st.session_state.user_id = None
            st.session_state.username = ""
            st.session_state.role = ""

            st.session_state.doctor_page = "dashboard"

            st.rerun()


    # =====================================================
    # DASHBOARD HOME
    # =====================================================

    if st.session_state.doctor_page == "dashboard":

        show_dashboard()


    # =====================================================
    # PATIENTS
    # =====================================================

    elif st.session_state.doctor_page == "patients":

        show_patients()


    # =====================================================
    # PREDICTIONS
    # =====================================================

    elif st.session_state.doctor_page == "predictions":

        show_predictions()


# =========================================================
# DASHBOARD HOME
# =========================================================

def show_dashboard():

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:20px;
        ">

        <h1 style="
            color:#1e3a8a;
            font-size:42px;
        ">
            ️ Doctor Dashboard
        </h1>

        <p style="
            color:#64748b;
            font-size:18px;
        ">
            Alzheimer's Disease Prediction System
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.success(
        f"Welcome, Dr. {st.session_state.username}! "
    )


    # =====================================================
    # GET DATABASE DATA
    # =====================================================

    patients = get_all_patients()

    predictions = get_all_predictions()


    # =====================================================
    # CALCULATE STATISTICS
    # =====================================================

    total_patients = len(patients)

    total_predictions = len(predictions)

    high_risk = 0

    low_risk = 0


    for prediction in predictions:

        result = str(prediction[2]).lower()

        if "high" in result or result == "1":

            high_risk += 1

        else:

            low_risk += 1


    # =====================================================
    # STATISTICS
    # =====================================================

    st.markdown("###  Overview")


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            " Total Patients",
            total_patients
        )


    with col2:

        st.metric(
            " Total Predictions",
            total_predictions
        )


    with col3:

        st.metric(
            "🔴 High Risk",
            high_risk
        )


    with col4:

        st.metric(
            "🟢 Low Risk",
            low_risk
        )


    # =====================================================
    # INFORMATION
    # =====================================================

    st.markdown("---")

    st.info(
        """
        ###  Doctor Portal

        From this dashboard you can:

        • View registered patients

        • Review prediction results

        • Monitor high-risk predictions

        • Review prediction confidence

        • Analyze patient assessment history
        """
    )


# =========================================================
# PATIENT LIST
# =========================================================

def show_patients():

    st.title(" Registered Patients")

    st.write(
        "View all patients registered in the system."
    )


    patients = get_all_patients()


    # =====================================================
    # NO PATIENTS
    # =====================================================

    if not patients:

        st.info(
            "No patients are registered yet."
        )

        return


    # =====================================================
    # CREATE DATAFRAME
    # =====================================================

    patient_data = []


    for patient in patients:

        patient_data.append({

            "Patient ID": patient[0],

            "Username": patient[1],

            "Registered On": patient[2]

        })


    patient_df = pd.DataFrame(
        patient_data
    )


    st.dataframe(
        patient_df,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# ALL PREDICTIONS
# =========================================================

def show_predictions():

    st.title(" All Prediction Results")

    st.write(
        "Review prediction results for all patients."
    )


    predictions = get_all_predictions()


    # =====================================================
    # NO PREDICTIONS
    # =====================================================

    if not predictions:

        st.info(
            "No predictions have been recorded yet."
        )

        return


    # =====================================================
    # CREATE DATAFRAME
    # =====================================================

    prediction_data = []


    for result in predictions:

        prediction_data.append({

            "Prediction ID": result[0],

            "Patient": result[1],

            "Prediction": result[2],

            "Confidence": f"{result[3]:.2f}%",

            "Alzheimer Probability":
                f"{result[4] * 100:.2f}%",

            "Date": result[5]

        })


    prediction_df = pd.DataFrame(
        prediction_data
    )


    # =====================================================
    # FILTER
    # =====================================================

    st.markdown("###  Filter Results")


    filter_option = st.selectbox(
        "Prediction Result",
        [
            "All",
            "High Risk",
            "Low Risk"
        ]
    )


    filtered_df = prediction_df


    if filter_option == "High Risk":

        filtered_df = prediction_df[
            prediction_df["Prediction"]
            .astype(str)
            .str.contains(
                "high",
                case=False,
                na=False
            )
        ]


    elif filter_option == "Low Risk":

        filtered_df = prediction_df[
            prediction_df["Prediction"]
            .astype(str)
            .str.contains(
                "low",
                case=False,
                na=False
            )
        ]


    # =====================================================
    # DISPLAY RESULTS
    # =====================================================

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# END
# =========================================================