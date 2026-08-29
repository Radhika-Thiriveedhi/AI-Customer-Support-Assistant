from flask import Blueprint, jsonify
from app.services.analytics_service import AnalyticsService
analytics_bp=Blueprint("analytics",__name__)
analytics=AnalyticsService()
@analytics_bp.get("/dashboard")
def dashboard(): return jsonify(analytics.dashboard())
@analytics_bp.get("/intents")
def intents(): return jsonify({"intents":analytics.intent_catalog()})
