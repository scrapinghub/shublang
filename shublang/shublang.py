from pipe import *
from w3lib.html import replace_entities, remove_tags
import re
import jmespath as jp
from parsel import Selector
import builtins
import math
import json
import logging
import dateparser
from price_parser import Price
import types

"""
Conventions

1. Function names should be terse but have clear semantics
2. Functions need to be created with the point of view reusability. They should not be quick and dirty solutions that
are used just once.
3. Use logging to aid in debugging
"""

# TODO
"""
Add context variables such as URL that will be required for urljoin operation
Alternatively, should this be handled in the traversal code?

"""

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

@Pipe
def sub(iterable, pattern, repl=None):
    if not repl:
        repl = ""
    return (re.sub(pattern, repl, x) for x in iterable)


@Pipe
def encode(iterable, encoding, errors='ignore'):
    return (x.encode(encoding, errors=errors) for x in iterable)


@Pipe
def decode(iterable, encoding):
    return (x.decode(encoding) for x in iterable)


@Pipe
def sanitize(iterable):
    # TODO change name and add other options

    iterable = (x.strip() for x in iterable)
    iterable = (re.sub(r'[\n\t\r\s]+', ' ', x) for x in iterable)
    iterable = (x.encode('ascii', errors='ignore').decode('ascii') for x in iterable)
    iterable = (replace_entities(x) for x in iterable)
    iterable = (remove_tags(x) for x in iterable)
    return iterable


@Pipe
def xpath_getall(iterable, pred):
    return (Selector(x).xpath(pred).getall() for x in iterable)


@Pipe
def xpath_get(iterable, pred):
    return (Selector(x).xpath(pred).get() for x in iterable)

@Pipe
def css_getall(iterable, pred):
    return (Selector(x).css(pred).getall() for x in iterable)

@Pipe
def css_get(iterable, pred):
    return (Selector(x).css(pred).get() for x in iterable)


@Pipe
def jmespath(iterable, query):
    return (jp.search(query, x) for x in iterable)

@Pipe
def any(iterable):
    return builtins.any(iterable)

@Pipe
def all(iterable):
    return builtins.all(iterable)

@Pipe
def exists(iterable, pred):
    if pred in iterable:
        return True
    else:
        return False

@Pipe
def none(iterable, pred):
    if pred not in iterable:
        return True
    else:
        return False

@Pipe
def length(iterable):
    return len(iterable)

@Pipe
def bool(iterable):
    return (builtins.bool(x) for x in iterable)

@Pipe
def float(iterable):
    return (builtins.float(x) for x in iterable)


@Pipe
def int(iterable):
    return (builtins.int(x) for x in iterable)

@Pipe
def abs(iterable):
    return (builtins.abs(x) for x in iterable)

@Pipe
def ceil(iterable):
    return (math.ceil(x) for x in iterable)

@Pipe
def round(iterable, pred):
    return (builtins.round(x, pred) for x in iterable)

@Pipe
def join(iterable, separator=", "):
    return separator.join(builtins.map(str, iterable))

@Pipe
def capitalize(iterable):
    return (x.capitalize() for x in iterable)


@Pipe
def isdigit(iterable):
    return (x.isdigit() for x in iterable)


@Pipe
def isdecimal(iterable):
    return (x.isdecimal() for x in iterable)

@Pipe
def startswith(iterable, pred):
    return (x.startswith(pred) for x in iterable)

@Pipe
def endswith(iterable, pred):
    return (x.endswith(pred) for x in iterable)

@Pipe
def re_search(iterable, pattern):
    #return (re.sub(pattern, repl, x) for x in iterable)
    iterable =  builtins.map(lambda x: re.search(pattern, x), iterable)
    return (x.groups() if x else None for x in iterable)

@Pipe
def json_loads(iterable):
    return (json.loads(x) for x in iterable)

@Pipe
def date_format(iterable, fmt):
    return (dateparser.parse(item).strftime(fmt) for item in iterable)

@Pipe
def extract_price(iterable):
    return (str(Price.fromstring(item).amount) for item in iterable)

@Pipe
def extract_currency(iterable):
    return (Price.fromstring(item).currency for item in iterable)

filter = where
map = select

def evaluate(expression, data):
    # TODO use StatementParser.is_safe before evaluating code.
    # if StatementParser.is_safe(expression):
    # FIXME DANGEROUS!! Only for POC. This needs to be reimplemented using Lark.
    data = eval(f'data|{expression}')
    if isinstance(data, (types.GeneratorType, builtins.map)):
        data = list(data)
    return data
