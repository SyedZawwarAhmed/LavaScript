from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *
from Parser.expression import *

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
    if select_rule(first_of_OE):
        if OE():
            return True
    elif select_rule([OPENING_BRACKET]):
        if array():
            return True
    return False

def array() -> bool:
    if select_rule([OPENING_BRACKET]):
        if match_terminal(OPENING_BRACKET):
            if array_element():
                if match_terminal(CLOSING_BRACKET):
                    return True
    return False

def array_element() -> bool:
    if select_rule([CLOSING_BRACKET]):
        return True
    elif select_rule([THIS, IDENTIFIER, INTEGER_CONSTANT, FLOAT_CONSTANT, STRING_CONSTANT, BOOL_CONSTANT, NOT, OPENING_BRACKET]):
        if expression_array():
            if next_element():
                return True
    return False

def next_element() -> bool:
    if select_rule([COMMA]):
        if match_terminal(COMMA):
            if expression_array():
                if next_element():
                    return True
    elif select_rule([CLOSING_BRACKET]):
        return True
    return False