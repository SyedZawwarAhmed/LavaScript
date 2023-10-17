from typing import List
from Lexer.lexer import Token
import Parser.parser as parser

def match_terminal(terminal: str) -> bool:
    from main import tokens
    if tokens[parser.i].token_type == terminal:
        parser.i += 1
        return True
    else:
        return False