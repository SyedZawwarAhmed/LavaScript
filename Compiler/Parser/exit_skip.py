from Semantic.enums import Scope_Type
from Semantic.helpers import check_scope
from Lexer.constants import *

from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal

def exit_skip() -> bool:
    if select_rule([EXIT_SKIP]):
        name = match_terminal(EXIT_SKIP)
        if name:
            if not check_scope(Scope_Type.LOOP):
                print(f"{name} can only be used inside a loop.")
                return False
            return True
    return False