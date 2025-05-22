import openai
import streamlit as st

def build_image_prompt(role: str, tone: str) -> str:
    return (
        f"A mock job interview scene with a {tone} interviewer for a {role} position. "
        "The interviewer is seated in a professional office setting, at a desk, facing the candidate. "
        "The environment should match the tone: friendly = relaxed startup; strict = corporate boardroom."
    )

def generate_interview_image(prompt: str, size: str = "512x512") -> str:
    response = openai.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size=size
    )
    return response.data[0].url

def render_interview_image(role: str = "Frontend Developer", tone: str = "friendly"):
    with st.expander("🖼️ Visual Interview Scene", expanded=True):
        prompt = build_image_prompt(role, tone)
        with st.spinner("Generating image..."):
            try:
                image_url = generate_interview_image(prompt)
                st.image(image_url, caption="🎥 Interview Simulation Scene")
            except Exception as e:
                st.error(f"Image generation failed: {e}")
