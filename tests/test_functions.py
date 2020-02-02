# TODO add tests for functions

from shublang import evaluate

def test_sub():
    text = "Python,Haskell,Scala,Rust"
    assert evaluate('sub(",", " ")', data=[text]) == ["Python Haskell Scala Rust"]

def test_sub_2():
    text = "Python,Haskell,Scala,Rust"
    assert evaluate('sub(",")', data=[text]) == ["PythonHaskellScalaRust"]

def test_encode():
    text = "ἀἐἠἰὀὐὠὰᾀᾐ"
    assert evaluate('encode("UTF8")', data=[text]) ==\
           [b'\xe1\xbc\x80\xe1\xbc\x90\xe1\xbc\xa0\xe1\xbc\xb0\xe1\xbd\x80\xe1\xbd\x90\xe1\xbd\xa0\xe1\xbd\xb0\xe1' \
           b'\xbe\x80\xe1\xbe\x90']

def test_decode():
    text = b'\xe1\xbc\x80\xe1\xbc\x90\xe1\xbc\xa0\xe1\xbc\xb0\xe1\xbd\x80\xe1\xbd\x90\xe1\xbd\xa0\xe1\xbd\xb0\xe1' \
           b'\xbe\x80\xe1\xbe\x90'
    assert evaluate('decode("UTF8")', data=[text]) == ["ἀἐἠἰὀὐὠὰᾀᾐ"]

def test_sanitize():
    text = ["Python \t\t\t\t",
            "<br/>Haskell",
            "    Rust"]
    assert evaluate("sanitize", data=text) == ["Python", "Haskell", "Rust"]

def test_xpath_getall():
    html = '<div><li class="results"><ul>Skoda</ul><ul>Vauxhall</ul><ul>Peugot</ul></li></div>'
    assert evaluate(f'xpath_getall(\'//li[@class="results"]/ul/text()\')', data=[html]) == \
           [["Skoda", "Vauxhall", "Peugot"]]

def test_xpath_get():
    html = '<div><li class="results"><ul>Skoda</ul><ul>Vauxhall</ul><ul>Peugot</ul></li></div>'
    assert evaluate(f'xpath_get(\'//li[@class="results"]/ul/text()\')', data=[html]) == ["Skoda"]


def test_css_getall():
    html = '<div><li class="results"><ul>Skoda</ul><ul>Vauxhall</ul><ul>Peugot</ul></li></div>'
    assert evaluate(f'css_getall("li.results>ul::text")', data=[html]) == \
           [["Skoda", "Vauxhall", "Peugot"]]

def test_css_get():
    html = '<div><li class="results"><ul>Skoda</ul><ul>Vauxhall</ul><ul>Peugot</ul></li></div>'
    assert evaluate(f'css_get("li.results>ul::text")', data=[html]) == ["Skoda"]

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

def test_float():
    assert evaluate('float', [20, 1, 2]) == [20.0, 1.0, 2.0]

def test_float_2():
    assert evaluate('float', ["20", "1", "2"]) == [20.0, 1.0, 2.0]

def test_int():
    assert evaluate('int', [20.0, 1.0, 2.0]) == [20, 1, 2]

def test_int_2():
    assert evaluate('int', ["20", "1", "2"]) == [20, 1, 2]

def test_abs():
    assert evaluate('abs', [-1, -2, 3]) == [1, 2, 3]

def test_ceil():
    assert evaluate('ceil', [1.5, -2.2, 3.1]) == [2, -2, 4]

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

def test_re_search():
    text = "Expected Price: $1233"
    assert evaluate('re_search(r"(\\d+)")', data=[text]) == [('1233', )]

def test_json_loads():
    json_data = '{"results":["Skoda", "Peugot", "Vauxhall"]}'
    assert evaluate("json_loads", data=[json_data]) == [{"results":["Skoda", "Peugot", "Vauxhall"]}]

def test_date_format():
    assert evaluate('date_format("%Y-%m-%d")|first', data=['15th August 2016']) == '2016-08-15'

def test_price_1():
    assert evaluate('extract_price', data=['22,90 €']) == ['22.90']

def test_price_2():
    assert evaluate('extract_price', data=['$1,199.00']) == ['1199.00']

def test_price_3():
    assert evaluate('extract_price', data=['$12']) == ['12']

def test_price_4():
    assert evaluate('extract_price', data=['12.000,95']) == ['12000.95']

def test_currency_1():
    assert evaluate('extract_currency', data=['22,90 €']) == ['€']

def test_currency_2():
    assert evaluate('extract_currency', data=['$1,199.00']) == ['$']
