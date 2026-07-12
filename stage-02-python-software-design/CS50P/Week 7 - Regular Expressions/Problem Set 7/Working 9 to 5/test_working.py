import pytest
from working import convert


def test_full_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 8:45 PM") == "10:30 to 20:45"
    assert convert("1:15 PM to 11:59 PM") == "13:15 to 23:59"


def test_times_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("1 PM to 2 PM") == "13:00 to 14:00"
    assert convert("11 AM to 12 PM") == "11:00 to 12:00"


def test_mixed_formats():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("3 PM to 11:30 PM") == "15:00 to 23:30"


def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:30 AM to 12:30 PM") == "00:30 to 12:30"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_overnight_hours():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("11 PM to 2 AM") == "23:00 to 02:00"


def test_invalid_hours():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("0:00 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 15:00 PM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:99 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 5:5 PM")


def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("9:00 am to 5:00 pm")

    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM to 05:00 PM")

    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")

    with pytest.raises(ValueError):
        convert("9:00 AM  to  5:00 PM")
