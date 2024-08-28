import pytest

from um import count

def test_single_case():
    assert count("Um?") == 1
    assert count("um!") == 1
    assert count("Um,") == 1
    assert count(", Um") == 1
def test_double_case():
    assert count("Um, um") == 2
    assert count("um Um") == 2
    assert count("um!u Um?") == 2
    assert count("um/n um 2a") == 2
def test_substring_case():
    assert count("Yum") == 0
    assert count("Yummy") == 0
    assert count("Tummy") == 0
    assert count("Hum") == 0
    assert count("plumb") == 0

