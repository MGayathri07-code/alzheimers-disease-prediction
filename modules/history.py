import streamlit as st
import pandas as pd

from database import get_prediction_history


def show():


    st.title(" Prediction History")

    st.write(
        "View your previous Alzheimer's disease "
        "assessment results."
    )

    st.markdown("---")



    patient_id = st.session_state.get(
        "user_id"
    )



    if patient_id is None:

        st.error(
            "Unable to identify the logged-in patient."
        )

        return



    try:

        history = get_prediction_history(
            patient_id
        )

    except Exception as e:

        st.error(
            f"Unable to load prediction history: {e}"
        )

        return


    if not history:

        st.info(
            " You do not have any prediction "
            "history yet."
        )

        st.write(
            "Complete a new assessment from "
            "** New Assessment** to see your "
            "results here."
        )

        return


    df = pd.DataFrame(
        history,
        columns=[
            "Prediction",
            "Confidence",
            "Date"
        ]
    )


    df["Confidence"] = df["Confidence"].apply(
        lambda x: f"{float(x):.2f}%"
    )


    total_predictions = len(df)

    high_risk = sum(
        1
        for row in history
        if str(row[0]).lower()
        in ["positive", "high risk"]
    )

    low_risk = total_predictions - high_risk


    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Assessments",
            total_predictions
        )

    with col2:

        st.metric(
            "High Risk",
            high_risk
        )

    with col3:

        st.metric(
            "Low Risk",
            low_risk
        )


    st.markdown("---")


    st.subheader(" Previous Assessments")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


    latest = history[0]

    latest_prediction = latest[0]
    latest_confidence = float(latest[1])
    latest_date = latest[2]


    st.markdown("---")

    st.subheader(" Latest Assessment")


    if str(latest_prediction).lower() in [
        "positive",
        "high risk"
    ]:

        st.error(
            f"⚠️ Latest Result: {latest_prediction}"
        )

    else:

        st.success(
            f" Latest Result: {latest_prediction}"
        )


    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Confidence",
            f"{latest_confidence:.2f}%"
        )

    with col2:

        st.metric(
            "Assessment Date",
            str(latest_date)
        )


    # =====================================================
    # DISCLAIMER
    # =====================================================

    st.warning(
        """
        **Disclaimer:** Previous prediction results are
        provided for informational and educational purposes
        only. They should not be interpreted as a medical
        diagnosis.
        """
    )