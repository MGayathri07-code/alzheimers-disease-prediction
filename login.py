
import streamlit as st

from database import verify_login
from dashboards import doctor_dashboard
from dashboards import patient_dashboard
from register import show_register


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Alzheimer's Disease Prediction",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "username" not in st.session_state:
    st.session_state.username = ""

if "role" not in st.session_state:
    st.session_state.role = ""

if "page" not in st.session_state:
    st.session_state.page = "login"


# =========================================================
# IF USER IS LOGGED IN
# =========================================================

if st.session_state.logged_in:

    if st.session_state.role == "Doctor":

        doctor_dashboard.show()

        st.stop()

    elif st.session_state.role == "Patient":

        patient_dashboard.show()

        st.stop()


# =========================================================
# SHOW REGISTRATION PAGE
# =========================================================

if st.session_state.page == "register":

    show_register()

    st.stop()


# =========================================================
# LOGIN PAGE
# =========================================================

st.markdown(
    """
    <h1 style="
        text-align:center;
        color:#1e3a8a;
    ">
        🧠 Alzheimer's Disease
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h2 style="
        text-align:center;
        color:#1e3a8a;
    ">
        Prediction System
    </h2>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        text-align:center;
        color:#64748b;
        font-size:17px;
    ">
        AI-powered early risk assessment
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.subheader(" Login")


# =========================================================
# LOGIN INPUTS
# =========================================================

email = st.text_input(
    "Email",
    placeholder="Enter your email"
)

password = st.text_input(
    "Password",
    type="password",
    placeholder="Enter your password"
)


# =========================================================
# LOGIN BUTTON
# =========================================================

login_button = st.button(
    " Login",
    use_container_width=True
)


# =========================================================
# LOGIN PROCESS
# =========================================================

if login_button:

    if not email:

        st.warning(
            "Please enter your email."
        )

    elif not password:

        st.warning(
            "Please enter your password."
        )

    else:

        user = verify_login(
            email,
            password
        )

        if user:

            # ---------------------------------------------
            # STORE USER INFORMATION
            # ---------------------------------------------

            st.session_state.logged_in = True

            st.session_state.user_id = user[0]

            st.session_state.username = user[1]

            st.session_state.role = user[4]

            # ---------------------------------------------
            # GO TO DASHBOARD
            # ---------------------------------------------

            st.rerun()

        else:

            st.error(
                "❌ Invalid email or password."
            )


# =========================================================
# REGISTER SECTION
# =========================================================

st.markdown("---")

st.markdown(
    "<p style='text-align:center;'>"
    "Don't have an account?"
    "</p>",
    unsafe_allow_html=True
)


register_button = st.button(
    " Create New Account",
    use_container_width=True
)


if register_button:

    st.session_state.page = "register"

    st.rerun()


# =========================================================
# DISCLAIMER
# =========================================================

st.markdown(
    """
    <div style="
        text-align:center;
        color:#64748b;
        font-size:13px;
        margin-top:25px;
    ">
        This application is intended for educational
        and research purposes only.<br>
        It is not a substitute for professional
        medical advice.
    </div>
    """,
    unsafe_allow_html=True
)
