from commands.send_request_command import SendRequestCommand
from strategies.response_coherence_strategy import ResponseCoherenceStrategy
from strategies.response_biggest_length_strategy import ResponseBiggestLengthStrategy

class CLI():

    def __init__(self):
        self.strategy = None
    
    def ask_to_continue(self):
        while True:
            print("\nDo you want to continue talking with the models?")
            print("1 - Yes!")
            print("2 - No!")
            choice = input("Enter the number of your choice: ")
            print("\n")

            try:
                choice = int(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue 

            if choice == 1:
                break
            if choice == 2:
                exit()
            else:
                print("Invalid choice! Please select a valid option.")

    def display_all_responses(self, responses):
        print("\nChatGPT Response:", responses["ChatGPT"])
        print("\n")
        print("Gemini Response:", responses["Gemini"])

    def display_selected_model_answer(self, selected_model, responses, reason):
        print("\nSelected Response:")
        print(selected_model, ":", responses[selected_model])
        print("Reason:", reason)

    def send_prompt(self):
        prompt = input("Write a message: ")
        
        command = SendRequestCommand(prompt)
        chatgpt_response, gemini_response = command.execute()

        responses = {
            "ChatGPT": chatgpt_response,
            "Gemini": gemini_response
        }

        return prompt, responses

    def select_strategy(self):
        while True:
            print("\nChoose the evaluation strategy for your next message:")
            print("1 - Coherence")
            print("2 - Response with the biggest length")
            print("3 - Show responses from both models")
            choice = input("Enter the number of your choice: ")
            print("\n")

            try:
                choice = int(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue 

            if 1 <= choice <= 3:
                if choice == 1:
                    self.strategy = ResponseCoherenceStrategy()
                elif choice == 2:
                    self.strategy = ResponseBiggestLengthStrategy()
                elif choice == 3:
                    self.strategy = None
                break
            else:
                choice
                print("Invalid choice! Please select a valid option.")

    def display_welcom_prompt(self):
        print("\n========================================================")
        print("            Welcom to the LLM connector!")
        print("========================================================\n")
    
    def start_system(self):
        self.display_welcom_prompt()
        self.select_strategy()

        while(True):
            prompt, responses = self.send_prompt()

            if self.strategy == None:
                self.display_all_responses(responses)
            else:
                selected_model, reason = self.strategy.evaluate(prompt, responses)
                self.display_selected_model_answer(selected_model, responses, reason)
            self.ask_to_continue()
            self.select_strategy()