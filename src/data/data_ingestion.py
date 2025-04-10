import os
import pandas as pd
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def get_raw_data_path(filename: str) -> str:
    """
    Build an absolute path to the raw data file, based on the script's location.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_path = os.path.join(base_dir, "data", "raw", filename)
    return data_path

def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load the dataset from the given file path.
    """
    try:
        logging.info(f"Loading dataset from: {file_path}")
        df = pd.read_csv(file_path)
        logging.info(f"Dataset loaded successfully. Shape: {df.shape}")
        return df
    except Exception as e:
        logging.error(f"Failed to load dataset: {e}")
        raise

def split_dataset(df: pd.DataFrame, test_size: float = 0.2):
    """
    Split dataset into train and test sets.
    """
    from sklearn.model_selection import train_test_split
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=42)
    logging.info(f"Split dataset: Train={train_df.shape}, Test={test_df.shape}")
    return train_df, test_df

if __name__ == "__main__":
    raw_data_path = get_raw_data_path("telco_customer_churn.csv")
    data = load_dataset(raw_data_path)
    train_data, test_data = split_dataset(data)
