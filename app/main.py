from models.factories.chatgpt_factory import ChatGPTFactory
from models.factories.gemini_factory import GeminiFactory

def main() -> None:
    chatgpt_factory = ChatGPTFactory
    gemini_factory = GeminiFactory

    chatgpt_model = chatgpt_factory.manufacturesLLM()
    gemini_model = gemini_factory.manufacturesLLM()

    print("ChatGPT response:", chatgpt_model.get_response("write a sentence"))
    print("Gemini response:", gemini_model.get_response("write a sentence"))

main()