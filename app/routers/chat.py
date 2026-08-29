from flask import Blueprint, request, jsonify
from app.services.chat_service import SupportChatService
chat_bp = Blueprint("chat", __name__)
service = SupportChatService()
@chat_bp.post("/")
def chat():
    payload=request.get_json(silent=True) or {}
    message=str(payload.get("message","")).strip()
    if not message: return jsonify({"error":"Message is required"}),400
    return jsonify(service.reply(message))
