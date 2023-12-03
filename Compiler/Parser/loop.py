from Parser.expression import OE
import Parser.parser as parser
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *

def loop() -> bool:    
    if select_rule([UNTIL]):
        if match_terminal(UNTIL):
            if match_terminal(OPENING_PARENTHESIS):
                type_of_expression = OE()
                if type_of_expression:
                    if type_of_expression != 'boolean':
                        print("Loop condition must be of type boolean.")
                        return False
                    if match_terminal(CLOSING_PARENTHESIS):
                        if match_terminal(OPENING_BRACE):
                            if parser.MST():
                                if match_terminal(CLOSING_BRACE):
                                    return True
    return False