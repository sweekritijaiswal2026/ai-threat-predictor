# AI Cyber Threat Predictor

Real-time machine learning threat classification dashboard built with FastAPI, Scikit-learn, and HTML5.

## Features
- **Machine Learning Engine:** Scikit-learn Random Forest model detecting network anomalies.
- **FastAPI Server:** Asynchronous REST API serving predictions in milliseconds.
- **Dashboard UI:** Real-time threat visualization and risk reporting.

## Setup & Execution
1. Install dependencies: `pip install fastapi uvicorn scikit-learn joblib numpy`
2. Train model: `python train_model.py`
3. Start backend API: `uvicorn app:app --reload`
4. Open `index.html` in browser.