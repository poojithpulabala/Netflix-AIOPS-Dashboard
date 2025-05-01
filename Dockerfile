FROM python:3.10-slim

WORKDIR /app

COPY app/ /app/

RUN pip install --upgrade pip && \
    pip install streamlit scikit-learn pandas matplotlib

EXPOSE 8501

CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
