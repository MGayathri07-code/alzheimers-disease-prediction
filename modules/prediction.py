import streamlit as st

from utils.input_form import patient_form
from utils.preprocessing import preprocess
from utils.predictor import get_prediction_result
from database import save_prediction


# =========================================================
# PREDICTION PAGE
# =========================================================

def show():

    # =====================================================
    # GET LOGGED-IN PATIENT ID
    # =====================================================

    patient_id = st.session_state.get("user_id")

    if patient_id is None:

        st.error(
            "Patient information not found. "
            "Please log in again."
        )

        st.stop()


    # =====================================================
    # PAGE TITLE
    # =====================================================

    st.markdown(
        "<div class='main-title'>"
        "🧠 Alzheimer's Disease Assessment"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>"
        "AI-powered early risk assessment using "
        "a Gradient Boosting Machine Learning model"
        "</div>",
        unsafe_allow_html=True
    )


    # =====================================================
    # SIDEBAR
    # =====================================================

    with st.sidebar:

        st.title("🧠 About")

        st.info(
            """
            This application predicts the likelihood
            of Alzheimer's disease using a Machine
            Learning model.

            **Model:** Gradient Boosting Classifier

            **Purpose:** Educational / Research /
            Demonstration

            ⚠️ This application is not a substitute
            for professional medical advice.
            """
        )

        st.markdown("---")

        if "username" in st.session_state:

            st.write(
                f"👤 Logged in as: "
                f"**{st.session_state.username}**"
            )

        if "role" in st.session_state:

            st.write(
                f"Role: **{st.session_state.role}**"
            )


    # =====================================================
    # PATIENT INPUT FORM
    # =====================================================

    patient_data = patient_form()


    # =====================================================
    # PREDICTION BUTTON
    # =====================================================

    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([2, 2, 2])

    with col2:

        predict_button = st.button(
            "🔮 Predict Disease",
            use_container_width=True
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


    # =====================================================
    # MAKE PREDICTION
    # =====================================================

    if predict_button:

        with st.spinner(
            "🔄 Analyzing patient data..."
        ):

            try:

                # -----------------------------------------
                # STEP 1: PREPROCESS INPUT
                # -----------------------------------------

                input_df = preprocess(
                    patient_data
                )


                # -----------------------------------------
                # STEP 2: MAKE MODEL PREDICTION
                # -----------------------------------------

                (
                    prediction,
                    alzheimer_probability,
                    confidence
                ) = get_prediction_result(
                    input_df
                )


            except Exception as e:

                st.error(
                    f"An error occurred while making "
                    f"the prediction: {e}"
                )

                st.stop()


        # =================================================
        # CONVERT VALUES TO PERCENTAGES
        # =================================================

        confidence_percentage = confidence * 100

        alzheimer_percentage = (
            alzheimer_probability*100
        )


        # =================================================
        # CONVERT PREDICTION TO TEXT
        # =================================================

        if prediction == 1:

            prediction_text = "High Risk"

        else:

            prediction_text = "Low Risk"


        # =================================================
        # SAVE PREDICTION TO DATABASE
        # =================================================

        try:

            save_prediction(
                patient_id=patient_id,
                prediction=prediction_text,
                confidence=confidence_percentage,
                alzheimer_probability=alzheimer_percentage
            )

            saved_successfully = True

        except Exception as e:

            saved_successfully = False

            st.error(
                f"Prediction was generated, but "
                f"could not be saved to the database: {e}"
            )


        # =================================================
        # DISPLAY RESULT
        # =================================================

        st.markdown(
            "<div class='card'>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div class='section-title'>"
            "📊 Prediction Result"
            "</div>",
            unsafe_allow_html=True
        )


        # -------------------------------------------------
        # HIGH RISK RESULT
        # -------------------------------------------------

        if prediction == 1:

            st.markdown(
                """
                <div class='warning-box'>
                ⚠️ High Risk of Alzheimer's Disease Detected
                </div>
                """,
                unsafe_allow_html=True
            )


        # -------------------------------------------------
        # LOW RISK RESULT
        # -------------------------------------------------

        else:

            st.markdown(
                """
                <div class='success-box'>
                ✅ Low Risk of Alzheimer's Disease
                </div>
                """,
                unsafe_allow_html=True
            )


        # =================================================
        # CONFIDENCE
        # =================================================

        st.metric(
            "Prediction Confidence",
            f"{confidence_percentage:.2f}%"
        )


        # =================================================
        # ALZHEIMER'S PROBABILITY
        # =================================================

        st.write(
            f"**Alzheimer's Probability:** "
            f"{alzheimer_percentage:.2f}%"
        )

        st.progress(
            float(alzheimer_probability)
        )


        # =================================================
        # DATABASE STATUS
        # =================================================

        if saved_successfully:

            st.success(
                "✅ Your prediction has been saved "
                "to your prediction history."
            )


        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


        # =================================================
        # DISCLAIMER
        # =================================================

        st.markdown(
            "<div class='card'>",
            unsafe_allow_html=True
        )

        st.warning(
            """
            **Disclaimer:** This application is intended
            for educational and research purposes only.

            It should not be used as a medical diagnosis.

            Please consult a qualified healthcare
            professional for proper medical evaluation.
            """
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )
