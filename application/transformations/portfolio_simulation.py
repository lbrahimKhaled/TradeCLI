def portfolio_simulation(balance: float, price: list[float], entry: list[float], exit: list[float]) -> list[float]:
    positions_held = 0
    portfolio = []
    for i in range(len(price)):
        if exit[i] == 1:
            balance += positions_held * price[i]
        elif entry[i] == 1:
            positions_held += 1
            balance -= price[i]
        portfolio.append(balance + positions_held * price[i])
    return portfolio
