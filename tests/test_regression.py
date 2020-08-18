"""This serves as a test bed for using shublang in complex real-world scenarios.
"""

from shublang import evaluate
from .utils import traverse_specs, get_resource_data


def test_get_non_empty_price():
    data = ['  \r\t   \n   ', '\n', '\n', '  \tprice: $123,823.00 \n', ' ']
    expression = 'sanitize | sub("[\$,]", "")'

    data = evaluate(expression, data)
    assert data == ['price: 123823.00']

    assert evaluate('re_search("(\d+\.\d{2})") | first | float | first', data) == 123823.00


def test_convert_product_to_bv_product_schema():
    """Converting Unified-Schema product data to a custom customer schema (BV - Amazon).
    """

    specifications = {
        "name": 'jmespath("name") | first',
        "brand_name": 'jmespath("brand") | first',
        "description": 'jmespath("description") | first',
        "category": 'jmespath("breadcrumbs[*].name") | first | join(" > ")',
        "identifier_sku": "jmespath(\"additionalProperty[?name=='asin'].value | [0]\") | first",
        "part_number": "jmespath(\"additionalProperty[?name=='model number'].value | [0]\") | first",
        "features": 'jmespath("additionalProperty[].[name, value]") | first',
        "weight": "jmespath(\"additionalProperty[?name=='item weight'].value | [0]\") | first",
        "dimensions": "jmespath(\"additionalProperty[?name=='package dimensions'].value | [0]\") | first",
        "colour": "jmespath(\"additionalProperty[?name=='colour'].value | [0]\") | first",
        "url": 'jmespath("url") | first',
        "response_url": 'jmespath("url") | first',
        "image_urls": 'jmespath("images") | first',
        "price_now": 'jmespath("offers[*].price | [0]") | first',
        "currency": 'jmespath("offers[*].currency | [0]") | first',
        "in_stock": 'jmespath("offers[*].availability | [0]") | map(lambda x: x == "InStock") | first',
        "rating_current": 'jmespath("aggregateRating.ratingValue") | map(lambda x: str(x)) | first',
        "rating_out_of": 'jmespath("aggregateRating.bestRating") | map(lambda x: str(x)) | first',
        "reviews_quantity": 'jmespath("aggregateRating.reviewCount") | map(lambda x: str(x)) | first',
        "reviews_quantity_1_star": "jmespath(\"ratingHistogram[?ratingValue=='1'].ratingPercentage | [0]\") | map(lambda x: str(x)) | first",
        "reviews_quantity_2_star": "jmespath(\"ratingHistogram[?ratingValue=='2'].ratingPercentage | [0]\") | map(lambda x: str(x)) | first",
        "reviews_quantity_3_star": "jmespath(\"ratingHistogram[?ratingValue=='3'].ratingPercentage | [0]\") | map(lambda x: str(x)) | first",
        "reviews_quantity_4_star": "jmespath(\"ratingHistogram[?ratingValue=='4'].ratingPercentage | [0]\") | map(lambda x: str(x)) | first",
        "reviews_quantity_5_star": "jmespath(\"ratingHistogram[?ratingValue=='5'].ratingPercentage | [0]\") | map(lambda x: str(x)) | first",

        # missing fields
        "is_add_on_item": None,
        "download_product_image": None,
        "amazons_choice": None,
        "get_ratings_extended": None,
        "country": None,
        "fulfilled_by": None,
        "ranking_item": None,
        "get_shipping_info": None,
        "preorder": None,
        "get_ratings": None,
        "available_online": None,
        "discovery_item_id": None,
        "stock_inventory": None,
        "description_bulletpoints": None,
        "get_video": None,
        "datapoint_identifier": None,
        "zipcode": None,
        "get_ratings_extended_limit": None,
        "video_available": None,
        "download_html": None,
        "country_code": None,
        "images": None,
        "members_only_item": None,
        "is_buybox_winner": None,
        "download_screenshot": None,
        "sold_by": None,
        "is_faux_price": None,
        "shipping_available": None,
    }

    product = get_resource_data("unified_schema_product.json")
    output = traverse_specs(specifications.copy(), product)

    assert output == get_resource_data("bv_amazon_product.json")
