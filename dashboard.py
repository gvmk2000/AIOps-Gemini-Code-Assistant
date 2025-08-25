import streamlit as st
import pandas as pd
import sqlite3

st.title("AIOps Dashboard")

conn = sqlite3.connect('aiops.db')

# Metrics
st.header("Metrics")
df_metrics = pd.read_sql_query("SELECT * FROM metrics", conn)
st.line_chart(df_metrics.pivot_table(index='timestamp', columns='device_id', values=['cpu', 'memory', 'latency']))

# Anomalies
st.header("Anomalies")
df_anomalies = pd.read_sql_query("SELECT * FROM anomalies", conn)
st.dataframe(df_anomalies)

# RCA & Recommendations
st.header("RCA & Recommendations")
df_rca = pd.read_sql_query("SELECT a.device_id, a.description, r.recommendation FROM anomalies a JOIN rca r ON a.rowid = r.anomaly_id", conn)
st.dataframe(df_rca)

# Action History
st.header("Action History")
df_actions = pd.read_sql_query("SELECT * FROM anomalies WHERE status != 'new'", conn)
st.dataframe(df_actions)

conn.close()
