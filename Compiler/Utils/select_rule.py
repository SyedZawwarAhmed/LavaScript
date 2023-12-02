from typing import List
from Lexer.token import Token
import Parser.parser as parser

def select_rule(selection_set: List) -> bool:
    from tokenset import tokens
    return tokens[parser.i].token_type in selection_set