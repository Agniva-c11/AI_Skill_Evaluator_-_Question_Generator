from fastapi import APIRouter, HTTPException
from services.code_executor import run_code

coding_router = APIRouter(prefix="/coding", tags=["coding"])

@coding_router.post("/submit")
def submit_code(data: dict):
    # Expect data to have: source_code, language_id (optional), test_cases (list of dicts)
    try:
        result = run_code(
            data["source_code"],
            data.get("language_id", 71),  # 71 is Python 3.8 in Judge0 mapping commonly
            data["test_cases"]
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
