import sqlite3

def setup_database():
    conn = sqlite3.connect('aiops.db')
    c = conn.cursor()

    # Create tables
    c.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            timestamp DATETIME,
            device_id TEXT,
            cpu REAL,
            memory REAL,
            latency REAL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS anomalies (
            timestamp DATETIME,
            device_id TEXT,
            severity REAL,
            description TEXT,
            status TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS configs (
            device_id TEXT PRIMARY KEY,
            config TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS rca (
            anomaly_id INTEGER,
            recommendation TEXT,
            FOREIGN KEY (anomaly_id) REFERENCES anomalies(rowid)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
