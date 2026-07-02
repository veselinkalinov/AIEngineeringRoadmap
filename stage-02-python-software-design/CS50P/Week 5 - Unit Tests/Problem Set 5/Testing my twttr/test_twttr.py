from twttr import shorten


def test_lowercase_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"


def test_uppercase_vowels():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"


def test_mixed_case_vowels():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("CS50P") == "CS50P"


def test_no_vowels():
    assert shorten("rhythm") == "rhythm"
    assert shorten("crypt") == "crypt"


def test_numbers_and_punctuation():
    assert shorten("What's up?") == "Wht's p?"
    assert shorten("CS50!") == "CS50!"


def test_empty_string():
    assert shorten("") == ""
