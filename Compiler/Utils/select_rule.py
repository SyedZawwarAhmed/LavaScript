from typing import List
from Lexer.token import Token
from Parser.parser import i
from main import tokens

def select_rule(selection_set: List) -> bool:
    return tokens[i].token_type in selection_set