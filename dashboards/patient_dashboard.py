import streamlit as st

from modules import history, prediction

from styles import load_css

load_css()

def show():

    st.sidebar.title(" Patient Portal")

    menu = st.sidebar.radio(
        "Navigation",
        [
            " Dashboard",
            " New Assessment",
            " Prediction History",
            " Profile"
        ]
    )

    st.sidebar.markdown("---")

    if st.sidebar.button(" Logout"):

        st.session_state.clear()

        st.rerun()



    if menu == " Dashboard":

        st.title(" Patient Dashboard")

        st.success(
            f"Welcome, {st.session_state.username}!"
        )

        st.markdown(
            """
            ###  Alzheimer's Disease Prediction System

            Welcome to your patient portal.

            From the navigation menu, you can:

            -  Complete a new Alzheimer's assessment
            -  View your previous prediction results
            -  View your profile
            -  Logout securely
            """
        )


    # =====================================================
    # NEW ASSESSMENT
    # =====================================================

    elif menu == " New Assessment":

        prediction.show()


    # =====================================================
    # PREDICTION HISTORY
    # =====================================================

    elif menu == " Prediction History":

        history.show()


    # =====================================================
    # PROFILE
    # =====================================================

    elif menu == " Profile":

        st.title(" My Profile")

        st.markdown(
            "<div class='card'>",
            unsafe_allow_html=True
        )

        st.write(
            f"**Username:** "
            f"{st.session_state.username}"
        )

        st.write(
            f"**Role:** "
            f"{st.session_state.role}"
        )

        if "user_id" in st.session_state:

            st.write(
                f"**User ID:** "
                f"{st.session_state.user_id}"
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )