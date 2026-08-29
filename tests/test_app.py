from app import create_app
def test_health():
    assert create_app().test_client().get("/health").status_code == 200
def test_chat():
    r=create_app().test_client().post("/api/chat/",json={"message":"Where is my order?"})
    assert r.status_code==200 and r.json["intent"]=="order_status"
