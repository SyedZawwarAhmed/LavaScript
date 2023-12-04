from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *
from Parser.expression import *

from Semantic.helpers import *

def var_declaration() -> bool:    
    if select_rule([DYNAMIC_STATIC]):
        if match_terminal(DYNAMIC_STATIC):
            name = match_terminal(IDENTIFIER)
            if name:
                variable_type = data_type()
                if variable_type:
                    if not insert_function_table(name, variable_type):
                        print(f"{name} is already declared.")
                        return False
                    if assignment_statement(variable_type):
                        return True
    return False

def data_type():
    if select_rule([COLON]):
        if match_terminal(COLON):
            type_of_variable = type_name()
            if type_of_variable:
                return type_of_variable
    return False

def type_name():
    if select_rule([DATA_TYPES]):
        type_of_variable = match_terminal(DATA_TYPES)
        if type_of_variable:
            return type_of_variable
    elif select_rule([IDENTIFIER]):
        type_of_object = match_terminal(IDENTIFIER)
        if type_of_object:
            main_table_row = lookup_main_table(type_of_object)
            if not main_table_row:
                print(f"{type_of_object} does not exist.")
                return False
            return type_of_object
    return False

def assignment_statement(variable_type: str) -> bool:
    if select_rule([ASSIGNMENT_OPERATOR]):
        operator = match_terminal(ASSIGNMENT_OPERATOR)
        if operator:
            type_of_expression_array = expression_array()
            if type_of_expression_array and type(type_of_expression_array) == str:
                if not compatibility_for_two_operands(variable_type, type_of_expression_array, operator):
                    print(f"expression of type {type_of_expression_array} cannot be assigned to variable of type {variable_type}")
                    return False
                return True
    elif select_rule([SEMICOLON]):
        return True
    return False

def expression_array() -> bool:
    if select_rule(first_of_OE):
        type_of_expression = OE()
        if type_of_expression:
            return type_of_expression
    elif select_rule([OPENING_BRACKET]):
        if array():
            return True
    return False

def array() -> bool:
    if select_rule([OPENING_BRACKET]):
        if match_terminal(OPENING_BRACKET):
            if array_element():
                if match_terminal(CLOSING_BRACKET):
                    return True
    return False

def array_element() -> bool:
    if select_rule([CLOSING_BRACKET]):
        return True
    elif select_rule([THIS, IDENTIFIER, INTEGER_CONSTANT, FLOAT_CONSTANT, STRING_CONSTANT, BOOL_CONSTANT, NOT, OPENING_BRACKET]):
        if expression_array():
            if next_element():
                return True
    return False

def next_element() -> bool:
    if select_rule([COMMA]):
        if match_terminal(COMMA):
            if expression_array():
                if next_element():
                    return True
    elif select_rule([CLOSING_BRACKET]):
        return True
    return False