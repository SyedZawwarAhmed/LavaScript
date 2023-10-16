from Parser.expression import OE
from Parser.parser import MST
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *

def loop() -> bool:    
    if select_rule([UNTIL]):
        if match_terminal(UNTIL):
            if match_terminal(OPENING_PARENTHESIS):
                if OE():
                    if match_terminal(CLOSING_PARENTHESIS):
                        if match_terminal(OPENING_BRACE):
                            if MST():
                                if match_terminal(CLOSING_BRACE):
                                    return True
    return False