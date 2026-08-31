from app import create_app


def test_health():
    response = create_app().test_client().get("/health")
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["status"] == "ok"
    assert payload["service"] == "AI Customer Support Assistant"


def test_chat():
    response = create_app().test_client().post("/api/chat/", json={"message": "Where is my order?"})
    assert response.status_code == 200
    assert response.json["intent"] == "order_status"
    assert "answer" in response.json


def test_chat_requires_message():
    response = create_app().test_client().post("/api/chat/", json={"message": ""})
    assert response.status_code == 400
    assert "Message is required" in response.get_json()["error"]


def test_analyzer_returns_summary_and_keywords():
    response = create_app().test_client().post(
        "/api/analyzer/analyze",
        json={"text": "I need a refund for my late delivery and a broken package."},
    )
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["words"] >= 12
    assert "summary" in payload
    assert payload["keywords"]


def test_analytics_dashboard_exposes_summary():
    response = create_app().test_client().get("/api/analytics/dashboard")
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["automation_coverage"] > 0
    assert payload["service_status"] == "healthy"
