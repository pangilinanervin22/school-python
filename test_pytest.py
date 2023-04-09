from sample import isEven


def test_square():
    n = 2
    assert n*n == 4


def test_cube():
    n = 2
    assert n*n*n == 8


def test_isOdd():
    assert (isEven(221) == True), "should be true"
    assert (isEven(2) == True)
