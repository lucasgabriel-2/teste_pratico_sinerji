from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, prompt: str, selected_model: str, selected_response: str, reason: str):
        pass