from llm.llm_client import call_llm
import json

def analyze_resume(text):
    prompt = f"""
You are an expert technical interviewer.
Read this resume and extract the following fields as JSON:
- skills (list of strings)
- tech_stack (list of strings)
- domains (list of domain names / areas)
- project_insights (list of short strings describing 2-4 projects & what candidate did)

Resume text:
{text}

Return strict JSON only.
"""
    resp = call_llm(prompt)
    # try to return parsed JSON if possible
    try:
        return json.loads(resp)
    except Exception:
        # fallback: return raw string
        return {"raw": resp}
