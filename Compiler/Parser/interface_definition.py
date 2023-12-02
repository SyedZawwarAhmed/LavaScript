from Parser.class_definition import method_header
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *

def interface_defintion() -> bool:
    if select_rule([INTERFACE]):
        if match_terminal(INTERFACE):
            if match_terminal(IDENTIFIER):
                if match_terminal(OPENING_BRACE):
                    if interface_body():
                        if match_terminal(CLOSING_BRACE):
                            return True
    return False

def interface_body() -> bool:
    if select_rule([METHOD]):
        if method_header():
            if match_terminal(SEMICOLON):
                if interface_body_next():
                    return True
    return False

def interface_body_next() -> bool:
    if select_rule([METHOD]):
        if method_header():
            if match_terminal(SEMICOLON):
                if interface_body_next():
                    return True
    elif select_rule([CLOSING_BRACE]):
        return True
    return False