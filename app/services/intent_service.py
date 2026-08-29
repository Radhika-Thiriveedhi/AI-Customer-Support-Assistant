class IntentService:
    RULES={
      "greeting":["hello","hi","hey","good morning","good evening"],
      "order_status":["where is my order","order status","track order","tracking","shipment"],
      "return":["return","send back","replace","replacement"],
      "refund":["refund","money back","reimburse","refund status"],
      "delivery":["delivery","delivered","courier","late","arrive"],
      "payment":["payment","paid","charge","transaction","card"],
      "account":["password","account","profile","login","sign in"],
      "complaint":["complaint","angry","terrible","bad service","unhappy"]
    }
    def detect(self,text):
        value=text.lower().strip()
        for intent,phrases in self.RULES.items():
            if any(p in value for p in phrases): return intent
        return "unknown"
