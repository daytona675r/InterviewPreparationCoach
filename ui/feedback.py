import streamlit as st

def render_question_score_json(data: dict):
    score = data.get("score")
    explanation = data.get("explanation", "")
    improvement = data.get("improvement", "")

    if score is not None:
        color = "🟢" if score >= 8 else "🟡" if score >= 5 else "🔴"
        st.markdown(f"### 🔍 Question Score: {color} **{score}/10**")
        st.markdown(f"📝 *{explanation}*")
        if improvement:
            with st.expander("🔧 Suggested Improvement"):
                st.write(improvement)
    else:
        st.warning("⚠️ Could not evaluate question.")
