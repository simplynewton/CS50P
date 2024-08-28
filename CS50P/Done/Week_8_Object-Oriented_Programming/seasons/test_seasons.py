import pytest
from datetime import date
from seasons import Ageinmin


def test_parse():
    assert Ageinmin("2008-05-02").bday == date(2008, 5, 2)
    with pytest.raises(ValueError):
        Ageinmin("20000-32-01")

def test_calmin():
    # going to use set day for consistency
    set_today = date(2000, 1, 1)
    instance = Ageinmin("1999-01-01", today=set_today)
    assert instance.calcmin() == 525600

def test_mintowords():
    set_today = date(2000, 1, 1)
    instance = Ageinmin("1999-01-01", today=set_today)
    assert instance.mintowords() == "Five hundred twenty-five thousand, six hundred minutes"

if __name__ == "__main__":
    pytest.main()
