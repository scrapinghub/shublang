# TODO add tests for functions

from shublang import evaluate


def test_any():

    assert evaluate('any', [1, False, 2]) == True
    assert evaluate('any', [0, False, None]) == False

def test_all():
    assert evaluate('all', [1, False, []]) == False
    assert evaluate('all', [1, True, [1]]) == True


def test_exists():
    assert evaluate('exists(20)', [20, 0, 1]) == True
    assert evaluate('exists(0)', [1, True, [1]]) == False


def test_none():
    assert evaluate('none(20)', [20, 0, 1]) == False
    assert evaluate('none(0)', [1, True, [1]]) == True

def test_length():
    assert evaluate('length', [20, 0, 1]) == 3
    assert evaluate('length', "length") == 6

def test_bool():
    assert list(evaluate('bool', [0, [], ''])) == [False, False, False]
    assert list(evaluate('bool', [1, [1], ''])) == [True, True, False]

def test_round():
    assert list(evaluate('round(2)', [1.221123])) == [1.22]

def test_filter():
    assert list(evaluate('filter(lambda x: x>1)', [0, 1, 2])) == [2]


def test_startswith():
    assert list(evaluate('startswith("a")', ["andrew", "alex", "akshay"])) == [True, True, True]
    assert list(evaluate('startswith("b")', ["ian"])) == [False]

def test_endswith():
    assert list(evaluate('endswith("a")', ["andrew", "alex", "akshay"])) == [False, False, False]
    assert list(evaluate('endswith("b")', ["Rob"])) == [True]