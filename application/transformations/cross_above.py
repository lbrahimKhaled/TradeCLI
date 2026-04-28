def cross_above(a1: list[float], a2: list[float]) -> list[float]:
    result = [0.0]
    for t in range(1, len(a1)):
        crossed = a1[t - 1] < a2[t - 1] and a1[t] > a2[t]
        result.append(1.0 if crossed else 0.0)
    return result
