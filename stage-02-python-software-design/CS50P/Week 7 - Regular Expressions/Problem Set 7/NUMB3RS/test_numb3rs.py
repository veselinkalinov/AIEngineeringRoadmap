from numb3rs import validate


def test_valid():
    assert validate("0.0.0.0")
    assert validate("255.255.255.255")
    assert validate("192.168.1.1")
    assert validate("1.2.3.4")


def test_invalid_range():
    assert not validate("256.1.1.1")
    assert not validate("1.256.1.1")
    assert not validate("1.1.1.256")
    assert not validate("300.300.300.300")


def test_invalid_format():
    assert not validate("1.2.3")
    assert not validate("1.2.3.4.5")
    assert not validate("...")
    assert not validate("")


def test_invalid_characters():
    assert not validate("cat")
    assert not validate("1.2.3.a")
    assert not validate("1.2.3.4a")
    assert not validate("1.2.3.-4")
