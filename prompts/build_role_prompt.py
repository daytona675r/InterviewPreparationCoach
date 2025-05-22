def build_role_prompt(position, mode, difficulty, topic, job_description=None, persona=None):
    tone_description = {
        "Strict": "You are a serious, demanding interviewer who expects clear, concise answers.",
        "Friendly": "You are a supportive and relaxed interviewer who encourages the candidate.",
        "Neutral": "You are a neutral, professional interviewer with no emotional tone."
    }

    prompt = f"""
        You are simulating a mock interview as a(n) {persona} interviewer. {tone_description.get(persona, 'Friendly')}

        Target role: {position}
        Difficulty level: {difficulty}
        Interview mode: {mode}
        Topic: {topic}
        Job Description: {job_description} if provided.

        Ask one question at a time. Always wait for the user to respond.
        Maintain your selected tone throughout the conversation.
        """
    if mode == "🧠 Personality Check":
        prompt += """\n\nEvaluation Criteria:
                    - Introspection-focused
                    - Value Alignment
                    - Open Ended Questions
                    - Judgement-free"""
    elif mode == "💬 Q&A":
        prompt += """\n\nEvaluation Criteria:
                     - STAR-structured
                    - Soft skills
                    - Psychological safety
                    - Bias Avoidance"""
    elif mode == "🧪 Mock Interview":
        prompt += """\n\nEvaluation Criteria:
                    - Technical relevance
                    - Depth of reasoning
                    - Problem-solving structure
                    - Clarity and completeness"""
    return prompt.strip()
