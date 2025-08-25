import pandas as pd
import numpy as np
import sqlite3
import yaml

def generate_network_metrics(num_samples=1000):
    timestamps = pd.date_range(start="2024-01-01", periods=num_samples, freq="5min")
    cpu = np.random.normal(50, 15, num_samples).clip(0, 100)
    memory = np.random.normal(60, 10, num_samples).clip(0, 100)
    latency = np.random.normal(100, 20, num_samples).clip(20, 200)
    return pd.DataFrame({"timestamp": timestamps, "cpu": cpu, "memory": memory, "latency": latency})

def simulate_data():
    conn = sqlite3.connect('aiops.db')
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    for device in config['devices']:
        df = generate_network_metrics()
        df['device_id'] = device['name']
        df.to_sql('metrics', conn, if_exists='append', index=False)

        # Store config
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO configs (device_id, config) VALUES (?, ?)", 
                  (device['name'], yaml.dump(device)))
        conn.commit()

    conn.close()

if __name__ == "__main__":
    simulate_data()
