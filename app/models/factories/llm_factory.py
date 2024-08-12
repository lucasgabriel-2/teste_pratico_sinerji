from models.llms.llm_interface import LLMInterface

from abc import ABC, abstractmethod
class LLMFactory(ABC):
    @abstractmethod
    def manufacturesLLM(self) -> LLMInterface:
        pass
