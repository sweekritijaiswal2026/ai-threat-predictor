import joblib
import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model once at startup
try:
    model = joblib.load("model.joblib")
except Exception as e:
    model = None


class SecurityPayload(BaseModel):
    packet_size: float
    request_rate: float
    failed_logins: float


@app.post("/predict")
def predict_security_risk(data: SecurityPayload):
    if model is None:
        return {"prediction": "SAFE", "threat_level": "SAFE"}

    features = np.array(
        [[data.packet_size, data.request_rate, data.failed_logins]]
    )
    pred_class = int(model.predict(features)[0])

    labels = {0: "SAFE", 1: "SUSPICIOUS", 2: "CRITICAL THREAT"}
    status = labels.get(pred_class, "SAFE")

    return {"prediction": status, "threat_level": status}
