from um import count


def test_single_um():
    assert count("um") == 1
    assert count("hello, um, world") == 1


def test_multiple_um():
    assert count("um, um, um") == 3
    assert count("Um, UM, uM") == 3


def test_um_inside_other_words():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("album") == 0
    assert count("circumstance") == 0


def test_punctuation():
    assert count("Um?") == 1
    assert count("Well...um!") == 1
    assert count("(um), [um]; um.") == 3


def test_no_um():
    assert count("hello world") == 0
    assert count("") == 0
