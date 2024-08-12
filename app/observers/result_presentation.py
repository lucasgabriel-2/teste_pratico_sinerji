from observers.observer import Observer

class ResultPresentation(Observer):
    def update(self, prompt: str, selected_model: str, selected_response: str, reason: str):
        print(selected_model, ":", selected_response)
        print("Reason:", reason)