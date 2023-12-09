from Parser.expression import OE
import Parser.parser as parser
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *
from Parser.expression import *

from Semantic.helpers import *

def if_statement() -> bool:    
    if select_rule([IF]):
        if match_terminal(IF):
            if match_terminal(OPENING_PARENTHESIS):
                type_of_expression = OE()
                if type_of_expression and type(type_of_expression) == Function_Table_Row_Type:
                    if type_of_expression.type != 'boolean':
                        print("If condition must be of type boolean.")
                        return False
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
    elif select_rule([DYNAMIC_STATIC, IF, UNTIL, PROC, RETURN, ASSIGN, EXIT_SKIP, THIS, IDENTIFIER, INTEGER_CONSTANT, FLOAT_CONSTANT, STRING_CONSTANT, BOOL_CONSTANT, NOT, SEALED, CLASS, INTERFACE, END_MARKER, CLOSING_BRACE]):
        return True
    return False