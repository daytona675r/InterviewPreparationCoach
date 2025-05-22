def build_zeroshot_prompt(position, mode, difficulty, topic, job_description=None):
    base = f"""
        You are acting as a professional job interviewer.
        Position: {position}.
        Interview mode: {mode}.
        Difficulty: {difficulty}.
        Topic: {topic}.
        Ask one question at a time. Wait for user response.
        """
    if job_description:
        base += f"\nJob Description:\n{job_description}"

    if mode == "🧠 Personality Check":
        base += """\n\nEvaluation Criteria:
                    - Introspection-focused
                    - Value Alignment
                    - Open Ended Questions
                    - Judgement-free"""
    elif mode == "💬 Q&A":
        base += """\n\nEvaluation Criteria:
                     - STAR-structured
                    - Soft skills
                    - Psychological safety
                    - Bias Avoidance"""
    elif mode == "🧪 Mock Interview":
        base += """\n\nEvaluation Criteria:
                    - Technical relevance
                    - Depth of reasoning
                    - Problem-solving structure
                    - Clarity and completeness"""
    return base.strip()