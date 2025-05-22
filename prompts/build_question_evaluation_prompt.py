def build_question_evaluation_prompt_json(question: str, role: str = "Frontend Developer", level: str = "Medium") -> str:
    return f"""
        You are an expert technical interviewer and evaluator. Always return valid JSON.

        Your job is to evaluate the following interview question for the role of {role} (difficulty: {level}):

        "{question}"

        Return your evaluation strictly in the following JSON format:

        {{
        "score": <integer from 1 to 10>,
        "explanation": "<short explanation>",
        "improvement": "<short suggestion for improvement or empty string>"
        }}
        """