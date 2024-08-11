from commands.send_request_command import SendRequestCommand

def main() -> None:
    print("\n========================================================")
    print("            Welcom to the LLM connector!")
    print("========================================================\n")
    prompt = input("Write a message: ")
    
    command = SendRequestCommand(prompt)
    chatgpt_response, gemini_response = command.execute()
    print("ChatGPT response:", chatgpt_response)
    print("Gemini response:", gemini_response)

main()