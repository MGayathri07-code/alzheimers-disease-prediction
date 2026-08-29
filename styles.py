import streamlit as st

def load_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #1f3b73;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #445;
        margin-bottom: 25px;
    }

    .card {
        background-color: white;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .section-title {
        color: #0b5ed7;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    div.stButton > button {
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        color: white;
        font-size: 18px;
        font-weight: 700;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        width: 100%;
    }

    .success-box {
        background-color: #d1fae5;
        color: #065f46;
        padding: 18px;
        border-radius: 14px;
        font-size: 18px;
        font-weight: 600;
    }

    .warning-box {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 18px;
        border-radius: 14px;
        font-size: 18px;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

