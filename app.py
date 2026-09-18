from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Enable CORS so the HTML frontend can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained ML Model on startup
model = joblib.load("model.joblib")
THREAT_LABELS = {0: "SAFE", 1: "SUSPICIOUS", 2: "CRITICAL THREAT"}

# Define expected input schema
class SecurityPayload(BaseModel):
    packet_size: float
    request_rate: float
    failed_logins: float

@app.post("/predict")
async def predict_security_risk(data: SecurityPayload):
    # Convert input payload to model feature vector
    features = np.array([[data.packet_size, data.request_rate, data.failed_logins]])
    
    # Run prediction
    prediction_class = int(model.predict(features)[0])
    probabilities = model.predict_proba(features)[0].tolist()
    
    return {
        "threat_level": THREAT_LABELS[prediction_class],
        "confidence": round(max(probabilities) * 100, 2),
        "raw_class": prediction_class
    }