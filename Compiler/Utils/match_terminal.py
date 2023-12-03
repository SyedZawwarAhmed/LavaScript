from Lexer.constants import *
import Parser.parser as parser
from Utils.get_name import get_name
from Semantic.helpers import *

def match_terminal(terminal: str):
    from tokenset import tokens
    if tokens[parser.i].token_type == terminal:
        name = get_name()
        if tokens[parser.i].token_type == OPENING_BRACE:
            create_scope()
        if tokens[parser.i].token_type == CLOSING_BRACE:
            destroy_scope()
        parser.i += 1
        return name
    else:
        return False