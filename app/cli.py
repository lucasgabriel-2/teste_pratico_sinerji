from commands.send_request_command import SendRequestCommand
from strategies.response_coherence_strategy import ResponseCoherenceStrategy
from strategies.response_biggest_length_strategy import ResponseBiggestLengthStrategy
from observers.result_presentation import ResultPresentation
from observers.logger import Logger
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

    def send_prompt(self):
        prompt = input("Write a message: ")
        print("\n")
        
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
            choice = input("Enter the number of your choice: ")
            print("\n")

            try:
                choice = int(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue 

            if 1 <= choice <= 2:
                if choice == 1:
                    self.strategy = ResponseCoherenceStrategy()
                elif choice == 2:
                    self.strategy = ResponseBiggestLengthStrategy()
                break
            else:
                choice
                print("Invalid choice! Please select a valid option.")

    def display_welcom_prompt(self):
        print("\n========================================================")
        print("            Welcom to the LLM connector!")
        print("========================================================\n")
    
    def start_system(self):
        presentation = ResultPresentation()
        logger = Logger()

        self.display_welcom_prompt()
        self.select_strategy()

        while(True):
            prompt, responses = self.send_prompt()

            selected_model, reason = self.strategy.evaluate(prompt, responses)
            selected_response = responses[selected_model]
            
            presentation.update(prompt, selected_model, selected_response, reason)
            logger.update(prompt, selected_model, selected_response, reason)

            self.ask_to_continue()