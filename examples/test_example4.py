from shublang import evaluate
from parsel import Selector

def test_example_4():
    with open('examples/resources/test_example_4.html', 'r') as f:
        html = f.read()


    sel = Selector(html)
    data = sel.xpath('//script[contains(., "pidData")]/text()').extract()

    assert evaluate('re_search(\'"pidData":({.*}),"msgs":\')|first|json_loads|jmespath("pid")|first', data) == '10001'

