from models.factories.llm_factory import LLMFactory
from models.llms.llm_interface import LLMInterface
from models.llms.chatgpt import ChatGPTModel

class ChatGPTFactory(LLMFactory):
    def manufacturesLLM() -> LLMInterface:
        return ChatGPTModel()
