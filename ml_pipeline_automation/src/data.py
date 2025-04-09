import pandas as pd

def load_data(filepath):
    '''Loads data from a CSV file.'''
    return pd.read_csv(filepath)

def preprocess_data(df):
    '''Preprocess the dataframe.'''
    # Add preprocessing steps here
    return df
