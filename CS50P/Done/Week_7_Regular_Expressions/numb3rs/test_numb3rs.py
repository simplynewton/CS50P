from numb3rs import validate
def test_valid():
    assert validate("255.255.255.255") == True
def test_invalid():
    assert validate("512.512.512.512") == False
    assert validate("192.300.1.1") == False
    assert validate("1.2.3.1000") == False
def test_edge():
    assert validate("0.0.0.0") == True
