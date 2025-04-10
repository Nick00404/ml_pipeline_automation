# src/data/feature_engineering.py

import pandas as pd
import numpy as np
import logging
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


def load_data(filepath: str) -> pd.DataFrame:
    """Loads the dataset from a CSV file."""
    logging.info(f"Loading dataset from: {filepath}")
    df = pd.read_csv(filepath)
    logging.info(f"Dataset loaded successfully. Shape: {df.shape}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the data: trims strings, drops unused columns, handles missing values."""
    logging.info("Starting data cleaning...")

    # Strip spaces from string fields
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Drop customerID if it exists
    if 'customerID' in df.columns:
        df.drop('customerID', axis=1, inplace=True)
        logging.info("Dropped 'customerID' column.")

    # Convert TotalCharges to numeric (some are empty strings)
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Drop rows with too many missing values (optional)
    df.dropna(subset=['TotalCharges'], inplace=True)

    logging.info("Missing values handled.")
    logging.info(f"Cleaned data shape: {df.shape}")
    return df


def encode_features(df: pd.DataFrame) -> pd.DataFrame:
    """Encodes categorical features using binary and one-hot encoding."""
    logging.info("Starting feature encoding...")

    binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling',
                   'Churn', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                   'TechSupport', 'StreamingTV', 'StreamingMovies', 'MultipleLines']

    # Binary encode
    for col in binary_cols:
        if col in df.columns:
            df[col] = df[col].map({'Yes': 1, 'No': 0})
            logging.info(f"Binary encoded: {col}")

    # One-hot encode remaining categoricals
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    logging.info("One-hot encoding completed.")
    return df


def scale_features(df: pd.DataFrame) -> pd.DataFrame:
    """Imputes missing values (median) and scales numerical features."""
    logging.info("Starting feature scaling...")

    # Force binary columns to numeric (just in case)
    binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling',
                   'Churn', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                   'TechSupport', 'StreamingTV', 'StreamingMovies', 'MultipleLines']
    for col in binary_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Get numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    # Drop numeric cols that are fully NaN
    full_nan_cols = [col for col in numeric_cols if df[col].isnull().all()]
    if full_nan_cols:
        logging.warning(f"These numeric columns are fully NaN and will be dropped: {full_nan_cols}")
        df.drop(columns=full_nan_cols, inplace=True)
        numeric_cols = [col for col in numeric_cols if col not in full_nan_cols]

    # Handle NaNs with median imputer
    nan_count = df[numeric_cols].isnull().sum().sum()
    if nan_count > 0:
        logging.warning(f"{nan_count} NaN values found in numeric columns before scaling. Applying median imputation.")
        imputer = SimpleImputer(strategy='median')
        imputed_array = imputer.fit_transform(df[numeric_cols])
        df[numeric_cols] = pd.DataFrame(imputed_array, columns=numeric_cols, index=df.index)

    # Scale
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    logging.info("Feature scaling completed.")
    logging.info(f"Final processed shape: {df.shape}")
    return df


def process_pipeline(filepath: str) -> pd.DataFrame:
    """Full processing pipeline: load, clean, encode, scale."""
    df = load_data(filepath)
    df = clean_data(df)
    df = encode_features(df)
    df = scale_features(df)
    return df


# If you want to run this as a script
if __name__ == "__main__":
    processed_df = process_pipeline("data/raw/telco_customer_churn.csv")
    print(processed_df.head())
