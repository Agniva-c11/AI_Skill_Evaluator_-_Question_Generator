import httpx
import json
from config import OPENROUTER_API_KEY, OPENROUTER_MODEL

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def call_llm(prompt, model_override=None, timeout=30):
    model = model_override or OPENROUTER_MODEL
    if not OPENROUTER_API_KEY:
        # Fallback: return a simple deterministic response for testing locally
        # This keeps your dev flow working without exposing keys.
        return json.dumps({"score": 5, "feedback": "No API key set; this is a dummy response."})

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        with httpx.Client(timeout=timeout) as client:
            resp = client.post(OPENROUTER_URL, json=body, headers=headers)
            resp.raise_for_status()
            data = resp.json()
            # defensive extraction - depends on provider shape
            choices = data.get("choices")
            if choices and isinstance(choices, list):
                message = choices[0].get("message", {}).get("content")
                return message
            # fallback if provider returns text directly
            return data.get("text") or json.dumps(data)
    except Exception as e:
        # Return an error-like object as string so callers can handle gracefully
        return json.dumps({"error": f"LLM call failed: {e}"})
