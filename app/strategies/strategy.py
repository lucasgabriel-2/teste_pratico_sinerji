from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def evaluate(self, prompt: str, responses: dict) -> tuple [str,str]:
        pass