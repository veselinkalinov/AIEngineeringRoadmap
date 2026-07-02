from bank import value


def test_hello_lowercase():
    assert value("hello") == 0
    assert value("hello, Newman") == 0


def test_hello_case_insensitive():
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("HeLLo there") == 0


def test_starts_with_h_but_not_hello():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("How are you?") == 20


def test_otherwise():
    assert value("good morning") == 100
    assert value("what's up") == 100
    assert value("yo") == 100
