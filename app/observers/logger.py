from observers.observer import Observer

class Logger(Observer):

    def __init__(self):
        with open("responses.log", "a") as log_file:
            log_file.write("Logger initialized.\n\n")

    def update(self, prompt: str, selected_model: str, selected_response: str, reason: str):
        try:
            with open("responses.log", "a",  buffering=1) as log_file:
                log_file.write(f"Prompt: {prompt}\n")
                log_file.write(f"Selected Model: {selected_model}\n")
                log_file.write(f"Selected Response: {selected_response}\n")
                log_file.write(f"Reason: {reason}\n\n")
                log_file.flush()
        except Exception as e:
            print(f"Failed to write to log: {e}")
