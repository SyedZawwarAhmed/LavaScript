from Parser.expression import OE
from Parser.function_definition import params
import Parser.parser as parser
from Parser.variable_declaration import assignment_statement
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *

from Semantic.helpers import *

def class_definition() -> bool:
    if select_rule([SEALED, CLASS]):
        access_modifier = Main_Table_Access_Modifier.GENERAL
        parent = []
        category = class_category()
        if category:
            if match_terminal(CLASS):
                type = Main_Table_Type.CLASS
                name = match_terminal(IDENTIFIER)
                if inheritable_class():
                    if name:
                        if match_terminal(OPENING_BRACE):
                            create_scope()
                            if class_body():
                                new_data_table = create_data_table()
                                if not insert_main_table(name, type, access_modifier, category, parent, new_data_table):
                                    print(f"Class {name} is already declared.")
                                    return False
                                destroy_scope()
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
    if select_rule([EXTENDS, IMPLEMENTS]):
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
            name = match_terminal(IDENTIFIER)
            if name:
                row = lookup_main_table(name)
                if row:
                    if row.type == Main_Table_Type.INTERFACE:
                        print(f"{name} cannot extend an Interface")
                        return False
                    if row.access_modifier == Main_Table_Access_Modifier.PRIVATE:
                        print(f"{name} cannot extend a Private Class")
                        return False
                    if row.category == Main_Table_Category.SEALED:
                        print(f"{name} cannot extend a Sealed Class")
                        return False
                    row.parent.append(name)
                    return True
                else:
                    print(f"{name} Class not found")
                    return False
                
    elif select_rule([IMPLEMENTS]):
        if match_terminal(IMPLEMENTS):
            name = match_terminal(IDENTIFIER)
            if name:
                row = lookup_main_table(name)
                if row:
                    if row.type == Main_Table_Type.CLASS:
                        print(f"{name} cannot implement a Class")
                        return False
                    row.parent.append(name)
                    if inheritance_next():
                        return True
                else:
                    print(f"Interface {name} not found")
                    return False

    elif select_rule([OPENING_BRACE]):
        return True

    return False

def inheritance_next() -> bool:
    if select_rule([COMMA]):
        if match_terminal(COMMA):
            name = match_terminal(IDENTIFIER)
            if name:
                row = lookup_main_table(name)
                if row:
                    if row.type == Main_Table_Type.CLASS:
                        print(f"Cannot implement {name}, which is a class")
                        return False
                    if name in row.parent:
                        print(f"Interface {name} already implemented")
                        return False
                    if inheritance_next():
                        return True
                else:
                    print(f"Interface {name} definition not found")
                    return False

    elif select_rule([OPENING_BRACE]):
        create_scope()
        return True
    return False

def class_body() -> bool:
    if select_rule([IDENTIFIER, HASH, METHOD, CONSTRUCTOR]):
        if class_single_statement():
            if class_multi_statement():
                return True
    elif select_rule([CLOSING_BRACE]):
        destroy_scope()
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