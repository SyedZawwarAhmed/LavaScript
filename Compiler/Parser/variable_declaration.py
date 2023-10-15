from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *

def var_declaration() -> bool:    
    if select_rule([DYNAMIC_STATIC]):
        if match_terminal(DYNAMIC_STATIC):
            if match_terminal(IDENTIFIER):
                if assignment_statement():
                    return True
    return False

def assignment_statement() -> bool:
    if select_rule([ASSIGNMENT_OPERATOR]):
        if match_terminal(ASSIGNMENT_OPERATOR):
            if expression_array():
                return True
    elif select_rule([SEMICOLON]):
        return True
    return False

def expression_array() -> bool:
    
    return False