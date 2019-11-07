from shublang import evaluate, xpath_getall, as_list, first, sub, re_search, json_loads, jmespath
from parsel import Selector
import re


with open('examples/resources/test_example_4.html', 'r') as f:
    html = f.read()


sel = Selector(html)
data = sel.xpath('//script[contains(., "pidData")]/text()').extract()
result = re.search(r'"pidData":({.*}),"msgs":', data[0]).groups()[0]

print(data | re_search('"pidData":({.*}),"msgs":') | first | json_loads | jmespath('pid') | first)

