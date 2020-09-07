# TODO add tests for functions

import pytest
from shublang import evaluate


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ['str', [1, 2, 3]],
            ['1', '2', '3']
        ),
        (
            ['str', [1.1, 2.2, 3.3]],
            ['1.1', '2.2', '3.3']
        ),
        (
            ['str', ['1', '2', '3']],
            ['1', '2', '3']
        ),
    ]
)
def test_str(test_input, expected):
    assert evaluate(*test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ['sub(",", " ")', ['Python,Haskell,Scala,Rust']],
            ['Python Haskell Scala Rust']
        ),

        # Optional 'repl' param should work.
        (
            ['sub(",")', ['Python,Haskell,Scala,Rust']],
            ['PythonHaskellScalaRust']
        ),

        # Regular Expressions should work.
        (
            ['sub("b{2}(?:\\s+)", "xx ")', ['b bb          bbb']],
            ['b xx bbb']
        ),
    ]
)
def test_sub(test_input, expected):
    assert evaluate(*test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ['replace("cool", "dope")', ['Pretty cool']],
            ['Pretty dope']
        ),

        # Optional 'count' param should work on the first n patterns encountered.
        (
            ['replace("bb", "xx", 2)', ['bbb bbb bbb']],
            ['xxb xxb bbb']
        ),

        # Regular expressions won't work on `replace`.
        (
            ['replace("t+", "xx")', ['Regex Attempt']],
            ['Regex Attempt']
        ),
    ]
)
def test_replace(test_input, expected):
    assert evaluate(*test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ['format("Now Playing: {} and {}")', [['Rick', 'Morty']]],
            ['Now Playing: Rick and Morty']
        ),
        # Ordering should be respected
        (
            ['format("{2}, {1}, and {0}")', [['a', 'b', 'c']]],
            ['c, b, and a']
        ),
        # Lists of lists are aggregated into a list
        (
            ['format("{} and some value {}")', [[1, 2], ['x', 'y']]],
            ['1 and some value 2', 'x and some value y']
        ),
        # Args could be repeated
        (
            ['format("{0}--{0}-{1}!")', [['Re', 'Remix']]],
            ['Re--Re-Remix!']
        ),
        # Standard Formatting should work
        (
            ['format("{:.2f}")', [[7/3]]],
            ['2.33']
        ),
    ]
)
def test_format(test_input, expected):
    assert evaluate(*test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ['append("new thing")', ['A', 'B']],
            ['A', 'B', 'new thing']
        ),
        # list could be added as a single item
        (
            ['append([1, 2, "3"])', ['A', 'B']],
            ['A', 'B', [1, 2, '3']]
        ),
    ]
)
def test_append(test_input, expected):
    assert evaluate(*test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ['extend([1, 2, "3"])', ['A', 'B']],
            ['A', 'B', 1, 2, '3']
        ),

        # generators will also work
        (
            ['extend(range(3, 6))', ['A', 'B']],
            ['A', 'B', 3, 4, 5]
        ),

        # single strings are treated as iterables
        (
            ['extend("new")', ['A', 'B']],
            ['A', 'B', 'n', 'e', 'w']
        ),
    ]
)
def test_extend(test_input, expected):
    assert evaluate(*test_input) == expected


def test_extend_with_non_iterable():
    """It should raise a TypeError."""

    with pytest.raises(TypeError):
        evaluate("extend(123)", ['A', 'B'])


def test_encode():
    text = "ἀἐἠἰὀὐὠὰᾀᾐ"
    assert evaluate('encode("UTF8")', data=[text]) ==\
           [b'\xe1\xbc\x80\xe1\xbc\x90\xe1\xbc\xa0\xe1\xbc\xb0\xe1\xbd\x80\xe1\xbd\x90\xe1\xbd\xa0\xe1\xbd\xb0\xe1'
           b'\xbe\x80\xe1\xbe\x90']


def test_decode():
    text = b'\xe1\xbc\x80\xe1\xbc\x90\xe1\xbc\xa0\xe1\xbc\xb0\xe1\xbd\x80\xe1\xbd\x90\xe1\xbd\xa0\xe1\xbd\xb0\xe1' \
           b'\xbe\x80\xe1\xbe\x90'
    assert evaluate('decode("UTF8")', data=[text]) == ["ἀἐἠἰὀὐὠὰᾀᾐ"]


@pytest.mark.parametrize(
    "test_input,expected",
    [
        # should find at the entire string
        (
            ['find("th")', ['Python']],
            [2]
        ),

        # should respect where the search starts
        (
            ['find("th", 3)', ['Python']],
            [-1]
        ),

        # should respect where the search ends
        (
            ['find("th", 0, 1)', ['Python']],
            [-1]
        ),
    ]
)
def test_find(test_input, expected):
    assert evaluate(*test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ['split(",")', ['Python,Haskell,Scala,Rust']],
            [['Python', 'Haskell', 'Scala', 'Rust']]
        ),

        # maxsplit should limit the number of separations
        (
            ['split(",", 2)', ['Python,Haskell,Scala,Rust']],
            [['Python', 'Haskell', 'Scala,Rust']]
        ),
    ]
)
def test_split(test_input, expected):
    assert evaluate(*test_input) == expected


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
    assert evaluate('any', [1, False, 2]) is True
    assert evaluate('any', [0, False, None]) is False


def test_all():
    assert evaluate('all', [1, False, []]) is False
    assert evaluate('all', [1, True, [1]]) is True


def test_exists():
    assert evaluate('exists(20)', [20, 0, 1]) is True
    assert evaluate('exists(0)', [1, True, [1]]) is False


def test_none():
    assert evaluate('none(20)', [20, 0, 1]) is False
    assert evaluate('none(0)', [1, True, [1]]) is True


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
    assert evaluate("json_loads", data=[json_data]) == [{"results": ["Skoda", "Peugot", "Vauxhall"]}]


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


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ['join("")', ['A', 'B']],
            'AB'
        ),
        (
            ['join("")', ("A", "B")],
            'AB'
        ),
        (
            ['join("")', (1, 2)],
            '12'
        ),

    ]
)
def test_join(test_input, expected):
    assert evaluate(*test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ['urljoin("http://scrapinghub.com/products.html")', ['autoextract.html', 'uncork.html', 'crawlera.html']],
            [
                'http://scrapinghub.com/autoextract.html',
                'http://scrapinghub.com/uncork.html',
                'http://scrapinghub.com/crawlera.html',
            ]
        ),
        # If url is an absolute URL, the url’s host name and/or scheme will be present in the result
        (
                ['urljoin("http://www.scrapinghub.com")',
                 ['//doc.scrapinghub.com/unified_schema.html#operation/product']],
                [
                    'http://doc.scrapinghub.com/unified_schema.html#operation/product',
                ]
        ),
    ]
)
def test_urljoin(test_input, expected):
    assert evaluate(*test_input) == expected

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ['identity(True)',
             [10, 'far', ['boo', 3]]],
                True,
        ),
        (
            ['identity("InStock")',
             ["In Stock.", "Only 3 in Stock", "Stock Ok"]],
            "InStock",
        ),
        (
            ['identity((1,2,3,4,5))',
             "foo"],
            (1,2,3,4,5),
        ),
    ]
)

def test_identity(test_input, expected):
    assert evaluate(*test_input) == expected
