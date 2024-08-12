from strategies.strategy import Strategy
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import GEval

class ResponseCoherenceStrategy(Strategy):
    def evaluate(self, prompt: str, responses: dict) -> tuple [str,str]:
        best_model = None
        best_score = float('-inf')

        for model, response in responses.items():
            test_case = LLMTestCase(input=prompt, actual_output=response)
            coherence_metric = GEval(
                name="Coherence",
                criteria="Coherence - the collective quality of all sentences in the actual output",
                evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
                model="gpt-4o-mini"
            )

            coherence_metric.measure(test_case)
            score = coherence_metric.score
            reason = coherence_metric.reason

            # print(f"{model} Coherence Score: {score}")
            # print(f"{model} Reason: {reason}\n")

            if score > best_score:
                best_score = score
                best_model = model
                best_model_reason = reason

        return best_model, best_model_reason