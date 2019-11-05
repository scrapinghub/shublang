from .shublang import *
from .parser import StatementParser


def evaluate(expression, data):
    # TODO use StatementParser.is_safe before evaluating code.
    # if StatementParser.is_safe(expression):
    # FIXME DANGEROUS!! Only for POC. This needs to be reimplemented using Lark.
    return eval(f'data|{expression}')
