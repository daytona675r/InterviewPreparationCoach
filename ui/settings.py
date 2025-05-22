import streamlit as st

def render_settings_dialog():
    with st.expander("⚙️ OpenAI Settings", expanded=False):
        model = st.selectbox("Model", ["gpt-4", "gpt-3.5-turbo"])
        temperature = st.slider("Temperature", 0.0, 1.5, 0.7, 0.1)
        top_p = st.slider("Top-p", 0.0, 1.0, 1.0, 0.05)
        frequency_penalty = st.slider("Frequency Penalty", 0.0, 2.0, 0.0, 0.1)
        presence_penalty = st.slider("Presence Penalty", 0.0, 2.0, 0.0, 0.1)
        max_tokens = st.number_input("Max Tokens", min_value=100, max_value=4000, value=1000, step=100)

        st.session_state.openai_config = {
            "model": model,
            "temperature": temperature,
            "top_p": top_p,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
            "max_tokens": max_tokens,
        }

        st.caption("These settings are applied to all OpenAI completions.")
