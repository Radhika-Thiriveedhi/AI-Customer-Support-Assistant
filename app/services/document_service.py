import re
from collections import Counter


class DocumentAnalyzer:
    def analyze(self, text):
        text = str(text or "").strip()
        if not text:
            return {"characters": 0, "words": 0, "sentences": 0, "keywords": [], "summary": ""}

        sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
        words = re.findall(r"\b[\w'-]+\b", text.lower())
        keys = Counter(w for w in words if len(w) > 4).most_common(8)
        return {
            "characters": len(text),
            "words": len(words),
            "sentences": len(sentences),
            "keywords": [{"word": w, "count": c} for w, c in keys],
            "summary": " ".join(sentences[:3])[:500],
        }

    def classify(self, text):
        text = str(text or "").strip()
        lower = text.lower()
        labels = {
            "billing": ["invoice", "charge", "payment", "bill"],
            "technical": ["error", "bug", "crash", "login", "not working"],
            "order": ["order", "delivery", "shipment", "tracking"],
            "account": ["password", "profile", "account"],
        }
        scores = {k: sum(t in lower for t in v) for k, v in labels.items()}
        label = max(scores, key=scores.get) if max(scores.values()) else "general"
        return {"category": label, "scores": scores}
