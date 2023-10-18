from Parser.expression import OE
import Parser.parser as parser
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *
from Parser.expression import *

def if_statement() -> bool:    
    if select_rule([IF]):
        if match_terminal(IF):
            if match_terminal(OPENING_PARENTHESIS):
                if OE():
                    if match_terminal(CLOSING_PARENTHESIS):
                        if match_terminal(OPENING_BRACE):
                            if parser.MST():
                                if match_terminal(CLOSING_BRACE):
                                    if next():
                                        return True
    return False

def next() -> bool:
    if select_rule([ELSE]):
        if match_terminal(ELSE):
            if match_terminal(OPENING_BRACE):
                if parser.MST():
                    if match_terminal(CLOSING_BRACE):
                        return True
    elif select_rule([DYNAMIC_STATIC, IF, UNTIL, PROC, RETURN, ASSIGN, EXIT_SKIP, THIS, IDENTIFIER, INTEGER_CONSTANT, FLOAT_CONSTANT, STRING_CONSTANT, BOOL_CONSTANT, NOT]):
        return True
    return False