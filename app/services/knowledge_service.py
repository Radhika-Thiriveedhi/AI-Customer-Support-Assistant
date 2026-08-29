class KnowledgeService:
    ANSWERS={
      "greeting":"Hello! I can help with orders, returns, refunds, delivery, payments, and account questions.",
      "order_status":"Please provide your order number. I can guide you through the order-status process.",
      "return":"Returns are usually started from the order page. Select the item, choose a reason, and follow pickup instructions.",
      "refund":"Refunds are normally initiated after the returned item is received and inspected. Check your payment method for the final credit.",
      "delivery":"Check the latest tracking event and expected delivery date. If a shipment has not moved for several days, contact support.",
      "payment":"For payment issues, verify the payment method, transaction status, and whether your bank has placed a temporary authorization hold.",
      "account":"You can update profile details, password, and notification preferences from account settings.",
      "complaint":"I’m sorry you had this experience. Share the order or case details so the issue can be routed to the correct workflow.",
      "unknown":"I can help with orders, returns, refunds, delivery, payments, and account questions. Please describe your issue in more detail."
    }
    def answer(self,intent,message): return self.ANSWERS.get(intent,self.ANSWERS["unknown"])
