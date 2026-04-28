def simple_moving_average(window: int, series: list[float]) -> list[float]:
    result = []
    for t in range(len(series)):
        if t < window - 1:
            result.append(float("nan"))
        else:
            result.append(sum(series[t - window + 1: t + 1]) / window)
    return result
