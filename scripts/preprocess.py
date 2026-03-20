"""
Preprocesses the raw crop_recommendation.csv and saves the scaler + label encoder.
Run this BEFORE train_model.py
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import joblib
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def preprocess(input_path=None, output_path=None):
    if input_path is None:
        input_path  = os.path.join(BASE, "data", "raw", "crop_recommendation.csv")
    if output_path is None:
        output_path = os.path.join(BASE, "data", "processed", "features_cleaned.csv")

    df = pd.read_csv(input_path)
    print(f"Loaded {len(df)} rows, columns: {list(df.columns)}")

    # Add synthetic soil_type if not present (0=sandy, 1=loamy, 2=clay)
    if "soil_type" not in df.columns:
        df["soil_type"] = np.random.choice([0, 1, 2], size=len(df))
        print("Added synthetic soil_type column.")

    feature_cols = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall", "soil_type"]
    scaler = MinMaxScaler()
    df[feature_cols] = scaler.fit_transform(df[feature_cols])

    le = LabelEncoder()
    df["label_encoded"] = le.fit_transform(df["label"])

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    os.makedirs(os.path.join(BASE, "models"), exist_ok=True)

    df.to_csv(output_path, index=False)
    joblib.dump(scaler, os.path.join(BASE, "models", "scaler.pkl"))
    joblib.dump(le,     os.path.join(BASE, "models", "label_encoder.pkl"))
    print(f"Saved processed data → {output_path}")
    print(f"Saved scaler + label_encoder → models/")
    return df, scaler, le

if __name__ == "__main__":
    preprocess()
