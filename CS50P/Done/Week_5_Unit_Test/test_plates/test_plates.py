from plates import is_valid

def test_valid_plates():
    assert is_valid("ACB123") == True
    assert is_valid("XY12") == True
def test_invalid_length():
    assert is_valid("A1") == False
    assert is_valid("ABVDEFG") == False
    assert is_valid("A12345") == False
    assert is_valid("AB 213") == False
    assert is_valid("AB.123") == False
    assert is_valid("AB0123") == False
    assert is_valid("123ABC") == False
    assert is_valid("0AB") == False
    assert is_valid("AB123A") == False
