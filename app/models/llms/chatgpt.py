from openai import OpenAI
from models.llms.llm_interface import LLMInterface
from config import OPENAI_API_KEY

class ChatGPTModel(LLMInterface):
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def get_response(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
        )
        return completion.choices[0].message.content