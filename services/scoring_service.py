def compute_score(evaluation_results):
    # evaluation_results: list of dicts with at least {"score": numeric}
    if not evaluation_results:
        return 0.0
    total = 0.0
    count = 0
    for res in evaluation_results:
        # either LLM returned a dict or string JSON
        if isinstance(res, dict) and "score" in res:
            total += float(res["score"])
            count += 1
    return round(total / count, 2) if count else 0.0
