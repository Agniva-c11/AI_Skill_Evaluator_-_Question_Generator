from llm.llm_client import call_llm
import json

def generate_questions_from_resume(analysis_json):
    prompt = f"""
Based on this resume analysis (JSON):
{analysis_json}

Generate 6 theoretical questions and 2 coding questions (with solution and a few test_cases).
Return JSON with keys: theoretical (list of {{question, answer}}), coding (list of {{question, solution, test_cases}}).
"""
    resp = call_llm(prompt)
    try:
        return json.loads(resp)
    except Exception:
        return {"raw": resp}

def generate_topic_questions(topic):
    prompt = f"""
Generate 10 theoretical and 3 coding questions for topic: {topic}.
Return JSON similar to:
{{ "theoretical":[{{"question":"", "answer":""}}], "coding":[{{"question":"", "solution":"", "test_cases":[{{"input":"", "output":""}}]}}] }}
"""
    resp = call_llm(prompt)
    try:
        return json.loads(resp)
    except Exception:
        return {"raw": resp}
