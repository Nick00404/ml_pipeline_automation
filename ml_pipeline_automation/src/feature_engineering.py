from sklearn.preprocessing import StandardScaler

def engineer_features(df):
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df.select_dtypes(include=['float64', 'int']))
    return df_scaled
