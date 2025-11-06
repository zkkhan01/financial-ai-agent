def sma(series, k=5):
    out = []
    for i in range(len(series)):
        if i+1 < k: out.append(None)
        else: out.append(sum(series[i-k+1:i+1])/k)
    return out

def trend(series):
    if len(series) < 2: return "flat"
    return "up" if series[-1] > series[0] else "down"
