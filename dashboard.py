import streamlit as st
from stream_simulator import generate_stream_data
from anomaly_detector import detect_anomalies
from alert_manager import send_alert
import matplotlib.pyplot as plt

st.set_page_config(page_title="Netflix AIOps Dashboard", layout="wide")
st.title("🎬 Netflix-style AIOps Dashboard")

data = generate_stream_data(200)
data = detect_anomalies(data)
anomalies = data[data["anomaly"] == -1]

send_alert(len(anomalies))

st.subheader("📊 Stream Monitoring Data")
st.dataframe(data.tail(10))

fig, ax = plt.subplots()
ax.plot(data['timestamp'], data['response_time_ms'], label='Response Time (ms)')
ax.scatter(anomalies['timestamp'], anomalies['response_time_ms'], color='red', label='Anomalies')
ax.set_xlabel('Timestamp')
ax.set_ylabel('Response Time (ms)')
ax.legend()
st.pyplot(fig)
