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

def test_date_format():
    assert evaluate('date_format("%Y-%m-%d")|first', data=['15th August 2016']) == '2016-08-15'

def test_price_1():
    assert evaluate('extract_price|first', data=['22,90 €']) == '22.90'

def test_price_2():
    assert evaluate('extract_price|first', data=['$1,199.00']) == '1199.00'

def test_price_3():
    assert evaluate('extract_price|first', data=['$12']) == '12'

def test_price_4():
    assert evaluate('extract_price|first', data=['12.000,95']) == '12000.95'

def test_currency_1():
    assert evaluate('extract_currency|first', data=['22,90 €']) == '€'

def test_currency_2():
    assert evaluate('extract_currency|first', data=['$1,199.00']) == '$'