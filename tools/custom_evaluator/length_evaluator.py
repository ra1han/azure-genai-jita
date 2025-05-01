class LengthEvaluator:
    def __init__(self):
        pass
    def __call__(self, *, response: str, **kwargs):
        return {"length": len(response)}
    