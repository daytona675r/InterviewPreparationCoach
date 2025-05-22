import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def get_openai_settings():
    # Fallbacks, if not set in UI/session state
    return st.session_state.get("openai_config", {
        "model": "gpt-4",
        "temperature": 0.7,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "max_tokens": 1000
    })
