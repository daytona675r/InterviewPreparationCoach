import streamlit as st
import re

# --- Basic Input Validation ---
def is_valid_input(user_input: str) -> bool:
    if not user_input:
        return False
    if len(user_input) > 1000:
        return False

    blocked_phrases = [
        "ignore previous instructions",
        "you are now",
        "simulate system prompt",
        "pretend to be",
        "jailbreak",
        "act as",
    ]

    lowered = user_input.lower()
    if any(phrase in lowered for phrase in blocked_phrases):
        return False

    return True

# --- Check and Warn for Token Limit ---
def check_token_limit(limit=10000):
    if "total_tokens" not in st.session_state:
        st.session_state.total_tokens = 0

    if st.session_state.total_tokens > limit:
        st.error("🚫 Token usage limit exceeded for this session.")
        st.stop()

# --- Update Token Count after each API call ---
def track_tokens(response):
    if "usage" in response and "total_tokens" in response["usage"]:
        st.session_state.total_tokens += response["usage"]["total_tokens"]

# --- Optional: log rejected input ---
def log_rejected_input(user_input: str):
    with open("rejected_inputs.log", "a") as f:
        f.write(user_input + "\n")
