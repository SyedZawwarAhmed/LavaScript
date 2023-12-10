from Parser.class_definition import method_header
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *
from Semantic.helpers import *
import Utils.config as config
# from Parser.parser import *

def interface_defintion() -> bool:
    global config
    if select_rule([INTERFACE]):
        access_modifier = Main_Table_Access_Modifier.GENERAL
        parent = []
        category = Main_Table_Category.DEFAULT
        if match_terminal(INTERFACE):
            name = match_terminal(IDENTIFIER)
            type = Main_Table_Type.INTERFACE
            if name:
                if match_terminal(OPENING_BRACE, True, Scope_Type.INTERFACE):
                    config.current_class_data_table = create_data_table()
                    if not insert_main_table(name, type, access_modifier, category, parent, config.current_class_data_table):
                        print(f"Interface {name} is already defined")
                        return False
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