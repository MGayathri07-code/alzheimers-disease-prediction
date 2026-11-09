# Alzheimer's Disease Risk Prediction Application

A machine learning-based web application that estimates Alzheimer's disease risk using patient demographic, lifestyle, medical, and clinical information.

The application is developed using Python and Streamlit, with a Gradient Boosting Classifier for risk prediction and SQLite for storing user and prediction records.

## Project Overview

Alzheimer's disease is a progressive neurological condition that affects memory, thinking, and behaviour. This project explores how machine learning can be used to identify patterns in patient data and estimate the likelihood of a positive classification.

The application provides separate interfaces for patients and doctors, allowing patients to enter relevant information and view prediction results, while doctors can access available patient prediction records.

**Note:** This is an educational machine learning project. It is not a medical diagnostic system and cannot replace professional medical evaluation.

## Features

- Patient registration and login
- Doctor registration and login
- Separate patient and doctor dashboards
- Patient information input through a web form
- Data preprocessing and feature transformation
- Alzheimer's risk prediction using a trained Gradient Boosting Classifier
- Display of predicted risk category and estimated probability
- Prediction history for patients
- Doctor access to available patient prediction records
- SQLite database integration

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development and machine learning |
| Streamlit | Web application interface |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations |
| Scikit-learn | Model training and evaluation |
| Joblib | Saving and loading the trained model |
| SQLite | Database management |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |

## Machine Learning Workflow

The project follows these steps:

1. **Data Collection:** Obtain the Alzheimer's Disease Dataset from Kaggle.
2. **Exploratory Data Analysis:** Explore the dataset and understand feature distributions and relationships.
3. **Data Preprocessing:** Handle categorical variables and prepare features for model training.
4. **Train-Test Split:** Divide the dataset into training and testing sets.
5. **Model Comparison:** Compare classification algorithms using accuracy, precision, recall, and F1-score.
6. **Model Selection:** Use Gradient Boosting Classifier as the final prediction model.
7. **Model Evaluation:** Evaluate the selected model using a classification report, confusion matrix, and other relevant metrics.
8. **Model Persistence:** Save the trained model using Joblib.
9. **Application Development:** Integrate the trained model into the Streamlit application.

## Dataset

The project uses the **Alzheimer's Disease Dataset** available on Kaggle.

- **Dataset author:** Rabie El Kharoua
- **Publication year:** 2024
- **Dataset:** Alzheimer's Disease Dataset
- **Kaggle URL:** https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset
- **Dataset DOI:** 10.34740/KAGGLE/DSV/8668279
- **File used:** `alzheimers_disease_data.csv`

The dataset contains demographic, lifestyle, medical history, clinical, cognitive, and functional assessment information.

### Dataset Citation

El Kharoua, R. (2024). *Alzheimer's Disease Dataset*. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/8668279

BibTeX citation:

```bibtex
@misc{rabie_el_kharoua_2024,
  title={Alzheimer's Disease Dataset},
  author={Rabie El Kharoua},
  year={2024},
  publisher={Kaggle},
  doi={10.34740/KAGGLE/DSV/8668279},
  url={https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset}
}
```

**Dataset acknowledgment:** The dataset used in this project was created and published by Rabie El Kharoua. All dataset credit belongs to the original author. This project uses the dataset for educational and machine learning purposes.

## Project Structure

```text
alzheimers-disease-prediction/
│
├── dashboards/
│   ├── doctor_dashboard.py
│   └── patient_dashboard.py
│
├── data/
│   └── alzheimers_disease_data.csv
│
├── models/
│   └── alzheimers_model.pkl
│
├── modules/
│   ├── history.py
│   └── prediction.py
│
├── utils/
│   ├── input_form.py
│   ├── predictor.py
│   └── preprocessing.py
│
├── alzheimers_model.py
├── database.py
├── feature_names.pkl
├── login.py
├── register.py
├── styles.py
├── requirements.txt
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/MGayathri07-code/alzheimers-disease-prediction.git
```

### 2. Navigate to the project directory

```bash
cd alzheimers-disease-prediction
```

### 3. Create a virtual environment (optional)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run login.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## Model Information

The final application uses a **Gradient Boosting Classifier**, a supervised machine learning algorithm based on an ensemble of decision trees.

The model is trained using the dataset's available features and saved as a Joblib file for use in the application.

The prediction output includes:

- Predicted risk category
- Estimated probability for the positive class
- Model confidence information

The probability represents the model's estimate based on patterns learned from the training data. It should not be interpreted as a patient's actual probability of developing Alzheimer's disease.

## Limitations

- The model is trained using a single Kaggle dataset.
- Its performance on independent real-world patient populations has not been established.
- Predictions depend on the quality and representativeness of the input data.
- The model is not clinically validated.
- The application is intended for educational and demonstration purposes, not medical diagnosis or treatment decisions.

## Future Improvements

- Integrate a persistent cloud database.
- Improve model validation using independent datasets.
- Add explainable AI techniques such as SHAP.
- Improve application security and user data protection.
- Explore additional machine learning algorithms and optimization techniques.

## Author

**Gayathri**

GitHub: https://github.com/MGayathri07-code

## Disclaimer

This project is developed for educational and research purposes only. It is not intended to diagnose, treat, or prevent Alzheimer's disease or any other medical condition. Always consult qualified healthcare professionals for medical advice and diagnosis.