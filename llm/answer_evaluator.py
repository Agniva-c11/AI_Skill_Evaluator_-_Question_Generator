from llm.llm_client import call_llm
import json

def evaluate_answer(question, correct_answer, user_answer):
    prompt = f"""
You are an expert grader.
Question: {question}
Correct Answer: {correct_answer}
User Answer: {user_answer}

Rate the user's answer from 0 to 10 (integer). Provide brief feedback.
Return strict JSON: {{ "score": <number>, "feedback": "<text>" }}
"""
    resp = call_llm(prompt)
    # try parse JSON
    try:
        return json.loads(resp)
    except Exception:
        # if LLM gave text, try to extract digits; otherwise return fallback
        return {"score": 0, "feedback": str(resp)}
