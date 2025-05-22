import streamlit as st
from ui.sidebar import render_sidebar
from ui.chat import render_chat_interface
from prompts.system_prompt import build_system_prompt
from logic.openai_client import call_chatgpt
from utils.session import init_session_state
from ui.settings import render_settings_dialog
from ui.interview_image import render_interview_image
import os

st.set_page_config(page_title="Interview Coach", layout="wide")
col1, col2 = st.columns([6, 2])
with col2:
    render_settings_dialog()
st.title("🧠 Interview Coach – Practice smarter")

init_session_state()

openai_api_key, google_api_key, position, job_description, topic, difficulty, mode, prompt_style, persona, image,  start_button = render_sidebar()


if start_button:
    st.session_state.interview_started = True
    st.session_state.question_count = 1
    st.session_state.total_tokens = 0
    st.session_state.total_cost = 0.0
    st.session_state.interview_log = []
    prompt = build_system_prompt(position, mode, difficulty, topic, job_description, prompt_style, persona)
    st.session_state.messages = [
        {"role": "system", "content": prompt},
        {"role": "assistant", "content": "Welcome to your interview! Here's your first question:", "cost": 0.0},
        {"role": "assistant", "content": "How are you doing today?", "cost": 0.0},
    ]



if st.session_state.interview_started:
    os.environ["OPENAI_API_KEY"] = openai_api_key 
    os.environ["GOOGLE_API_KEY"] = google_api_key
    if image:
        render_interview_image(role=position, tone=persona)
    render_chat_interface(position=position, difficulty=difficulty)

st.markdown("---")
total_cost = st.session_state.get("total_cost", 0.0)
st.caption(f"🧮 Total cost of this session: **${total_cost:.5f}**")
