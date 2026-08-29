import re
def normalize_text(value): return re.sub(r"\s+"," ",str(value or "")).strip()
def tokenize(value): return re.findall(r"\b[\w'-]+\b",normalize_text(value).lower())
