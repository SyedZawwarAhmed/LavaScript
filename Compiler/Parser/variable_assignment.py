from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *

def var_assignment() -> bool:    
    if select_rule([ASSIGN]):
        if match_terminal(ASSIGN):
            return True
    return False
