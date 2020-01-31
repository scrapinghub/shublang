from shublang import evaluate
from parsel import Selector

def test_example_5():
    with open('examples/resources/test_example_5.html', 'r') as f:
        html = f.read()

    data = Selector(html).css('#SalesRank::text').extract()

    expression = r"sub(r',', '') | re_search(r'#(\d+)') | filter(lambda x: x) | first | int | first"

    assert evaluate(expression, data) == 12958
