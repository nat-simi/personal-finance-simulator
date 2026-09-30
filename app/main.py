from fastapi import FastAPI
from app.schemas import SimulationParameters, SimulationReport
from app.simulator import generate_finance_simulation

app = FastAPI(
    title="Personal Finance Simulation API",
    description="Simulates ledger activity, account balances, savings projections, and category budgets.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "API is live. Go to /docs to test endpoints!"}

@app.post("/api/v1/simulate", response_model=SimulationReport)
def run_simulation(params: SimulationParameters):
    return generate_finance_simulation(params)

@app.get("/api/v1/simulate/quick-demo", response_model=SimulationReport)
def run_quick_demo():
    default_params = SimulationParameters()
    return generate_finance_simulation(default_params)