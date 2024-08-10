from models.factories.llm_factory import LLMFactory
from models.llms.llm_interface import LLMInterface
from models.llms.gemini import GeminiModel

class GeminiFactory(LLMFactory):
    def manufacturesLLM() -> LLMInterface:
        return GeminiModel()