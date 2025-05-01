import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_stream_data(n=100):
    np.random.seed(42)
    now = datetime.now()
    timestamps = [now - timedelta(seconds=i*10) for i in range(n)][::-1]
    users = np.random.randint(1000, 1100, size=n)
    response_time = np.random.normal(loc=200, scale=25, size=n)  # ms
    stream_quality = np.random.choice(['480p', '720p', '1080p', '4K'], size=n, p=[0.2, 0.4, 0.3, 0.1])
    error_rate = np.random.beta(a=1, b=100, size=n)  # very low error rates

    data = pd.DataFrame({
        'timestamp': timestamps,
        'user_id': users,
        'response_time_ms': response_time,
        'stream_quality': stream_quality,
        'error_rate': error_rate
    })
    return data
