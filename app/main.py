from commands.send_request_command import SendRequestCommand
from strategies.response_coherence_strategy import ResponseCoherenceStrategy
from strategies.response_biggest_length_strategy import ResponseBiggestLengthStrategy

def display_all_responses(responses):
    print("ChatGPT Response:", responses["ChatGPT"])
    print("Gemini Response:", responses["Gemini"])

def display_selected_model_answer(selected_model, responses, reason):
    print("Selected Response:")
    print(selected_model, ":", responses[selected_model])
    print("Reason:", reason)

def main() -> None:
    print("\n========================================================")
    print("            Welcom to the LLM connector!")
    print("========================================================\n")
    prompt = input("Write a message: ")
    
    command = SendRequestCommand(prompt)
    chatgpt_response, gemini_response = command.execute()

    responses = {
        "ChatGPT": chatgpt_response,
        "Gemini": gemini_response
    }

    print("\nChoose the evaluation strategy:")
    print("1 - Coherence")
    print("2 - Response with the biggest length")
    print("3 - Show responses from both models")
    choice = input("Enter the number of your choice: ")
    print("\n")
    strategy = None

    if choice == "1":
        strategy = ResponseCoherenceStrategy()
        selected_model, reason = strategy.evaluate(prompt, responses)
        display_selected_model_answer(selected_model, responses, reason)
    elif choice == "2":
        strategy = ResponseBiggestLengthStrategy()
        selected_model, reason = strategy.evaluate(prompt, responses)
        display_selected_model_answer(selected_model, responses, reason)
    elif choice == "3":
        display_all_responses(responses)
    else:
        print("Invalid choice! Defaulting to show responses from both models.")
        display_all_responses(responses)

main()