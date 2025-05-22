import streamlit as st
from logic.openai_client import call_chatgpt
from logic.question_evaluator import evaluate_interview_question_json
from ui.feedback import render_question_score_json
from ui.summary import render_interview_summary

TOTAL_QUESTIONS = 4

def render_progress():
    question_number = st.session_state.get("question_count", 1)
    st.markdown(f"**🧭 Question {question_number} of {TOTAL_QUESTIONS}**")
    st.progress(min(question_number / TOTAL_QUESTIONS, 1.0))

def render_chat_interface(position, difficulty):
    st.subheader("💬 Interview Chat")
    render_progress()
    
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message("You").write(msg["content"])
        elif msg["role"] == "assistant":
            st.chat_message("Interviewer 🤖").write(msg["content"])
            if "cost" in msg and "feedback" in msg:
                score=msg['feedback']['score']
                color = "🟢" if score >= 8 else "🟡" if score >= 5 else "🔴"
                expander=st.expander("💡 Details", expanded=False)
                expander.markdown(f"💸 This message cost approx: ${msg['cost']}")
                expander.markdown(f"🔍 Question Score: {color} {score}/10")

    user_input = st.chat_input("Your response...")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner("Thinking..."):
            reply, cost, tokens = call_chatgpt(st.session_state.messages)

        feedback_data = evaluate_interview_question_json(question=reply, role=position, level=difficulty)
        st.session_state.messages.append({"role": "assistant", "content": reply, "cost": cost, "feedback": feedback_data})

        st.session_state.interview_log.append({
            "question": reply,
            "user_answer": user_input,
            "judge_feedback": feedback_data,
            "tokens_used": tokens,
            "cost": cost
        })
       

        # increase progress
        if "question_count" not in st.session_state:
            st.session_state.question_count = 1
        st.session_state.question_count += 1

        # end interview
        if st.session_state.question_count > TOTAL_QUESTIONS:
            st.success("✅ Interview complete! You've reached the end of the interview session.")
            render_interview_summary()
            st.stop()
        st.rerun()
