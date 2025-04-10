import pandas as pd
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the input dataframe:
    - Handles missing values
    - Fixes data types for numerical columns
    - Drops useless columns
    """
    logging.info("Starting data cleaning...")

    # Drop customerID (it's just an identifier, not useful for prediction)
    if 'customerID' in df.columns:
        df.drop('customerID', axis=1, inplace=True)
        logging.info("Dropped 'customerID' column.")

    # Replace spaces in 'TotalCharges' with NaN
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'].replace(" ", pd.NA), errors='coerce')

    # Fill missing values with median for numerical columns
    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    # Fill categorical NaNs (if any) with mode
    cat_cols = df.select_dtypes(include='object').columns
    df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

    logging.info("Missing values handled.")
    logging.info(f"Cleaned data shape: {df.shape}")
    return df

# For quick testing/debugging
if __name__ == "__main__":
    from data_ingestion import get_raw_data_path, load_dataset
    raw_path = get_raw_data_path("telco_customer_churn.csv")
    df = load_dataset(raw_path)
    df_cleaned = clean_data(df)
    print(df_cleaned.head())
