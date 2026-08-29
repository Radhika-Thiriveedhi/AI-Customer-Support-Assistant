from flask import Flask
from pathlib import Path

def create_app():
    root = Path(__file__).resolve().parent.parent
    app = Flask(__name__, template_folder=str(root / "templates"), static_folder=str(root / "static"))
    app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024
    from app.routers.main import main_bp
    from app.routers.chat import chat_bp
    from app.routers.analyzer import analyzer_bp
    from app.routers.analytics import analytics_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(chat_bp, url_prefix="/api/chat")
    app.register_blueprint(analyzer_bp, url_prefix="/api/analyzer")
    app.register_blueprint(analytics_bp, url_prefix="/api/analytics")
    return app
