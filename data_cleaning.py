# src/utils/data_cleaning.py
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def clean_strings(df: pd.DataFrame) -> pd.DataFrame:
    """Strip strings in object columns."""
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)
    return df

def drop_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    logging.info(f"Dropping columns: {columns}")
    return df.drop(columns=columns, errors='ignore')

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Convert empty strings to NaN and drop rows with all NaNs."""
    df.replace("", np.nan, inplace=True)
    df.dropna(how='all', inplace=True)
    logging.info("Missing values handled.")
    return df

def encode_binary_columns(df: pd.DataFrame, binary_columns: list) -> pd.DataFrame:
    for col in binary_columns:
        df[col] = df[col].map({'Yes': 1, 'No': 0})
        logging.info(f"Binary encoded: {col}")
    return df

def apply_one_hot_encoding(df: pd.DataFrame, exclude_columns: list) -> pd.DataFrame:
    categorical_cols = df.select_dtypes(include=['object']).columns.difference(exclude_columns)
    df = pd.get_dummies(df, columns=categorical_cols)
    logging.info("One-hot encoding completed.")
    return df

def scale_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    fully_nan_cols = [col for col in numeric_cols if df[col].isna().all()]
    if fully_nan_cols:
        logging.warning(f"These numeric columns are fully NaN and will be dropped: {fully_nan_cols}")
        df.drop(columns=fully_nan_cols, inplace=True)

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if df[numeric_cols].isna().sum().sum() > 0:
        logging.warning(f"{int(df[numeric_cols].isna().sum().sum())} NaN values found in numeric columns before scaling. Applying median imputation.")
        imputer = SimpleImputer(strategy='median')
        df[numeric_cols] = pd.DataFrame(imputer.fit_transform(df[numeric_cols]), columns=numeric_cols)

    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    logging.info("Feature scaling completed.")
    return df