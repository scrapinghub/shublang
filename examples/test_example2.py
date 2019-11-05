from examples import clean_text
import re
from shublang import evaluate


def parse_active_ingredient(values):
    """
    Example https://www.heb.com/product-detail/benadryl-allergy-ultratabs-tablets/235091

    https://bitbucket.org/scrapinghub/smartersorting/src/f9b437f55b4895e9d9b88a8fae1d9462ab76c793/smartersorting/
    spiders/heb_com.py#lines-25

    :param values: list
    :return: str
    """

    values = map(clean_text, values)
    values = filter(None, values)
    text = ' '.join(values)
    if not text:
        return None

    text = text[:-1] if text[-1] == '.' else text
    text = re.sub(r'(active|other|inactive)\s+ingredients?\s*:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\)\.\s*', '), ', text)
    text = re.sub(r'\s+\(', ' (', text)
    return text


def test_example2():
    data = ["    Active Ingredients: Bismuth Subsalicylate (262 mg). Inactive Ingredients: Caramel,"
            " Carboxymethylcellulose Sodium, Citric Acid, Flavor, Microcrystalline Cellulose, Salicylic Acid, "
            "Sucralose, Sucrose, Water, Xanthan Gum."]

    expression = r"sanitize | sub(r'(Active|Other|Inactive)\s+Ingredients?\s*:\s*', '') | sub(r'\)\.\s*', '), ') | " \
                 r"sub(r'\s+\(', ' (',) | sub(r'.$', '',) | first"

    assert evaluate(expression, data) == parse_active_ingredient(data)
