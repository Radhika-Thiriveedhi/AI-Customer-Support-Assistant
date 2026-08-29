from datetime import datetime
from app.services.knowledge_service import KnowledgeService
from app.services.intent_service import IntentService
from app.services.sentiment_service import SentimentService
class SupportChatService:
    def __init__(self):
        self.knowledge=KnowledgeService()
        self.intent=IntentService()
        self.sentiment=SentimentService()
    def reply(self,message):
        intent=self.intent.detect(message)
        sentiment=self.sentiment.score(message)
        return {"answer":self.knowledge.answer(intent,message),"intent":intent,
                "sentiment":sentiment["label"],"confidence":sentiment["confidence"],
                "timestamp":datetime.utcnow().isoformat()+"Z"}
