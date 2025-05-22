import os
import json
import re
import google.generativeai as genai
from prompts.build_question_evaluation_prompt import build_question_evaluation_prompt_json

def extract_json_from_text(text: str) -> dict:
    try:
        json_str = re.search(r"\{.*\}", text, re.DOTALL).group()
        return json.loads(json_str)
    except Exception:
        return {"score": None, "explanation": "Failed to extract valid JSON.", "improvement": ""}
    
def evaluate_interview_question_json(question: str, role: str = "Frontend Developer", level: str = "Medium") -> dict:
    prompt = build_question_evaluation_prompt_json(question, role, level)

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    messages = [
        {"role": "system", "content": "You are a strict and structured evaluator. Always return valid JSON."},
        {"role": "user", "content": prompt}
    ]

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)

        content = response.text

        return extract_json_from_text(content)
    except json.JSONDecodeError:
        return {"score": None, "explanation": "Invalid JSON returned.", "improvement": ""}
    except Exception as e:
        return {"score": None, "explanation": f"Error: {e}", "improvement": ""}
