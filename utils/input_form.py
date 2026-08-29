import streamlit as st
def patient_form():
    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='section-title'> Patient Information</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=40,
            max_value=100,
            value=65
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        ethnicity = st.selectbox(
            "Ethnicity",
            [
                "Caucasian",
                "African American",
                "Asian",
                "Other"
            ]
        )

    with col2:

        education = st.selectbox(
            "Education Level",
            [0, 1, 2, 3]
        )

        bmi = st.number_input(
            "BMI",
            min_value=10.0,
            max_value=50.0,
            value=25.0
        )

    st.markdown("</div>", unsafe_allow_html=True)


    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='section-title'> Lifestyle Factors</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        smoking = st.selectbox(
            "Smoking",
            ["No", "Yes"]
        )

        alcohol = st.number_input(
            "Alcohol Consumption",
            value=0.0
        )

        physical = st.number_input(
            "Physical Activity",
            value=0.0
        )

    with col2:

        diet = st.number_input(
            "Diet Quality",
            value=0.0
        )

        sleep = st.number_input(
            "Sleep Quality",
            value=0.0
        )

    st.markdown("</div>", unsafe_allow_html=True)


    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='section-title'> Medical History</div>",
        unsafe_allow_html=True
    )

    family = st.selectbox(
        "Family History of Alzheimer's",
        ["No", "Yes"]
    )

    cardio = st.selectbox(
        "Cardiovascular Disease",
        ["No", "Yes"]
    )

    diabetes = st.selectbox(
        "Diabetes",
        ["No", "Yes"]
    )

    depression = st.selectbox(
        "Depression",
        ["No", "Yes"]
    )

    head = st.selectbox(
        "Head Injury",
        ["No", "Yes"]
    )

    hypertension = st.selectbox(
        "Hypertension",
        ["No", "Yes"]
    )

    st.markdown("</div>", unsafe_allow_html=True)



    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='section-title'> Clinical Measurements</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        sbp = st.number_input(
            "Systolic BP",
            value=120
        )

        dbp = st.number_input(
            "Diastolic BP",
            value=80
        )

        chol = st.number_input(
            "Total Cholesterol",
            value=180.0
        )

    with col2:

        ldl = st.number_input(
            "LDL",
            value=100.0
        )

        hdl = st.number_input(
            "HDL",
            value=50.0
        )

        tri = st.number_input(
            "Triglycerides",
            value=150.0
        )

    st.markdown("</div>", unsafe_allow_html=True)



    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='section-title'> Cognitive Assessment</div>",
        unsafe_allow_html=True
    )

    mmse = st.number_input(
        "MMSE",
        value=25.0
    )

    functional = st.number_input(
        "Functional Assessment",
        value=5.0
    )

    adl = st.number_input(
        "Activities of Daily Living (ADL)",
        value=5.0
    )

    st.markdown("</div>", unsafe_allow_html=True)


    st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='section-title'> Symptoms</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        memory = st.selectbox(
            "Memory Complaints",
            ["No", "Yes"]
        )

        behavior = st.selectbox(
            "Behavioral Problems",
            ["No", "Yes"]
        )

        confusion = st.selectbox(
            "Confusion",
            ["No", "Yes"]
        )

        disorientation = st.selectbox(
            "Disorientation",
            ["No", "Yes"]
        )

    with col2:

        personality = st.selectbox(
            "Personality Changes",
            ["No", "Yes"]
        )

        difficulty = st.selectbox(
            "Difficulty Completing Tasks",
            ["No", "Yes"]
        )

        forgetfulness = st.selectbox(
            "Forgetfulness",
            ["No", "Yes"]
        )

    st.markdown("</div>", unsafe_allow_html=True)


    return {

        "Age": age,

        "Gender": gender,

        "Ethnicity": ethnicity,

        "EducationLevel": education,

        "BMI": bmi,

        "Smoking": smoking,

        "AlcoholConsumption": alcohol,

        "PhysicalActivity": physical,

        "DietQuality": diet,

        "SleepQuality": sleep,

        "FamilyHistoryAlzheimers": family,

        "CardiovascularDisease": cardio,

        "Diabetes": diabetes,

        "Depression": depression,

        "HeadInjury": head,

        "Hypertension": hypertension,

        "SystolicBP": sbp,

        "DiastolicBP": dbp,

        "CholesterolTotal": chol,

        "CholesterolLDL": ldl,

        "CholesterolHDL": hdl,

        "CholesterolTriglycerides": tri,

        "MMSE": mmse,

        "FunctionalAssessment": functional,

        "MemoryComplaints": memory,

        "BehavioralProblems": behavior,

        "ADL": adl,

        "Confusion": confusion,

        "Disorientation": disorientation,

        "PersonalityChanges": personality,

        "DifficultyCompletingTasks": difficulty,

        "Forgetfulness": forgetfulness
    }
