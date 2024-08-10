import google.generativeai as genai
from models.llms.llm_interface import LLMInterface
from config import GOOGLE_API_KEY

class GeminiModel(LLMInterface):
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def get_response(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text