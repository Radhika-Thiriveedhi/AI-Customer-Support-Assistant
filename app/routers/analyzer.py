from flask import Blueprint, request, jsonify
from app.services.document_service import DocumentAnalyzer
analyzer_bp=Blueprint("analyzer",__name__)
analyzer=DocumentAnalyzer()
@analyzer_bp.post("/analyze")
def analyze():
    payload=request.get_json(silent=True) or {}
    text=str(payload.get("text","")).strip()
    if not text: return jsonify({"error":"Text is required"}),400
    return jsonify(analyzer.analyze(text))
@analyzer_bp.post("/classify")
def classify():
    payload=request.get_json(silent=True) or {}
    text=str(payload.get("text","")).strip()
    if not text: return jsonify({"error":"Text is required"}),400
    return jsonify(analyzer.classify(text))
