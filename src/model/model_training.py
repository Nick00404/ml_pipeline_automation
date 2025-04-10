# src/model/model_training.py

import logging
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from src.data.data_cleaning import clean_data
from src.data.feature_engineering import clean_data, encode_features, scale_features

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def load_and_prepare_data(path: str):
    logging.info(f"Loading dataset from: {path}")
    df = pd.read_csv(path)
    logging.info(f"Dataset loaded successfully. Shape: {df.shape}")

    logging.info("Cleaning data...")
    df = clean_data(df)

    logging.info("Engineering features...")
    df = feature_engineering(df)

    # Drop any rows with NaN just to be safe
    df = df.dropna()

    # Target column
    y = df['Churn']
    X = df.drop(columns=['Churn'])

    return X, y

def train_model(X, y):
    logging.info("Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    logging.info("Training logistic regression model...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    logging.info("Model training complete.")

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    logging.info(f"Accuracy: {acc:.4f}")
    logging.info("Classification Report:\n" + classification_report(y_test, y_pred))

    return model

if __name__ == "__main__":
    raw_data_path = "data/raw/telco_customer_churn.csv"
    X, y = load_and_prepare_data(raw_data_path)
    model = train_model(X, y)
