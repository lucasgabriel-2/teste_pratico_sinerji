from openai import OpenAI
from models.llms.llm_interface import LLMInterface
from config import OPENAI_API_KEY

class ChatGPTModel(LLMInterface):
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def get_response(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
        )
        return completion.choices[0].message.content