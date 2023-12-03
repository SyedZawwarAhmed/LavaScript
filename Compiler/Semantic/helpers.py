from typing import List
from symbol_table import *
from main_table_row import Main_Table_Row
from function_table_row import Function_Table_Row
from data_table_row import *

def create_data_table() -> List[Data_Table_Row]:
    new_table: List[Data_Table_Row] = []
    return new_table

def insert_main_table(name: str, type: str, access_modifier: str, type_modifier: str, category: str, parent: str, link: List[Data_Table_Row]) -> bool:
    for row in main_table:
        if row.name == name:
            return False
    new_row = Main_Table_Row(name, type, access_modifier, type_modifier, category, parent, link)
    main_table.append(new_row)
    return True

def insert_function_table(name: str, type: str, scope: int) -> bool:
    for row in function_table:
        if row.name == name and row.scope == scope:
            return False
    new_row = Function_Table_Row(name, type, scope)
    function_table.append(new_row)
    return True

def insert_data_table(name: str, type: Data_Table_Row_Type, access_modifier: str, type_modifier: str, data_table: List[Data_Table_Row]) -> bool:
    for row in data_table:
        if row.name == name:
            return False
    new_row = Data_Table_Row(name, type, access_modifier, type_modifier)
    data_table.append(new_row)
    return True

def lookup_main_table(name: str):
    for row in main_table:
        if row.name == name:
            return row

def lookup_attribute_data_table(name: str, data_table: List[Data_Table_Row]):
    for row in data_table:
        if row.name == name:
            return row

def lookup_function_data_table(name: str, parameter_list: List[str], data_table: List[Data_Table_Row]):
    for row in data_table:
        if row.name == name:
            for i in range(len(parameter_list)):
                if row.type.parameter_list:
                    if parameter_list[i] != row.type.parameter_list[i]:
                        return
                else:
                    return
            return row

def lookup_funtion_table(name: str):
    for row in function_table:
        if row.name == name:
            return row

def compatibility_for_two_operands(left_operand_type: str, right_operand_type: str, operator: str):
    # Define compatibility rules based on data types
    compatibility_rules = {
        '+': ['number', 'string'],    # Addition is compatible with numbers and strings
        '-': ['number'],               # Subtraction is compatible with numbers
        '*': ['number'],    # Multiplication is compatible with numbers and strings
        '/': ['number'],               # Division is compatible with numbers
        '%': ['number'],               # Modulo is compatible with numbers
        '<': ['number', 'string'],    # Less than is compatible with numbers and strings
        '>': ['number', 'string'],    # Greater than is compatible with numbers and strings
        '=': ['string', 'number', 'boolean'],  # Assignment is compatible with all types
        '!': ['boolean'],             # Exclamation mark (logical NOT) is compatible with booleans
        '&': ['boolean'],             # Ampersand (bitwise AND) is compatible with booleans
        '|': ['boolean'],             # Pipe (bitwise OR) is compatible with booleans
        '==': ['string', 'number', 'boolean'],  # Equal to is compatible with all types
        '!=': ['string', 'number', 'boolean'],  # Not equal to is compatible with all types
        '<=': ['number', 'string'],   # Less than or equal to is compatible with numbers and strings
        '>=': ['number', 'string'],   # Greater than or equal to is compatible with numbers and strings
        '&&': ['boolean'],            # Logical AND is compatible with booleans
        '||': ['boolean'],            # Logical OR is compatible with booleans
        '+=': ['number', 'string'],   # Addition assignment is compatible with numbers and strings
        '-=': ['number'],              # Subtraction assignment is compatible with numbers
        '*=': ['number'],   # Multiplication assignment is compatible with numbers and strings
        '/=': ['number'],              # Division assignment is compatible with numbers
        '%=': ['number']               # Modulo assignment is compatible with numbers
    }

    # Check if the operator is in the compatibility_rules dictionary
    if operator in compatibility_rules:
        # Check if both left and right operand types are compatible with the operator
        if left_operand_type == right_operand_type and left_operand_type in compatibility_rules[operator] and right_operand_type in compatibility_rules[operator]:
            return left_operand_type
        else:
            return
    else:
        # Operator not found in compatibility rules
        return

def compatibility_for_single_operand(operand_type: str, operator: str):
    # Define compatibility rules based on data types
    compatibility_rules = {
        '!': ['boolean'],   
        '++': ['number'],              # Increment is compatible with numbers
        '--': ['number'],              # Decrement is compatible with numbers
    }

    if operator in compatibility_rules:
        if operand_type in compatibility_rules[operator]:
            return operand_type
        else:
            return
    else:
        # Operator not found in compatibility rules
        return

def create_scope():
    global current_scope
    current_scope += 1
    scope_stack.append(current_scope)
    return

def destroy_scope():
    scope_stack.pop()
    return