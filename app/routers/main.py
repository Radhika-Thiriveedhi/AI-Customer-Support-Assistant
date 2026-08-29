from flask import Blueprint, render_template, jsonify
main_bp = Blueprint("main", __name__)
@main_bp.get("/")
def home():
    return render_template("index.html")
@main_bp.get("/health")
def health():
    return jsonify({"status":"ok","service":"AI Customer Support Assistant"})
