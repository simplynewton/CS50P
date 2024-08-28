import pytest
from fuel import convert, gauge

def test_percentage():
    assert convert("1/4") == 25
    assert convert("2/4") == 50

def test_convert_exceptions():
    with pytest.raises(ValueError):
        convert("3/2") #x>y
    with pytest.raises(ValueError):
        convert("five/three")
    with pytest.raises(ValueError):
        convert("5/zero")
    with pytest.raises(ZeroDivisionError):
        convert("1/0") #division by 0

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(51) == "51%"


