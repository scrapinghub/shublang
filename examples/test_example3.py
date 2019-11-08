from examples import clean_text
from collections import defaultdict
import re
from shublang import *
# # https://www.heb.com/product-detail/h-e-b-select-ingredients-in-house-roasted-traditional-turkey-sliced/1661266


def _parse_specification_table(self, response):
    specification_table = defaultdict(list)
    for tr in response.css('table.pdp-product-desc_specs tr'):
        tds = tr.css('td::text').getall()
        if not tds:
            continue

        (key, value) = tds
        key = key.lower()
        if 'size' in key:
            # normalize "Size" or "Size (oz.)" to "size"
            # also, extract "oz" as unit of measurement
            uom = re.search(r'\((\w+)\.?\)', key)
            uom = f' {uom.group(1)}' if uom else ''
            value = value + uom
            key = 'size'

        specification_table[key].append(value)

    return {k: ','.join(v) for (k, v) in specification_table.items()}