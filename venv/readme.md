Personal Finance Simulation API

A robust, high-performance RESTful API built with FastAPI and Pydantic to simulate, track, and analyze personal financial flows. This project enables users to perform balance projections, income/expense logging, and financial scenario simulations with strict data validation and comprehensive test coverage.

Key Features

Financial Simulation Engine: Simulate long-term portfolio growth and cash flows based on configurable recurring income, expenses, and savings rates.

Transaction & Ledger Management: Log income and expense transactions with custom categorization and balance updates.

Strict Data Validation: Powered by Pydantic v2, ensuring type safety, automated error handling, and structured request/response payloads.

Auto-Generated Interactive Documentation: Out-of-the-box Interactive API documentation using Swagger UI (/docs) and ReDoc (/redoc).

Automated Testing: Fully tested test suite utilizing Pytest and FastAPI's TestClient to ensure reliable endpoint behavior.

Tech Stack

Framework: FastAPI

Data Validation & Settings: Pydantic

ASGI Server: Uvicorn

Testing: Pytest

Language: Python 3.x

Project Structure

.
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application entry point
│   ├── models.py         # Pydantic schemas and models
│   ├── routers/          # API route definitions
│   └── services/        # Simulation and financial logic
├── tests/                # Automated pytest suite
│   ├── __init__.py
│   └── test_api.py
├── .gitignore
├── README.md
└── requirements.txt


Getting Started

Follow these steps to set up and run the application locally.

Prerequisites

Python 3.10 or higher installed on your machine.

Git for version control.

Installation

Clone the Repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


Create and Activate a Virtual Environment

Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1


macOS / Linux:

python3 -m venv venv
source venv/bin/activate


Install Dependencies

pip install -r requirements.txt


Running the Application

Start the local development server using Uvicorn:

uvicorn app.main:app --reload


The server will start at http://127.0.0.1:8000.

Interactive API Documentation

Once the server is running, you can explore and interact with the endpoints directly from your browser:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Running Tests

To run the automated unit and integration tests, execute:

pytest


To view test coverage details:

pytest --cov=app


Future Enhancements

[ ] Add JWT authentication for user session management.

[ ] Integrate PostgreSQL database backend with SQLAlchemy/Alembic migrations.

[ ] Support complex compound interest and investment asset allocation simulations.

[ ] Containerize application with Docker.

License

This project is licensed under the MIT License - see the LICENSE file for details.