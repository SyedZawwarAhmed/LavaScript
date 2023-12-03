from Parser.expression import OE
from Parser.function_definition import params
import Parser.parser as parser
from Parser.variable_declaration import assignment_statement
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *
from Semantic.symbol_table import current_class_data_table

from Semantic.helpers import *

def class_definition() -> bool:
    global current_class_data_table
    if select_rule([SEALED, CLASS]):
        access_modifier = Main_Table_Access_Modifier.GENERAL
        parent = None
        category = class_category()
        if category:
            if match_terminal(CLASS):
                type = Main_Table_Type.CLASS
                name = match_terminal(IDENTIFIER)
                if inheritable_class():
                    if name:
                        if match_terminal(OPENING_BRACE):
                            if class_body():
                                new_data_table = create_data_table()
                                current_class_data_table = new_data_table
                                if not insert_main_table(name, type, access_modifier, category, parent, new_data_table):
                                    print(f"Class {name} is already declared.")
                                    return False
                                if match_terminal(CLOSING_BRACE):
                                    return True
    return False

def class_category():
    if select_rule([SEALED]):
        if match_terminal(SEALED):
            return Main_Table_Category.SEALED
    elif select_rule([CLASS]):
        return Main_Table_Category.DEFAULT
    return False

def inheritable_class() -> bool:
    if select_rule([EXTENDS]):
        # if match_terminal(CLASS):
        #     if match_terminal(IDENTIFIER):
        if inheritance():
            return True
    elif select_rule([OPENING_BRACE]):
        return True
    return False

def inheritance() -> bool:
    if select_rule([EXTENDS]):
        if match_terminal(EXTENDS):
            if match_terminal(IDENTIFIER):
                return True
    elif select_rule([IMPLEMENTS]):
        if match_terminal(IMPLEMENTS):
            if match_terminal(IDENTIFIER):
                if inheritance_next():
                    return True
    elif select_rule([OPENING_BRACE]):
        return True

    return False

def inheritance_next() -> bool:
    if select_rule([COMMA]):
        if match_terminal(COMMA):
            if match_terminal(IDENTIFIER):
                if inheritance_next():
                    return True
    elif select_rule([OPENING_BRACE]):
        return True
    return False

def class_body() -> bool:
    if select_rule([IDENTIFIER, HASH, METHOD, CONSTRUCTOR]):
        if class_single_statement():
            if class_multi_statement():
                return True
    elif select_rule([CLOSING_BRACE]):
        return True
    return False

def class_single_statement() -> bool:
    if select_rule([IDENTIFIER]):
        if attribute():
            if match_terminal(SEMICOLON):
                return True
    elif select_rule([METHOD]):
        if method():
            if match_terminal(OPENING_BRACE):
                if parser.MST():
                    if match_terminal(CLOSING_BRACE):
                        return True
    elif select_rule([CONSTRUCTOR]):
        if constructor():
            return True
    return False

def attribute() -> bool:
    if select_rule([IDENTIFIER]):
        if match_terminal(IDENTIFIER):
            if assignment_statement():
                return True
    elif select_rule([HASH]):
        if match_terminal(HASH):
            if match_terminal(IDENTIFIER):
                if assignment_statement():
                    return True
    return False

def method() -> bool:
    if select_rule([METHOD]):
        if method_header():
            if match_terminal(OPENING_BRACE):
                if parser.MST():
                    if match_terminal(CLOSING_BRACE):
                        return True
    return False

def method_header() -> bool:
    if select_rule([METHOD]):
        if match_terminal(METHOD):
            if method_next():
                if match_terminal(OPENING_PARENTHESIS):
                    if params():
                        if match_terminal(CLOSING_PARENTHESIS):
                            if match_terminal(COLON):
                                if match_terminal(DATA_TYPES):
                                    return True
    return False

def method_next() -> bool:
    if select_rule([IDENTIFIER]):
        if match_terminal(IDENTIFIER):
            return True
    elif select_rule([HASH]):
        if match_terminal(HASH):
            if match_terminal(IDENTIFIER):
                return True
    return False

def constructor() -> bool:
    if select_rule([CONSTRUCTOR]):
        if match_terminal(CONSTRUCTOR):
            if match_terminal(OPENING_PARENTHESIS):
                if params():
                    if match_terminal(CLOSING_PARENTHESIS):
                        if match_terminal(OPENING_BRACE):
                            if parser.MST():
                                if match_terminal(CLOSING_BRACE):
                                    return True
    return False

def class_multi_statement() -> bool:
    if select_rule([IDENTIFIER, HASH, METHOD, CONSTRUCTOR]):
        if class_single_statement():
            if class_multi_statement():
                return True
    elif select_rule([CLOSING_BRACE]):
        return True
    return False