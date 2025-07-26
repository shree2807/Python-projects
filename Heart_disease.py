# Heart Disease Prediction using Machine Learning (Cleveland Dataset)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve, ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from imblearn.over_sampling import SMOTE
import joblib

# 1. Load Dataset
df = pd.read_csv("heart_cleveland_upload.csv")

# 2. Rename target column
df.rename(columns={"condition": "HeartDisease"}, inplace=True)

# 3. Convert multi-class target to binary (if needed)
df["HeartDisease"] = df["HeartDisease"].apply(lambda x: 1 if x > 0 else 0)

# 4. Check and handle missing values
print("Missing values:\n", df.isnull().sum())

# 5. EDA
sns.countplot(x="HeartDisease", data=df)
plt.title("Heart Disease Distribution")
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# 6. Feature & Target split
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

# 7. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# 8. Balance data using SMOTE
print("Before SMOTE:", y_train.value_counts())
sm = SMOTE(random_state=42)
X_train, y_train = sm.fit_resample(X_train, y_train)
print("After SMOTE:", y_train.value_counts())

# 9. Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 10. Model Training
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42),
    "DecisionTree": DecisionTreeClassifier(random_state=42),
    "RandomForest": RandomForestClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(probability=True, random_state=42),
}

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None

    acc = model.score(X_test, y_test)
    report = classification_report(y_test, y_pred, output_dict=True)
    roc_auc = roc_auc_score(y_test, y_proba) if y_proba is not None else None

    print(f"\n{name} Classification Report:")
    print(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    ConfusionMatrixDisplay(cm).plot()
    plt.title(f"{name} - Confusion Matrix")
    plt.show()

    if y_proba is not None:
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        plt.plot(fpr, tpr, label=f"{name} (AUC={roc_auc:.2f})")

    results.append({
        "Model": name,
        "Accuracy": acc,
        "Precision": report["1"]["precision"],
        "Recall": report["1"]["recall"],
        "F1": report["1"]["f1-score"],
        "ROC-AUC": roc_auc,
    })

# 11. ROC Curve Comparison
plt.plot([0, 1], [0, 1], "k--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison")
plt.legend()
plt.show()

# 12. Model Comparison
results_df = pd.DataFrame(results)
print("\nModel Comparison:\n", results_df)

# 13. Hyperparameter Tuning for Logistic Regression
param_grid = {"C": [0.01, 0.1, 1, 10], "solver": ["liblinear", "lbfgs"]}
grid = GridSearchCV(LogisticRegression(max_iter=1000, random_state=42),
                    param_grid, cv=5, scoring="roc_auc")
grid.fit(X_train, y_train)
best_lr = grid.best_estimator_
print("\nBest Logistic Regression Parameters:", grid.best_params_)

# 14. Cross Validation
cv_scores = cross_val_score(best_lr, X, y, cv=5, scoring="roc_auc")
print("Cross-Val ROC-AUC scores:", cv_scores)
print("Average CV ROC-AUC:", cv_scores.mean())

# 15. Feature Importance (from Random Forest)
rf = models["RandomForest"]
importances = rf.feature_importances_
features = X.columns
imp_df = pd.DataFrame({"Feature": features, "Importance": importances}).sort_values(by="Importance", ascending=False)

sns.barplot(x="Importance", y="Feature", data=imp_df)
plt.title("Feature Importance from Random Forest")
plt.show()

# 16. Save Final Model and Scaler
joblib.dump(best_lr, "heart_disease_model.pkl")
joblib.dump(scaler, "scaler.pkl")
print("Model and Scaler saved successfully.")
