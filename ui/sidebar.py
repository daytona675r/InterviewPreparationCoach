import streamlit as st

def render_sidebar():
    st.sidebar.header("🎯 Interview Settings")
    position = st.sidebar.text_input("Position/Role", "Frontend Developer")
    job_description = st.sidebar.text_area("Job Description (optional)")
    topic = st.sidebar.selectbox("Topic", ["General", "Tech", "Soft Skills"])
    difficulty = st.sidebar.select_slider("Difficulty", ["Easy", "Medium", "Hard"])
    mode = st.sidebar.radio("Mode", ["🧪 Mock Interview", "💬 Q&A", "🧠 Personality Check"])

    expander=st.sidebar.expander("AI prompting techniques", expanded=False)
    prompt_style = expander.selectbox("Choose prompting technique", ["Few-Shot", "Chain-of-Thought", "Zero-Shot", "Role-Based", "Self-Reflection"])
    if prompt_style == "Few-Shot":
        expander.write("_This technique provides examples to guide the model_")
    elif prompt_style == "Chain-of-Thought":
        expander.write("_This technique encourages step-by-step reasoning_")
    elif prompt_style == "Zero-Shot":
        expander.write("_This technique asks the model to generate a response without examples_")
    elif prompt_style == "Role-Based":
        expander.write("_This technique assigns a specific role to the model_")
    elif prompt_style == "Self-Reflection":
        expander.write("_This technique encourages the model to reflect on your responses, if you ask for feedback_",)

    persona = expander.selectbox("Choose AI persona", ["Friendly", "Strict", "Neutral"])

    image =st.sidebar.checkbox("Generate Interview Image", value=False)
    start = st.sidebar.button("🚀 Start Interview")
    return position, job_description, topic, difficulty, mode, prompt_style, persona, image, start
