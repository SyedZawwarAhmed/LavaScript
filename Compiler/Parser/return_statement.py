from Lexer.constants import *
from Parser.expression import OE
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal

def return_statement() -> bool:
    if select_rule([RETURN]):
        if match_terminal(RETURN):
            return_type = OE()
            if return_type:
                return True
    return False