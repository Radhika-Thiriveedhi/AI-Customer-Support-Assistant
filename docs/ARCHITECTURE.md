# Architecture

Flask routers expose support, analyzer, analytics and health endpoints. Services implement intent, sentiment, document, policy and workflow logic. The app is stateless and does not require a database.

## Runtime flow
1. The main app bootstraps blueprints for the home, health, chat, analyzer, and analytics routes.
2. Chat requests are routed to the support service, which detects intent, scores sentiment, and pulls the best knowledge answer.
3. Analyzer requests summarize text and classify support issues by category.
4. Analytics endpoints aggregate operational metrics for dashboards and monitoring.

## Design goals
- Stateless request handling
- Small, testable service layer
- Fast local setup without external infrastructure
- Clear separation between routing and business logic
