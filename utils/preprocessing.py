import pandas as pd


def yes_no_to_int(value):
    """
    Convert Yes/No values into 1/0.
    Yes = 1
    No  = 0
    """
    return 1 if value == "Yes" else 0


def preprocess(data):
    """
    Convert the patient input dictionary into
    the numeric DataFrame required by the ML model.
    """

    # ---------------------------------------------------------
    # Convert Gender
    # ---------------------------------------------------------

    gender = 1 if data["Gender"] == "Male" else 0

    # ---------------------------------------------------------
    # Convert Ethnicity
    # ---------------------------------------------------------

    ethnicity_map = {
        "Caucasian": 0,
        "African American": 1,
        "Asian": 2,
        "Other": 3
    }

    ethnicity = ethnicity_map[data["Ethnicity"]]

    # ---------------------------------------------------------
    # Convert Yes/No variables
    # ---------------------------------------------------------

    smoking = yes_no_to_int(data["Smoking"])

    family = yes_no_to_int(
        data["FamilyHistoryAlzheimers"]
    )

    cardio = yes_no_to_int(
        data["CardiovascularDisease"]
    )

    diabetes = yes_no_to_int(
        data["Diabetes"]
    )

    depression = yes_no_to_int(
        data["Depression"]
    )

    head = yes_no_to_int(
        data["HeadInjury"]
    )

    hypertension = yes_no_to_int(
        data["Hypertension"]
    )

    memory = yes_no_to_int(
        data["MemoryComplaints"]
    )

    behavior = yes_no_to_int(
        data["BehavioralProblems"]
    )

    confusion = yes_no_to_int(
        data["Confusion"]
    )

    disorientation = yes_no_to_int(
        data["Disorientation"]
    )

    personality = yes_no_to_int(
        data["PersonalityChanges"]
    )

    difficulty = yes_no_to_int(
        data["DifficultyCompletingTasks"]
    )

    forgetfulness = yes_no_to_int(
        data["Forgetfulness"]
    )

    # ---------------------------------------------------------
    # Create Model Input DataFrame
    # ---------------------------------------------------------

    input_df = pd.DataFrame({

        "Age": [
            data["Age"]
        ],

        "Gender": [
            gender
        ],

        "Ethnicity": [
            ethnicity
        ],

        "EducationLevel": [
            data["EducationLevel"]
        ],

        "BMI": [
            data["BMI"]
        ],

        "Smoking": [
            smoking
        ],

        "AlcoholConsumption": [
            data["AlcoholConsumption"]
        ],

        "PhysicalActivity": [
            data["PhysicalActivity"]
        ],

        "DietQuality": [
            data["DietQuality"]
        ],

        "SleepQuality": [
            data["SleepQuality"]
        ],

        "FamilyHistoryAlzheimers": [
            family
        ],

        "CardiovascularDisease": [
            cardio
        ],

        "Diabetes": [
            diabetes
        ],

        "Depression": [
            depression
        ],

        "HeadInjury": [
            head
        ],

        "Hypertension": [
            hypertension
        ],

        "SystolicBP": [
            data["SystolicBP"]
        ],

        "DiastolicBP": [
            data["DiastolicBP"]
        ],

        "CholesterolTotal": [
            data["CholesterolTotal"]
        ],

        "CholesterolLDL": [
            data["CholesterolLDL"]
        ],

        "CholesterolHDL": [
            data["CholesterolHDL"]
        ],

        "CholesterolTriglycerides": [
            data["CholesterolTriglycerides"]
        ],

        "MMSE": [
            data["MMSE"]
        ],

        "FunctionalAssessment": [
            data["FunctionalAssessment"]
        ],

        "MemoryComplaints": [
            memory
        ],

        "BehavioralProblems": [
            behavior
        ],

        "ADL": [
            data["ADL"]
        ],

        "Confusion": [
            confusion
        ],

        "Disorientation": [
            disorientation
        ],

        "PersonalityChanges": [
            personality
        ],

        "DifficultyCompletingTasks": [
            difficulty
        ],

        "Forgetfulness": [
            forgetfulness
        ]
    })

    return input_df