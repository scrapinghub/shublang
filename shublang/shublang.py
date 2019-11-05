from pipe import *
from w3lib.html import replace_entities, remove_tags
import re
import json
import jmespath as jp
from parsel import Selector

"""
Conventions

1. Function names should be terse but have clear semantics
2. Functions need to be created with the point of view reusability. They should not be quick and dirty solutions that
are used just once.
3. Use logging to aid in debugging
"""

# TODO
"""
Add context variables such as URL which that be required in urljoin operation
Alternatively, should this be handled in the traversal code

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
def xpath_getall(iterable, query):
    return (Selector(x).xpath(query).getall() for x in iterable)


@Pipe
def xpath_get(iterable, query):
    return (Selector(x).xpath(query).get() for x in iterable)


@Pipe
def jmespath(iterable, query):
    return (jp.search(query, x) for x in iterable)
