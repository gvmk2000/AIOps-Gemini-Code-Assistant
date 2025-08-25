# AIOps POC

This project is a Proof of Concept for an AIOps solution that simulates network data, detects anomalies, performs root cause analysis, and suggests remediation actions.

## How to Run

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Setup the database:**
   ```
   python database_setup.py
   ```

3. **Simulate data:**
   ```
   python data_simulator.py
   ```

4. **Detect anomalies:**
   ```
   python anomaly_detector.py
   ```

5. **Run remediation engine:**
   ```
   python remediation_engine.py
   ```

6. **Run the dashboard:**
   ```
   streamlit run dashboard.py
   ```
