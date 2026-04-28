def exponential_moving_average(alpha: float, series: list[float]) -> list[float]:
    result = [series[0]]
    for t in range(1, len(series)):
        result.append(alpha * series[t] + (1 - alpha) * result[t - 1])
    return result
