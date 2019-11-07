from pipe import *
from w3lib.html import replace_entities, remove_tags
import re
import jmespath as jp
from parsel import Selector
import builtins
import math
import json

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

@Pipe
def sub(iterable, pattern, repl=None):
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
    return builtins.map(lambda x: Selector(x).xpath(pred).getall(), iterable)


@Pipe
def xpath_get(iterable, pred):
    return builtins.map(lambda x: Selector(x).xpath(pred).get(), iterable)

@Pipe
def css_getall(iterable, pred):
    return builtins.map(lambda x: Selector(x).css(pred).getall(), iterable)

@Pipe
def css_get(iterable, pred):
    return builtins.map(lambda x: Selector(x).css(pred).get(), iterable)


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
    return builtins.map(lambda x: builtins.bool(x), iterable)

@Pipe
def float(iterable):
    return builtins.map(lambda x: builtins.float(x), iterable)


@Pipe
def int(iterable):
    return builtins.map(lambda x: builtins.int(x), iterable)

@Pipe
def abs(iterable):
    return builtins.map(lambda x: builtins.abs(x), iterable)

@Pipe
def ceil(iterable):
    return builtins.map(lambda x: math.ceil(x), iterable)

@Pipe
def round(iterable, pred):
    return builtins.map(lambda x: builtins.round(x, pred), iterable)

@Pipe
def join(iterable, separator=", "):
    return separator.join(builtins.map(str, iterable))

@Pipe
def capitalize(iterable):
    return builtins.map(lambda x: x.capialize(), iterable)


@Pipe
def isdigit(iterable):
    return builtins.map(lambda x: x.isdigit(), iterable)


@Pipe
def isdecimal(iterable):
    return builtins.map(lambda x: x.isdecimal(), iterable)

@Pipe
def startswith(iterable, pred):
    return builtins.map(lambda x: x.startswith(pred), iterable)

@Pipe
def endswith(iterable, pred):
    return builtins.map(lambda x: x.endswith(pred), iterable)

@Pipe
def re_search(iterable, pattern):
    #return (re.sub(pattern, repl, x) for x in iterable)
    iterable =  builtins.map(lambda x: re.search(pattern, x), iterable)
    return builtins.map(lambda x: x.groups() if x else None, iterable)

@Pipe
def json_loads(iterable):
    return builtins.map(lambda x: json.loads(x), iterable)

filter = where