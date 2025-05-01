from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df: pd.DataFrame):
    model = IsolationForest(contamination=0.05, random_state=42)
    features = df[['response_time_ms', 'error_rate']]
    df['anomaly'] = model.fit_predict(features)
    return df
