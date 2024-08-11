from abc import ABC, abstractmethod

class LLMCommand(ABC):
    @abstractmethod
    def execute(self):
        pass