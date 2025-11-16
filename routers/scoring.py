from fastapi import APIRouter, HTTPException
from llm.answer_evaluator import evaluate_answer
from services.scoring_service import compute_score
from utils.ranker import rank

scoring_router = APIRouter(prefix="/score", tags=["scoring"])

@scoring_router.post("/")
def score_answers(data: dict):
    if "answers" not in data:
        raise HTTPException(status_code=400, detail="Missing 'answers' key")

    evaluations = []
    for ans in data["answers"]:
        res = evaluate_answer(
            ans["question"],
            ans["correct_answer"],
            ans["user_answer"]
        )
        evaluations.append(res)

    final_score = compute_score(evaluations)
    final_rank = rank(final_score)

    return {
        "final_score": final_score,
        "rank": final_rank,
        "details": evaluations
    }
