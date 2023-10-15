from typing import List
from Lexer.lexer import Token
from Parser.parser import i
from main import tokens

def match_terminal(terminal: str) -> bool:
    if tokens[i].token_type == terminal:
        i += 1
        return True
    else:
        return False