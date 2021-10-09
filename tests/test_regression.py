"""This serves as a test bed for using shublang in complex real-world scenarios.
"""

from shublang import evaluate


def test_get_non_empty_price():
    data = ['  \r\t   \n   ', '\n', '\n', '  \tprice: $123,823.00 \n', ' ']
    expression = 'sanitize | sub("[\$,]", "")'

    data = evaluate(expression, data)
    assert data == ['price: 123823.00']

    assert evaluate('re_search("(\d+\.\d{2})") | first | float | first', data) == 123823.00
