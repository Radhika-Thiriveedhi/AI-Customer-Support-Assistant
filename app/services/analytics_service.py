class AnalyticsService:
    def dashboard(self):
        return {"active_intents":8,"supported_channels":4,"automation_coverage":.78,
                "response_target_seconds":2,"quality_checks":12}
    def intent_catalog(self):
        return ["greeting","order_status","return","refund","delivery","payment","account","complaint","unknown"]
