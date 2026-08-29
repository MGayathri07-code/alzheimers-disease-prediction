import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder

# Load dataset

df = pd.read_csv("data/alzheimers_disease_data.csv")

# Display dataset shape
print("Dataset Shape:", df.shape)

# Display first 5 rows

print(df.head())

df.drop(columns=["PatientID", "DoctorInCharge"], inplace=True)
df['Ethnicity'] = df['Ethnicity'].astype(str)

# Dataset information
df.info()

# Statistical summary

print(df.describe())

# Check missing values

print(df.isnull().sum())

# Check duplicates

print("Duplicate Rows:", df.duplicated().sum())

num_cols = [
    'Age', 'BMI', 'AlcoholConsumption', 'PhysicalActivity',
    'DietQuality', 'SleepQuality', 'SystolicBP', 'DiastolicBP',
    'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL',
    'CholesterolTriglycerides', 'MMSE',
    'FunctionalAssessment', 'ADL'
]
outlier_summary = {}

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    outlier_summary[col] = len(outliers)

# outlier_summary

df[num_cols].hist(figsize=(16,12), bins=20)
plt.tight_layout()

cols = ['Age', 'BMI', 'MMSE', 'FunctionalAssessment', 'ADL']

for col in cols:
    plt.figure(figsize=(5,3))
    sns.boxplot(x=df[col])
    plt.title(col)
    plt.show()

cat_cols = [
    'Gender',
    'EducationLevel',
    'Smoking',
    'FamilyHistoryAlzheimers',
    'CardiovascularDisease',
    'Diabetes',
    'Depression',
    'HeadInjury',
    'Hypertension',
    'MemoryComplaints',
    'BehavioralProblems',
    'Confusion',
    'Disorientation',
    'PersonalityChanges',
    'DifficultyCompletingTasks',
    'Forgetfulness',
    'Diagnosis'
]

fig, axes = plt.subplots(6, 3, figsize=(18, 24))
axes = axes.flatten()

for i, col in enumerate(cat_cols):
    ax = sns.countplot(data=df, x=col, ax=axes[i],
        hue=col,palette='viridis', legend=False)
    axes[i].set_title(f'{col} Distribution')

    total = len(df)
    for p in ax.patches:
        height = float(p.get_height())
        x_position = float(p.get_x())
        width = float(p.get_width())

        percentage = f'{100 * height / total:.1f}%'

        ax.annotate(
            percentage,
            (x_position + width / 2, height),
            ha='center',
            va='bottom',
            fontsize=9
        )

# Remove empty subplot
for j in range(len(cat_cols), len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

plt.figure(figsize=(18, 14))

corr = df.corr(numeric_only=True)

sns.heatmap(corr,
            cmap='coolwarm',
            center=0)

plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(8, 12))

corr = df.corr(numeric_only=True)[['Diagnosis']].sort_values(
    by='Diagnosis',
    ascending=False
)

sns.heatmap(corr,
            annot=True,
            cmap='coolwarm',
            center=0)

plt.title("Feature Correlation with Diagnosis")
plt.show()

# Label Encoding

label_encoder = LabelEncoder()

categorical_cols = df.select_dtypes(include=['object','string']).columns

for col in categorical_cols:

    df[col] = label_encoder.fit_transform(df[col])

print(df.head())

# Separate input and output variables

X = df.drop('Diagnosis', axis=1)

y = df['Diagnosis']

print("Input Features:")
print(X.head())

print("\nTarget Variable:")
print(y.head())

from sklearn.model_selection import train_test_split

# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train Shape:", X_train.shape)
print("X_test Shape:", X_test.shape)
print("y_train Shape:", y_train.shape)
print("y_test Shape:", y_test.shape)

from sklearn.decomposition import PCA

# Apply PCA

pca = PCA(n_components=2)

X_train_pca = pca.fit_transform(X_train)

X_test_pca = pca.transform(X_test)

print(X_train_pca)

# PCA Visualization

plt.figure(figsize=(8,6))

plt.scatter(
    X_train_pca[:,0],
    X_train_pca[:,1]
)

plt.xlabel("Principal Component 1")

plt.ylabel("Principal Component 2")

plt.title("PCA Visualization")

plt.show()

import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report
)

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

lr_model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=3000, random_state=42)
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.calibration import CalibratedClassifierCV

svm_model = make_pipeline(
    StandardScaler(),
    CalibratedClassifierCV(
        SVC(),
        method="sigmoid",
        cv=5
    )
)




models = {
    "Logistic Regression": LogisticRegression(max_iter=3000, random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(probability=True, random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42)
}

results = []

for name, model in models.items():

    # Train
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Store metrics
    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, zero_division=0),
        "Recall": recall_score(y_test, y_pred, zero_division=0),
        "F1-Score": f1_score(y_test, y_pred, zero_division=0),
        "ROC-AUC": roc_auc_score(y_test, y_prob)
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values(
    by="ROC-AUC",
    ascending=False
)
print(results_df)
# results_df

from sklearn.ensemble import GradientBoostingClassifier
#create model
model= GradientBoostingClassifier(random_state=42)

# Train model

model.fit(X_train, y_train)

# Predict values

y_pred = model.predict(X_test)

print(y_pred)

from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    display_labels=["Low Risk", "High Risk"],
    cmap="Blues"
)

plt.title("Confusion Matrix - Gradient Boosting")
plt.show()

from sklearn.metrics import RocCurveDisplay
RocCurveDisplay.from_estimator(model, X_test, y_test)
plt.title("ROC Curve Example")
plt.show()

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

import pandas as pd

feature_importance = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by='Importance',
    ascending=False
)

# feature_importance

top10 = feature_importance.head(10)

plt.figure(figsize=(8,6))

sns.barplot(
    data=top10,
    x='Importance',
    y='Feature'
)

plt.title("Top 10 Important Features - Gradient Boosting")
plt.xlabel("Importance")
plt.ylabel("Feature")

plt.tight_layout()
plt.show()

import joblib

joblib.dump(model, "models/alzheimers_model.pkl")
feature_names = X.columns.tolist()
joblib.dump(feature_names, 'feature_names.pkl')