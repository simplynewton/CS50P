from bank import value

def test_hello():
    assert value("Hello david") == 0
    assert value("hello, david") == 0
    assert value("hello! david!!") == 0
def test_h():
    assert value("hey wsg man") == 20
    assert value("hey, i think im cooked") == 20
    assert value("hell naw you good my brotha") == 20
def test_other():
    assert value("good day sir") == 100
    assert value("Great Day Sir") == 100
    assert value("sadness is but a joke") == 100
