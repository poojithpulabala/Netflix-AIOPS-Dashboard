def send_alert(anomalies_count):
    if anomalies_count > 0:
        print(f"[ALERT] 🚨 Detected {anomalies_count} anomalies in the stream.")
    else:
        print("[INFO] ✅ No anomalies detected.")
