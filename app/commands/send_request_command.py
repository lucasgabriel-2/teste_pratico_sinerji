from commands.command import LLMCommand
from models.factories.chatgpt_factory import ChatGPTFactory
from models.factories.gemini_factory import GeminiFactory

class SendRequestCommand(LLMCommand):
    def __init__(self, prompt):
        self.prompt = prompt

    def execute(self):
        chatgpt_factory = ChatGPTFactory
        gemini_factory = GeminiFactory

        chatgpt_model = chatgpt_factory.manufacturesLLM()
        gemini_model = gemini_factory.manufacturesLLM()
        
        chatgpt_response = chatgpt_model.get_response(self.prompt)
        gemini_response = gemini_model.get_response(self.prompt)
        
        return chatgpt_response, gemini_response