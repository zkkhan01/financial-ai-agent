from fastapi import FastAPI
from .data import mock_prices
from .logic import sma, trend
from .chart import spark_svg

app = FastAPI(title="Financial AI Agent")

@app.get("/analyze")
def analyze(ticker: str = "DEMO"):
    prices = mock_prices()
    s5 = [x for x in sma(prices, 5) if x is not None]
    signal = trend(prices)
    chart = spark_svg(prices)
    return {"ticker": ticker, "signal": signal, "last": prices[-1], "sma5_last": s5[-1] if s5 else None, "chart_svg": chart}
