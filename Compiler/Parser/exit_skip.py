from Lexer.constants import *

from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal

def exit_skip() -> bool:
    if select_rule([EXIT_SKIP]):
        if match_terminal(EXIT_SKIP):
            if match_terminal(SEMICOLON):
                return True
    return False