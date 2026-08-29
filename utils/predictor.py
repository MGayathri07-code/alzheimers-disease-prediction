import joblib


# ---------------------------------------------------------
# Load the trained model
# ---------------------------------------------------------

MODEL_PATH = "models/alzheimers_model.pkl"

model = joblib.load(MODEL_PATH)


# ---------------------------------------------------------
# Make Prediction
# ---------------------------------------------------------

def predict(input_df):
    """
    Make Alzheimer's disease prediction.

    Parameters
    ----------
    input_df : pandas.DataFrame
        Preprocessed patient data.

    Returns
    -------
    prediction : numpy.ndarray
        Predicted class (0 or 1).

    probability : numpy.ndarray
        Prediction probabilities for both classes.
    """

    # Prediction
    prediction = model.predict(input_df)

    # Prediction probability
    probability = model.predict_proba(input_df)

    return prediction, probability


# ---------------------------------------------------------
# Get Prediction Details
# ---------------------------------------------------------

def get_prediction_result(input_df):

    prediction, probability = predict(input_df)

    # Predicted class
    predicted_class = int(prediction[0])

    # Probability of Alzheimer's
    alzheimer_probability = float(
        probability[0][1]
    )

    # Confidence of predicted class
    confidence = float(
        probability[0].max()
    )

    return (
        predicted_class,
        alzheimer_probability,
        confidence
    )