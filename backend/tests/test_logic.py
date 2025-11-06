from app.logic import sma, trend

def test_sma():
    assert sma([1,2,3,4,5],5)[-1] == 3
def test_trend():
    assert trend([1,2,3]) == "up"
    assert trend([3,2,1]) == "down"
