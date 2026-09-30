import random
import uuid
from datetime import date, timedelta
from typing import List
from app.schemas import SimulationParameters, SimulationReport, Transaction, CategoryEnum

def generate_finance_simulation(params: SimulationParameters) -> SimulationReport:
    start_date = date.today()
    transactions: List[Transaction] = []
    
    current_balance = params.initial_balance
    total_income = 0.0
    total_expenses = 0.0
    misc_spent = 0.0
    
    category_spending = {
        CategoryEnum.FOOD: 0.0,
        CategoryEnum.HOUSING: 0.0,
        CategoryEnum.TRANSPORT: 0.0,
        CategoryEnum.ENTERTAINMENT: 0.0,
        CategoryEnum.MISCELLANEOUS: 0.0,
    }

    # 1. Income Deposit
    paycheck = Transaction(
        id=str(uuid.uuid4())[:8],
        date=start_date,
        category=CategoryEnum.INCOME,
        description="Monthly Salary Deposit",
        amount=params.monthly_income
    )
    transactions.append(paycheck)
    current_balance += params.monthly_income
    total_income += params.monthly_income

    # 2. Fixed Housing Payment
    housing_cost = params.housing_budget * random.uniform(0.95, 1.0)
    transactions.append(Transaction(
        id=str(uuid.uuid4())[:8],
        date=start_date,
        category=CategoryEnum.HOUSING,
        description="Rent & Utilities Payment",
        amount=-round(housing_cost, 2)
    ))
    current_balance -= housing_cost
    total_expenses += housing_cost
    category_spending[CategoryEnum.HOUSING] += housing_cost

    # 3. Daily Transactions
    food_options = ["Grocery Store", "Local Cafe", "Cozy Dinner", "Supermarket"]
    misc_options = ["Coffee Shop", "Bookstore", "Hardware Store", "Online Purchase"]
    transport_options = ["Gas Station", "Subway Pass", "Rideshare"]

    for day in range(1, params.simulation_days):
        current_date = start_date + timedelta(days=day)
        
        if random.random() < 0.8:
            amount = round(random.uniform(15.0, 60.0), 2)
            transactions.append(Transaction(
                id=str(uuid.uuid4())[:8],
                date=current_date,
                category=CategoryEnum.FOOD,
                description=random.choice(food_options),
                amount=-amount
            ))
            current_balance -= amount
            total_expenses += amount
            category_spending[CategoryEnum.FOOD] += amount

        if random.random() < 0.4:
            amount = round(random.uniform(10.0, 45.0), 2)
            transactions.append(Transaction(
                id=str(uuid.uuid4())[:8],
                date=current_date,
                category=CategoryEnum.TRANSPORT,
                description=random.choice(transport_options),
                amount=-amount
            ))
            current_balance -= amount
            total_expenses += amount
            category_spending[CategoryEnum.TRANSPORT] += amount

        if random.random() < 0.3:
            amount = round(random.uniform(8.0, 75.0), 2)
            transactions.append(Transaction(
                id=str(uuid.uuid4())[:8],
                date=current_date,
                category=CategoryEnum.MISCELLANEOUS,
                description=random.choice(misc_options),
                amount=-amount
            ))
            current_balance -= amount
            total_expenses += amount
            misc_spent += amount
            category_spending[CategoryEnum.MISCELLANEOUS] += amount

    # 4. Final Calculations
    monthly_savings = max(0.0, total_income - total_expenses)
    projected_annual_savings = monthly_savings * 12
    daily_safe_to_spend = round(max(0.0, (current_balance - 5000.0) / params.simulation_days), 2)

    return SimulationReport(
        starting_balance=params.initial_balance,
        ending_balance=round(current_balance, 2),
        total_income=round(total_income, 2),
        total_expenses=round(total_expenses, 2),
        miscellaneous_spent=round(misc_spent, 2),
        monthly_savings=round(monthly_savings, 2),
        projected_annual_savings=round(projected_annual_savings, 2),
        daily_safe_to_spend=daily_safe_to_spend,
        budget_breakdown={cat.value: round(amt, 2) for cat, amt in category_spending.items()},
        transactions=transactions
    )