from datetime import date
from enum import Enum
from typing import List, Dict
from pydantic import BaseModel, Field

class CategoryEnum(str, Enum):
    FOOD = "Food & Drink"
    HOUSING = "Housing & Utilities"
    TRANSPORT = "Transportation"
    ENTERTAINMENT = "Entertainment"
    MISCELLANEOUS = "Miscellaneous"
    INCOME = "Income"

class Transaction(BaseModel):
    id: str
    date: date
    category: CategoryEnum
    description: str
    amount: float

class SimulationParameters(BaseModel):
    initial_balance: float = Field(default=24567.89, ge=0)
    monthly_income: float = Field(default=5800.00, gt=0)
    food_budget: float = Field(default=800.00, ge=0)
    housing_budget: float = Field(default=1500.00, ge=0)
    transport_budget: float = Field(default=300.00, ge=0)
    misc_budget: float = Field(default=400.00, ge=0)
    simulation_days: int = Field(default=30, ge=1, le=90)

class SimulationReport(BaseModel):
    starting_balance: float
    ending_balance: float
    total_income: float
    total_expenses: float
    miscellaneous_spent: float
    monthly_savings: float
    projected_annual_savings: float
    daily_safe_to_spend: float
    budget_breakdown: Dict[str, float]
    transactions: List[Transaction]