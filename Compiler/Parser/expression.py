from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *
from main import tokens

first_of_F = [THIS, IDENTIFIER, INTEGER_CONSTANT, FLOAT_CONSTANT, STRING_CONSTANT, BOOL_CONSTANT, NOT]
first_of_T = first_of_F
first_of_E = first_of_T
first_of_RE = first_of_E
first_of_AE = first_of_RE
first_of_OE = first_of_AE

follow_of_OE = [SEMICOLON, CLOSING_BRACKET, CLOSING_PARENTHESIS]
follow_of_OE1 = follow_of_OE
follow_of_AE = follow_of_OE1
follow_of_AE1 = follow_of_AE
follow_of_RE = follow_of_AE1
follow_of_RE1 = follow_of_RE
follow_of_E = follow_of_RE1
follow_of_E1 = follow_of_E
follow_of_T = follow_of_E1
follow_of_T1 = follow_of_T

follow_of_F = [MULTIPLY_DIVIDE_MODULUS, SEMICOLON, CLOSING_BRACKET, CLOSING_PARENTHESIS]
follow_of_F1 = follow_of_F
follow_of_F2 = follow_of_F1

def OE() -> bool:
    if select_rule(first_of_OE):
        if AE():
            if OE1():
                return True
    return False

def AE() -> bool:
    if select_rule(first_of_AE):
        if RE():
            if AE1():
                return True
    return False

def OE1() -> bool:
    if select_rule([OR]):
        if match_terminal(OR):
            if AE():
                if OE1():
                    return True
    elif select_rule(follow_of_OE1):
        return True
    return False

def RE() -> bool:
    if select_rule(first_of_RE):
        if E():
            if RE1():
                return True
    return False

def AE1() -> bool:
    if select_rule([AND]):
        if match_terminal(AND):
            if RE():
                if AE1():
                    return True
    elif select_rule([follow_of_AE1]):
        return True
    return False

def E() -> bool:
    if select_rule(first_of_E):
        if T():
            if E1():
                return True
    return False

def E1() -> bool:
    if select_rule([PLUS_MINUS]):
        if match_terminal(PLUS_MINUS):
            if T():
                if E1():
                    return True
    elif select_rule(follow_of_E1):
        return True
    return False


def RE1() -> bool:
    if select_rule([COMPARISON]):
        if match_terminal(COMPARISON):
            if E():
                if RE1():
                    return True
    elif select_rule(follow_of_RE1):
        return True
    return False

def T() -> bool:
    if select_rule(first_of_T):
        if F():
            if T1():
                return True
    return False

def T1() -> bool:
    if select_rule([MULTIPLY_DIVIDE_MODULUS]):
        if match_terminal(MULTIPLY_DIVIDE_MODULUS):
            if F():
                if T1():
                    return True
    elif select_rule(follow_of_T1):
        return True
    return False

def F() -> bool:
    if select_rule([THIS, IDENTIFIER]):
        if P():
            if match_terminal(IDENTIFIER):
                if F1():
                    return True
    elif select_rule([INTEGER_CONSTANT, STRING_CONSTANT, FLOAT_CONSTANT, BOOL_CONSTANT]):
        if const():
            return True
    elif select_rule([NOT]):
        if match_terminal(NOT):
            if F():
                return True
    return False

def P() -> bool:
    if select_rule([THIS]):
        if match_terminal(THIS):
            if match_terminal(DOT):
                return True
    elif select_rule([IDENTIFIER]):
        return True
    return False

def F1() -> bool:
    if select_rule(follow_of_F1):
        return True
    elif select_rule([OPENING_BRACKET]):
        if match_terminal(OPENING_BRACKET):
            if OE():
                if match_terminal(CLOSING_BRACKET):
                    if F1():
                        return True
    elif select_rule([OPENING_PARENTHESIS]):
        if match_terminal(OPENING_PARENTHESIS):
            if AL():
                if match_terminal(CLOSING_PARENTHESIS):
                    if F2():
                        return True
    elif select_rule([DOT]):
        if match_terminal(DOT):
            if match_terminal(IDENTIFIER):
                if F1():
                    return True
    elif select_rule([INCREMENT_DECREMENT]):
        if match_terminal(INCREMENT_DECREMENT):
            return True
    return False

def F2() -> bool:
    if select_rule([DOT]):
        if match_terminal(DOT):
            if match_terminal(IDENTIFIER):
                if F1():
                    return True
    elif select_rule([OPENING_BRACKET]):
        if match_terminal(OPENING_BRACKET):
            if OE():
                if match_terminal(CLOSING_BRACKET):
                    if F1():
                        return True
    elif select_rule(follow_of_F2):
        return True
    return False

def AL() -> bool:
    if select_rule(first_of_OE):
        if arguement():
            if next_arguement():
                return True
    elif select_rule([CLOSING_PARENTHESIS]):
        return True
    return False

def const() -> bool:
    if select_rule([INTEGER_CONSTANT]):
        if match_terminal(INTEGER_CONSTANT):
            return True
    elif select_rule([FLOAT_CONSTANT]):
        if match_terminal(FLOAT_CONSTANT):
            return True
    elif select_rule([STRING_CONSTANT]):
        if match_terminal(STRING_CONSTANT):
            return True
    elif select_rule([BOOL_CONSTANT]):
        if match_terminal(BOOL_CONSTANT):
            return True
    return False

def arguement() -> bool:
    if select_rule(first_of_OE):
        if OE():
            return True
    return False

def next_arguement() -> bool:
    if select_rule([COMMA]):
        if match_terminal(COMMA):
            if OE():
                return True
    elif select_rule([CLOSING_PARENTHESIS]):
        return True
    return False