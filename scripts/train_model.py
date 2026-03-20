"""
Trains Random Forest, Decision Tree, and Naive Bayes classifiers.
Saves the best model (Random Forest) to models/random_forest_model.pkl

Usage:
    python scripts/train_model.py
"""
import sys
import os

# Make sure 'scripts/' is on the path so we can import preprocess.py
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPTS_DIR)

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
from preprocess import preprocess, BASE


def train():
    print("🌾 Starting model training...\n")
    df, scaler, le = preprocess()

    feature_cols = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall", "soil_type"]

    # Guard: make sure all feature columns exist
    missing_cols = [c for c in feature_cols if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in processed data: {missing_cols}")

    X = df[feature_cols]
    y = df["label_encoded"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Train samples: {len(X_train)} | Test samples: {len(X_test)}\n")

    models = {
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
        "Decision Tree": DecisionTreeClassifier(max_depth=10, random_state=42),
        "Naive Bayes":   GaussianNB(),
    }

    best_acc   = 0
    best_model = None
    best_name  = ""

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc   = accuracy_score(y_test, preds)
        print(f"{'='*50}")
        print(f"  {name}  |  Accuracy: {acc:.4f}")
        print(classification_report(y_test, preds, target_names=le.classes_))
        if acc > best_acc:
            best_acc   = acc
            best_model = model
            best_name  = name

    os.makedirs(os.path.join(BASE, "models"), exist_ok=True)
    out = os.path.join(BASE, "models", "random_forest_model.pkl")
    joblib.dump(best_model, out)
    print(f"\n✅ Best model: {best_name}  (accuracy={best_acc:.4f})")
    print(f"✅ Saved → {out}")
    print("\n🚀 Now run: streamlit run app/main.py")


if __name__ == "__main__":
    train()
