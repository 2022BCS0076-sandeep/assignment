import logging
from fastapi import FastAPI
from app.rules import calculate_risk

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.post("/predict-risk")
def predict_risk(data: dict):
    logging.info(f"Input: {data}")
    risk = calculate_risk(data)
    logging.info(f"Output: {risk}")
    return {"risk": risk}