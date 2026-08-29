import streamlit as st

from database import create_user


# =========================================================
# REGISTRATION PAGE
# =========================================================

def show_register():

    # =====================================================
    # TITLE
    # =====================================================

    st.markdown(
        """
        <h1 style="
            text-align:center;
            color:#1e3a8a;
        ">
            🧠 Create Account
        </h1>
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
            Alzheimer's Disease Prediction System
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")


    # =====================================================
    # ACCOUNT INFORMATION
    # =====================================================

    st.subheader(" Account Information")


    email = st.text_input(
        "Email",
        placeholder="Enter your email"
    )


    password = st.text_input(
        "Password",
        type="password",
        placeholder="Create a password"
    )


    confirm_password = st.text_input(
        "Confirm Password",
        type="password",
        placeholder="Re-enter your password"
    )


    # =====================================================
    # ROLE
    # =====================================================

    st.subheader(" Account Type")


    role = st.selectbox(
        "Select your role",
        [
            "Patient",
            "Doctor"
        ]
    )


    # =====================================================
    # CREATE ACCOUNT
    # =====================================================

    create_account = st.button(
        " Create Account",
        use_container_width=True
    )


    if create_account:

        # -------------------------------------------------
        # VALIDATION
        # -------------------------------------------------

        if not email:

            st.warning(
                "Please enter your email."
            )

        elif not password:

            st.warning(
                "Please enter a password."
            )

        elif password != confirm_password:

            st.error(
                "❌ Passwords do not match."
            )

        elif len(password) < 6:

            st.warning(
                "Password must contain at least "
                "6 characters."
            )

        else:

            # ---------------------------------------------
            # CREATE USER
            # ---------------------------------------------

            account_created = create_user(
                email,
                password,
                role
            )


            if account_created:

                st.success(
                    "✅ Account created successfully!"
                )

                st.info(
                    "Your account has been created. "
                    "You can now log in."
                )

                # -----------------------------------------
                # RETURN TO LOGIN
                # -----------------------------------------

                if st.button(
                    " Go to Login",
                    use_container_width=True
                ):

                    st.session_state.page = "login"

                    st.rerun()

            else:

                st.error(
                    "❌ An account with this email "
                    "already exists."
                )


    # =====================================================
    # BACK TO LOGIN
    # =====================================================

    st.markdown("---")

    if st.button(
        "← Back to Login",
        use_container_width=True
    ):

        st.session_state.page = "login"

        st.rerun()
