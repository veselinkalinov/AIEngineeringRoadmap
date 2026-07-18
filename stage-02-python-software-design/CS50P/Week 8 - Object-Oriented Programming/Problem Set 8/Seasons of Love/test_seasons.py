from datetime import date

import pytest
from seasons import calculate_minutes, format_minutes, parse_date


def test_parse_date():
    assert parse_date("2000-01-01") == date(2000, 1, 1)
    assert parse_date("2024-02-29") == date(2024, 2, 29)


def test_parse_date_invalid_format():
    with pytest.raises(ValueError):
        parse_date("January 1, 2000")

    with pytest.raises(ValueError):
        parse_date("01-01-2000")

    with pytest.raises(ValueError):
        parse_date("2000/01/01")


def test_parse_date_invalid_date():
    with pytest.raises(ValueError):
        parse_date("2023-02-29")

    with pytest.raises(ValueError):
        parse_date("2000-13-01")

    with pytest.raises(ValueError):
        parse_date("2000-01-32")


def test_calculate_minutes_one_day():
    assert (
        calculate_minutes(
            date(2025, 1, 1),
            date(2025, 1, 2),
        )
        == 1440
    )


def test_calculate_minutes_one_regular_year():
    assert (
        calculate_minutes(
            date(2023, 1, 1),
            date(2024, 1, 1),
        )
        == 525600
    )


def test_calculate_minutes_one_leap_year():
    assert (
        calculate_minutes(
            date(2024, 1, 1),
            date(2025, 1, 1),
        )
        == 527040
    )


def test_calculate_minutes_same_date():
    assert (
        calculate_minutes(
            date(2025, 1, 1),
            date(2025, 1, 1),
        )
        == 0
    )


def test_calculate_minutes_future_date():
    with pytest.raises(ValueError):
        calculate_minutes(
            date(2026, 1, 2),
            date(2026, 1, 1),
        )


def test_format_minutes():
    assert format_minutes(0) == "Zero minutes"
    assert format_minutes(1440) == "One thousand, four hundred forty minutes"
    assert format_minutes(525600) == (
        "Five hundred twenty-five thousand, six hundred minutes"
    )


def test_format_minutes_has_no_and():
    assert " and " not in format_minutes(525600).lower()
