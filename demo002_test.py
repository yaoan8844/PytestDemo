# Content of demo002_test.py
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_failinig():
    assert (1, 2, 3) == (3, 2, 1)


def add(x, y):
    return x + y


def test_add_1():
    assert add(1, 2) == 3


def test_add_2():
    assert add(2, 2) == 3