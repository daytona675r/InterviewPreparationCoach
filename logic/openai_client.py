import openai
import streamlit as st

from config.settings import OPENAI_API_KEY, get_openai_settings
from logic.security import is_valid_input, check_token_limit, track_tokens, log_rejected_input
from utils.token_costs import get_token_cost


openai.api_key = OPENAI_API_KEY

def call_chatgpt(messages):
    config = get_openai_settings()

    user_input = messages[-1]["content"] if messages else ""
    if not is_valid_input(user_input):
        st.warning("⚠️ Your input was blocked due to security filters.")
        log_rejected_input(user_input)
        st.stop()

    response = openai.chat.completions.create(
        model=config["model"],
        messages=messages,
        temperature=config["temperature"],
        top_p=config["top_p"],
        frequency_penalty=config["frequency_penalty"],
        presence_penalty=config["presence_penalty"],
        max_tokens=config["max_tokens"]
    )
    
    # Calculate token cost
    cost = get_token_cost(
        model=config["model"],
        prompt_tokens=response.usage.prompt_tokens,
        completion_tokens=response.usage.completion_tokens,
    )
    tokens=response.usage.prompt_tokens + response.usage.completion_tokens
     # Store totals
    st.session_state.total_tokens += response.usage.total_tokens
    st.session_state.total_cost += cost

    track_tokens(response)
    check_token_limit()

    return response.choices[0].message.content, cost, tokens