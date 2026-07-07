from plates import is_valid


def test_valid_letters_only():
    assert is_valid("CS")
    assert is_valid("HELLO")


def test_valid_letters_then_numbers():
    assert is_valid("CS50")
    assert is_valid("ABC123")


def test_length():
    assert not is_valid("A")
    assert not is_valid("ABCDEFG")


def test_starts_with_two_letters():
    assert not is_valid("1A")
    assert not is_valid("A1")
    assert not is_valid("50CS")


def test_numbers_not_in_middle():
    assert not is_valid("CS50P")
    assert not is_valid("AAA22A")


def test_first_number_not_zero():
    assert not is_valid("CS05")
    assert not is_valid("ABC012")


def test_no_punctuation_or_spaces():
    assert not is_valid("CS.50")
    assert not is_valid("CS 50")
    assert not is_valid("CS-50")
