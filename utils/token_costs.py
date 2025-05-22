def get_token_cost(model: str, prompt_tokens: int, completion_tokens: int) -> float:
    pricing = {
        "gpt-3.5-turbo": {"prompt": 0.0015, "completion": 0.002},
        "gpt-4": {"prompt": 0.03, "completion": 0.06},
    }

    if model not in pricing:
        return 0.0

    model_pricing = pricing[model]
    cost = (prompt_tokens / 1000) * model_pricing["prompt"] + \
           (completion_tokens / 1000) * model_pricing["completion"]
    return round(cost, 5)
