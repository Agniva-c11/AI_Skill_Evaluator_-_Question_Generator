import httpx
import time
from config import JUDGE0_URL, RAPIDAPI_KEY

# NOTE: Some Judge0 endpoints require different headers. This function supports RapidAPI-hosted Judge0.
def run_code(source_code, language_id, test_cases):
    if not JUDGE0_URL:
        raise ValueError("JUDGE0_URL not configured in environment")

    headers = {}
    # If RAPIDAPI_KEY is present, set RapidAPI headers expected by RapidAPI-hosted Judge0
    if RAPIDAPI_KEY:
        # The host value should match the host portion of JUDGE0_URL (RapidAPI's judge0-ce.p.rapidapi.com)
        headers = {
            "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com",
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "Content-Type": "application/json"
        }

    results = []
    passed = 0

    for case in test_cases:
        payload = {
            "language_id": language_id,
            "source_code": source_code,
            "stdin": case.get("input", "")
        }

        # Create submission
        with httpx.Client(timeout=30.0) as client:
            resp = client.post(f"{JUDGE0_URL}/submissions?base64_encoded=false&wait=false", json=payload, headers=headers)
            resp.raise_for_status()
            data = resp.json()
            token = data.get("token")
            if not token:
                raise RuntimeError("Judge0 did not return a token")

            # poll for result
            for _ in range(12):  # up to ~12 * 2s = 24s
                time.sleep(2)
                status_resp = client.get(f"{JUDGE0_URL}/submissions/{token}?base64_encoded=false", headers=headers)
                status_resp.raise_for_status()
                status = status_resp.json()
                if status.get("status", {}).get("description") != "In Queue":
                    stdout = status.get("stdout") or ""
                    # remove trailing newlines/spaces for comparison
                    output = stdout.strip()
                    expected = (case.get("output") or "").strip()
                    passed_flag = output == expected
                    if passed_flag:
                        passed += 1
                    results.append({
                        "input": case.get("input"),
                        "expected": expected,
                        "got": output,
                        "status": "Passed" if passed_flag else "Failed",
                        "raw_status": status.get("status", {})
                    })
                    break
            else:
                # timed out
                results.append({
                    "input": case.get("input"),
                    "expected": case.get("output"),
                    "got": None,
                    "status": "Timeout"
                })

    return {
        "passed": passed,
        "total": len(test_cases),
        "results": results
    }
