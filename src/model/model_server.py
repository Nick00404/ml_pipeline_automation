from fastapi import FastAPI
from prometheus_client import Counter, generate_latest

app = FastAPI()

REQUEST_COUNT = Counter('request_count', 'Total Request Count')

@app.get('/health')
def health():
    return {'status': 'healthy'}

@app.get('/predict')
def predict():
    REQUEST_COUNT.inc()
    # Dummy prediction
    return {'prediction': 1}

@app.get('/metrics')
def metrics():
    return generate_latest()
