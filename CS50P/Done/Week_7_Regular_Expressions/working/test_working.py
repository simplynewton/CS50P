from working import convert
import pytest

def test_valid():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 2:45 PM")== "10:30 to 14:45"
    assert convert("9 AM to 5 PM")== "09:00 to 17:00"

def test_invalid():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5 PM")

def test_edge():
    assert convert("12:00 AM to 12:00 PM")=="00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM")=="12:00 to 00:00"
    assert convert("11:59 PM to 12:00 AM") == "23:59 to 00:00"

def test_over():
    assert convert("11:00 PM to 6:00 AM")=="23:00 to 06:00"
    assert convert("11:00 AM to 1:00 PM")=="11:00 to 13:00"
