from fastapi import FastAPI, UploadFile, File

from src.image_damage_detector import detect_damage
from src.severity_predictor import predict_severity
from src.fraud_score import compute_fraud_score
from src.ai_explainer import generate_ai_explanation

app = FastAPI(title="Insurance AI API")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    damage = detect_damage("temp.jpg")
    severity = predict_severity("temp.jpg")

    fraud = compute_fraud_score(
        severity["score"],
        20, 10, 30,
        severity["confidence"] * 100
    )

    explanation = generate_ai_explanation(damage, severity, fraud)

    return {
        "damage": damage,
        "severity": severity,
        "fraud_score": fraud,
        "explanation": explanation
    }