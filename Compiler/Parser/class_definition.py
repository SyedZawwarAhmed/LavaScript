from Parser.expression import OE
from Parser.function_definition import params
import Parser.parser as parser
from Parser.variable_declaration import assignment_statement
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *
from Parser.variable_declaration import *

from Semantic.helpers import *

def class_definition() -> bool:
    global current_class_data_table
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
                            if class_body():
                                current_class_data_table = create_data_table()
                                if not insert_main_table(name, type, access_modifier, category, parent, current_class_data_table):
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
    if select_rule([IDENTIFIER, HASH]):
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
        name = match_terminal(IDENTIFIER)
        if name:
            type_and_array_dimensions = data_type()
            if type_and_array_dimensions:
                attribute_type = type_and_array_dimensions.type
                array_dimensions = type_and_array_dimensions.array_dimensions
                if attribute_type:
                    new_data_type = Data_Table_Row_Type(attribute_type, [], None, array_dimensions)
                    if not insert_data_table(name, new_data_type, Data_Table_Access_Modifier.PUBLIC, '', current_class_data_table):
                        print(f"Attribute {name} is already declared.")
                        return False
                    if assignment_statement(type_and_array_dimensions):
                        return True
    elif select_rule([HASH]):
        if match_terminal(HASH):
            name = match_terminal(IDENTIFIER)
            if name:
                type_and_array_dimensions = data_type()
                if type_and_array_dimensions:
                    attribute_type = type_and_array_dimensions.type
                    array_dimensions = type_and_array_dimensions.array_dimensions
                    if attribute_type:
                        new_data_type = Data_Table_Row_Type(attribute_type, [], None, array_dimensions)
                        if not insert_data_table(name, new_data_type, Data_Table_Access_Modifier.PRIVATE, '', current_class_data_table):
                            print(f"Attribute {name} is already declared.")
                            return False
                        if assignment_statement(type_and_array_dimensions):
                            return True
    return False

def method() -> bool:
    if select_rule([METHOD]):
        if method_header():
            if match_terminal(OPENING_BRACE, False):
                if parser.MST():
                    if match_terminal(CLOSING_BRACE):
                        return True
    return False

def method_header() -> bool:
    if select_rule([METHOD]):
        if match_terminal(METHOD):
            if method_next():
                if match_terminal(OPENING_PARENTHESIS):
                    create_scope()
                    if params():
                        destroy_scope()
                        if match_terminal(CLOSING_PARENTHESIS):
                            if data_type():
                                return True
    return False

def method_next() -> bool:
    if select_rule([IDENTIFIER]):
        name = match_terminal(IDENTIFIER)
        if name:
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