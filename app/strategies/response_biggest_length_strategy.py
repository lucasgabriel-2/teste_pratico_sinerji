from strategies.strategy import Strategy

class ResponseBiggestLengthStrategy(Strategy):
    def evaluate(self, prompt, responses: dict) -> tuple [str,str]:
        return max(responses, key=lambda k: len(responses[k])), "This was the answer with the biggest length"