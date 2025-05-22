import streamlit as st

def render_interview_summary():
    st.header("📋 Interview Summary")

    interview_log = st.session_state.get("interview_log", [])
    if not interview_log:
        st.info("No interview data available.")
        return

    total_cost = 0.0

    for i, item in enumerate(interview_log, 1):
        st.subheader(f"🧠 Question {i}")
        st.markdown(f"**Your Answer:** {item['user_answer']}")
        st.markdown(f"**Q:** {item['question']}")
        

        judge = item.get("judge_feedback", {})
        score = judge.get("score", "N/A")
        explanation = judge.get("explanation", "")
        improvement = judge.get("improvement", "")

        color = "🟢" if score >= 8 else "🟡" if score >= 5 else "🔴"
        st.markdown(f"### 🔍 Question Score: {color} **{score}/10**")
        if explanation:
            st.markdown(f"📝 *{explanation}*")
        if improvement:
            with st.expander("🔧 Suggested Improvement"):
                st.write(improvement)

        st.markdown(f"**Tokens Used:** {item.get('tokens_used', 0)} — 💰 ${item.get('cost', 0.0):.4f}")
        total_cost += item.get("cost", 0.0)

    st.markdown("---")
    st.success(f"✅ Total Cost of This Session: **${total_cost:.4f}**")
