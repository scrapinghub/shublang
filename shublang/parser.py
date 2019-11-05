import shlex
import shublang
from typing import Dict, Iterable, List, Optional
from .constants import REDIRECTION_PIPE, QUOTES


class StatementParser:
    """
    StatementParser class is used to parse piped statements

    # TODO refactor with shlex

    """
    SAFE_SYMBOLS = [x for x in dir(shublang) if not x.startswith('__') and x not in ['Pipe', 'Selector']]

    def __init__(self):
        # TODO add parser configuration
        pass

    @classmethod
    def is_safe(cls, statement: str) -> bool:

        tokens = cls.tokenize(statement)
        # TODO add token validation to weed out unsafe operations
        if tokens:
            return True

    @classmethod
    def tokenize(cls, line: str) -> List[str]:

        # TODO make it more performant
        # TODO cover corner cases before ultimately moving to lark, ply or another alternative

        safe_tokens = [REDIRECTION_PIPE]
        safe_tokens.extend(cls.SAFE_SYMBOLS)
        tokenized = []
        tokens = [x.strip() for x in shlex.shlex(line, posix=False) if x.strip()]
        print(tokens)
        current_token = ""

        for token in tokens:
            print(current_token)
            if token in safe_tokens:
                if current_token:
                    tokenized.append(current_token)
                    current_token = ""
                else:
                    current_token = token
                continue
            else:
                if token == "lambda":
                    current_token = f'{current_token}{token} '
                else:
                    current_token = f'{current_token}{token}'
        tokenized.append(current_token)

        return tokenized

