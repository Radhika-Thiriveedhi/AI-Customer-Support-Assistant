class SentimentService:
    POSITIVE={"great","good","happy","thanks","thank","excellent","love","helpful"}
    NEGATIVE={"bad","angry","terrible","worst","hate","late","broken","frustrated","unhappy"}
    def score(self,text):
        words=set(text.lower().split()); pos=len(words&self.POSITIVE); neg=len(words&self.NEGATIVE)
        if neg>pos: return {"label":"negative","confidence":min(.99,.55+neg*.08)}
        if pos>neg: return {"label":"positive","confidence":min(.99,.55+pos*.08)}
        return {"label":"neutral","confidence":.60}
