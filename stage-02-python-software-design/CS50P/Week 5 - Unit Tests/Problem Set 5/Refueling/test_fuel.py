import pytest
from fuel import convert, gauge


def test_convert_valid_fractions():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_convert_empty_and_full():
    assert convert("0/4") == 0
    assert convert("4/4") == 100
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_convert_value_errors():
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("1.5/3")

    with pytest.raises(ValueError):
        convert("3/2")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
