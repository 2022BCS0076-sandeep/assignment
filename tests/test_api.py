from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_high_risk():
    response = client.post("/predict-risk", json={
        "tickets_last_30_days": 6,
        "charges_increase": False,
        "contract": "Yearly",
        "complaint_ticket": False
    })
    assert response.json()["risk"] == "HIGH"