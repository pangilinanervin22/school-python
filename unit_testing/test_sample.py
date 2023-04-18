
num = 2


def sample(num):
    return num + num


def test_sasmple():
    assert sample(2) == 42


def test_sample():
    assert sample(2) == 2, "should be zero"


def capital_case(x):
    return x.capitalize()


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
