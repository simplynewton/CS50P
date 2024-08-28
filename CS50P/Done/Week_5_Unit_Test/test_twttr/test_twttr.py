from twttr import shorten


def test_shorten_basic():
    assert shorten("hello") == "hll"  # Should remove 'e' and 'o'
    assert shorten("world") == "wrld"  # Should remove 'o'
    assert shorten("CS50") == "CS50"  # No vowels to remove

def test_shorten_empty():
    assert shorten("") == ""  # Empty input should return empty

def test_shorten_all_vowels():
    assert shorten("aeiou") == ""  # All vowels should be removed
    assert shorten("AEIOU") == ""  # All uppercase vowels should be removed

def test_shorten_no_vowels():
    assert shorten("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"  # No change expected

def test_shorten_mixed_case():
    assert shorten("Hello World") == "Hll Wrld"  # Remove vowels but keep spaces and punctuation
    assert shorten("Python is fun!") == "Pythn s fn!"  # Includes punctuation

def test_shorten_numbers_and_punctuation():
    assert shorten("1234") == "1234"  # Numbers should not be changed
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"  # Punctuation should not be changed
    assert shorten("a1b2c3d4!") == "1b2c3d4!"  # Remove 'a' but keep numbers and punctuation

def test_shorten_capitalized_vowels():
    assert shorten("An Example") == "n xmpl"  # Remove both 'A' and 'E'
    assert shorten("A Quick Brown Fox") == " Qck Brwn Fx"  # Remove 'A', 'u', 'i', 'o'
