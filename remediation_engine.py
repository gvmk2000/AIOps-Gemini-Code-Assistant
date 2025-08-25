import sqlite3

def analyze_and_remediate():
    conn = sqlite3.connect('aiops.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM anomalies WHERE status = 'new'")
    anomalies = c.fetchall()

    for anomaly in anomalies:
        anomaly_id, timestamp, device_id, severity, description, status = anomaly

        # Simple RCA
        recommendation = "No recommendation"
        if "High resource usage" in description:
            if severity < -0.1:
                recommendation = f"Restart service on {device_id}"
            else:
                recommendation = f"Investigate resource usage on {device_id}"

        # Store RCA
        c.execute("INSERT INTO rca (anomaly_id, recommendation) VALUES (?, ?)", (anomaly_id, recommendation))

        # Simulate remediation
        if "Restart" in recommendation:
            print(f"Executing remediation: {recommendation}")
            # Update status
            c.execute("UPDATE anomalies SET status = 'remediated' WHERE rowid = ?", (anomaly_id,))
        else:
            c.execute("UPDATE anomalies SET status = 'investigating' WHERE rowid = ?", (anomaly_id,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    analyze_and_remediate()
