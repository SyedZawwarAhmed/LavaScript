from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *
from Parser.expression import *
from Parser.variable_declaration import expression_array_object

def variable_assignment() -> bool:    
    if select_rule([ASSIGN]):
        if left_side():
            if right_side():
                return True
    return False

def left_side() -> bool:
    if select_rule([ASSIGN]):
        if P():
            if match_terminal(IDENTIFIER):
                if A2():
                    return True
    return False

def right_side() -> bool:
    if select_rule([ASSIGNMENT_OPERATOR]):
        if match_terminal(ASSIGNMENT_OPERATOR):
            if expression_array_object():
                return True
    elif select_rule([COMPOUND_ASSIGNMENT_OPERATOR]):
        if match_terminal(ASSIGNMENT_OPERATOR):
            if OE():
                return True
    return False

def A2() -> bool:
    if select_rule([ASSIGNMENT_OPERATOR, COMPOUND_ASSIGNMENT_OPERATOR]):
        return True
    elif select_rule([DOT]):
        if match_terminal(DOT):
            if match_terminal(IDENTIFIER):
                if A2():
                    return True
    elif select_rule([OPENING_BRACKET]):
        if match_terminal(OPENING_BRACKET):
            if E():
                if match_terminal(CLOSING_BRACKET):
                    if A2():
                        return True
    elif select_rule([OPENING_PARENTHESIS]):
        if match_terminal(OPENING_PARENTHESIS):
            if AL():
                if match_terminal(CLOSING_PARENTHESIS):
                    if F3():
                        return True
    return False

def F3() -> bool:
    if select_rule([DOT]):
        if match_terminal(DOT):
            if match_terminal(IDENTIFIER):
                if A2():
                    return True
    elif select_rule([OPENING_BRACKET]):
        if match_terminal(OPENING_BRACKET):
            if E():
                if match_terminal(CLOSING_BRACKET):
                    if A2():
                        return True
    return False