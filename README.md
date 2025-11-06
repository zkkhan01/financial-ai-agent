# Financial Insights AI Agent (FastAPI)

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Tests](https://img.shields.io/badge/tests-pytest-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)


Analyzes a ticker's trend and returns summary + simple SVG chart (no external calls).
Swap the data provider with real APIs in `data.py` when deploying.

## Run
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
