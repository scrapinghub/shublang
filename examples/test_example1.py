from examples import clean_text
import re
from shublang import evaluate
from scrapy.loader.processors import Compose, MapCompose, Join


def parse_description(values):
    """
    Example https://www.heb.com/product-detail/benadryl-allergy-ultratabs-tablets/235091

    https://bitbucket.org/scrapinghub/smartersorting/src/f9b437f55b4895e9d9b88a8fae1d9462ab76c793/smartersorting/
    spiders/heb_com.py#lines-19

    :param values: list
    :return: str
    """

    description = Compose(
        MapCompose(clean_text),
        lambda x: filter(None, x),
        Join(' ')
    )

    return description(values)


def test_example1():

    values = [
        '- Each tablet contains 25 mg diphenhydramine HCI antihistamine',
        '- Provides allergy relief for symptoms: sneezing, runny nose, itchy nose or throat, and itchy, watery eyes',
        '- Provides cold relief for symptoms: sneezing and runny nose', '- For ages 6 and up',
        'Directions: Take every 4 to 6 hours, or as directed by a doctor. Do not take more than 6 times in 24 hours.  '
        'Adults and Children 12 Years and Over: 1 to 2 tablets.  Children 6 to Under 12 Years: 1 tablet.  '
        'Children Under 6 Years: Do not use.',
        '\n\t    \t\t\t\t\t',
        ]

    expression = r'sanitize | where (lambda x: x!="") | concat (" ")'

    assert evaluate(expression, values) == parse_description(values)
