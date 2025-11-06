def mock_prices(n=60):
    # generate a gentle uptrend list of floats
    base = 100.0
    pts = []
    for i in range(n):
        base += 0.5 - (i%5==0)*0.8 + (i%7==0)*1.2
        pts.append(round(base,2))
    return pts
