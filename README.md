# AI Customer Support Assistant

Production-oriented AI / ML application for customer-support automation.

## Domain
AI / ML & Data

## Subdomain
AI applications — AI customer support

## Features
- Router-based Flask architecture
- Support intent detection and sentiment analysis
- Customer document analysis and ticket classification
- Service analytics endpoints
- Responsive browser interface
- Automated tests and coverage
- Docker support
- No database connection required

## Install
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

## Run
python run.py
Open http://127.0.0.1:5000

## Build
docker build -t ai-customer-support-assistant .
docker run -p 5000:5000 ai-customer-support-assistant

## Test
pytest
