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

model = joblib.load("model.joblib")


class SecurityPayload(BaseModel):
    packet_size: float
    request_rate: float
    failed_logins: float


@app.post("/predict")
def predict_security_risk(data: SecurityPayload):
    features = np.array(
        [[data.packet_size, data.request_rate, data.failed_logins]]
    )
    prediction_class = int(model.predict(features)[0])

    # Direct string return for index.html matching
    labels = {0: "SAFE", 1: "SUSPICIOUS", 2: "CRITICAL THREAT"}
    status = labels.get(prediction_class, "SAFE")

    return {"prediction": status, "threat_level": status}
