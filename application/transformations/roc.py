def rate_of_change(period: int, series: list[float]) -> list[float]:
    result = []
    for t in range(len(series)):
        if t < period or series[t - period] == 0:
            result.append(float("nan"))
        else:
            result.append((series[t] - series[t - period]) / series[t - period])
    return result
