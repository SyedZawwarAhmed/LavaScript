from Parser.expression import OE
import Parser.parser as parser
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *

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
    elif select_rule([SEMICOLON]):
        return True
    return False