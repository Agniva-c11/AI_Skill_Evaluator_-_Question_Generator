def rank(score):
    try:
        sc = float(score)
    except Exception:
        return "D"
    if sc >= 9: return "S"
    if sc >= 8: return "A"
    if sc >= 6: return "B"
    if sc >= 4: return "C"
    return "D"
