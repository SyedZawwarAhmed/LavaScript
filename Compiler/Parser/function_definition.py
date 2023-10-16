from Parser.expression import OE
from Parser.parser import MST
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *

def function_definition() -> bool:    
    if select_rule([PROC]):
        if match_terminal(PROC):
            if match_terminal(IDENTIFIER):
                if match_terminal(OPENING_PARENTHESIS):
                    if params():
                        if match_terminal(CLOSING_PARENTHESIS):
                            if match_terminal(COLON):
                                if match_terminal(DATA_TYPES):
                                    if match_terminal(OPENING_BRACE):
                                        if MST():
                                            if match_terminal(CLOSING_BRACE):
                                                return True
    return False

def params():
    if select_rule([IDENTIFIER]):
        if parameter():
            if next_parameter():
                return True
        
    elif select_rule([CLOSING_PARENTHESIS]):
        return True
    return False

def next_parameter():
    if select_rule([COMMA]):
        if match_terminal(COMMA):
            if parameter():
                return True
    elif select_rule([CLOSING_PARENTHESIS]):
        return True
    return False

def parameter():
    if select_rule([IDENTIFIER]):
        if match_terminal(IDENTIFIER):
            if match_terminal(COLON):
                if match_terminal(DATA_TYPES):
                    return True
    return False