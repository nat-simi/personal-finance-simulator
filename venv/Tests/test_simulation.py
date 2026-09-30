from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is live. Go to /docs to test endpoints!"}

def test_quick_demo_simulation():
    response = client.get("/api/v1/simulate/quick-demo")
    assert response.status_code == 200
    data = response.json()
    
    # Verify core report fields exist
    assert "starting_balance" in data
    assert "ending_balance" in data
    assert "daily_safe_to_spend" in data
    assert "transactions" in data
    assert len(data["transactions"]) > 0

def test_custom_simulation_payload():
    payload = {
        "initial_balance": 10000.0,
        "monthly_income": 4000.0,
        "food_budget": 500.0,
        "housing_budget": 1000.0,
        "transport_budget": 200.0,
        "misc_budget": 150.0,
        "simulation_days": 15
    }
    response = client.post("/api/v1/simulate", json=payload)
    assert response.status_code == 200
    data = response.json()
    
    assert data["starting_balance"] == 10000.0
    assert data["total_income"] == 4000.0