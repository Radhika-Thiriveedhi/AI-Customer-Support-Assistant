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
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run
```bash
python run.py
```
Open http://127.0.0.1:5000

## Key API endpoints
- `GET /health` — basic service health check
- `POST /api/chat/` — customer support chat with intent and sentiment analysis
- `POST /api/analyzer/analyze` — document text summarization
- `POST /api/analyzer/classify` — support ticket categorization
- `GET /api/analytics/dashboard` — service health and automation summary

## Build
```bash
docker build -t ai-customer-support-assistant .
docker run -p 5000:5000 ai-customer-support-assistant
```

## Test
```bash
pytest
```

## Operational notes
This project is intentionally stateless and database-free, making it easy to run, test, and deploy in a containerized environment.
