import pandas as pd
import sqlite3
from sklearn.ensemble import IsolationForest

def train_and_detect_anomalies():
    conn = sqlite3.connect('aiops.db')
    df = pd.read_sql_query("SELECT * FROM metrics", conn)

    # Train model
    model = IsolationForest(contamination=0.05)
    model.fit(df[["cpu", "memory", "latency"]])

    # Detect anomalies
    df["anomaly_score"] = model.decision_function(df[["cpu", "memory", "latency"]])
    anomalies = df[df["anomaly_score"] < 0]

    # Store anomalies
    for _, row in anomalies.iterrows():
        c = conn.cursor()
        c.execute("INSERT INTO anomalies (timestamp, device_id, severity, description, status) VALUES (?, ?, ?, ?, ?)",
                  (row['timestamp'], row['device_id'], row['anomaly_score'], 'High resource usage', 'new'))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    train_and_detect_anomalies()
