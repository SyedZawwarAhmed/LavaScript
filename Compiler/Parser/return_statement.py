from Lexer.constants import *
from Parser.expression import OE
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal

def return_statement() -> bool:
    if select_rule([RETURN]):
        if match_terminal(RETURN):
            if OE():
                return True
    return False