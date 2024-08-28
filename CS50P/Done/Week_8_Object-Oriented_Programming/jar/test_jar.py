from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("12")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(5)

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7
    jar.withdraw(7)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(4)

