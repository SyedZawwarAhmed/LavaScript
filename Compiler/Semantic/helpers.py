from typing import List
from Semantic.symbol_table import *
from Semantic.main_table_row import Main_Table_Row
from Semantic.function_table_row import *
from Semantic.data_table_row import *
from Semantic.enums import *

def create_data_table() -> List[Data_Table_Row]:
    new_table: List[Data_Table_Row] = []
    return new_table

def insert_main_table(name: str, type: Main_Table_Type, access_modifier: Main_Table_Access_Modifier, category: Main_Table_Category, parent: List[str], link: List[Data_Table_Row]) -> bool:
    for row in main_table:
        if row.name == name:
            return False
    new_row = Main_Table_Row(name, type, access_modifier, category, parent, link)
    main_table.append(new_row)
    return True

def insert_function_table(name: str, type: Function_Table_Row_Type):
    for row in function_table:
        if row.name == name and row.scope == scope_stack[-1]:
            return False
    new_row = Function_Table_Row(name, type, scope_stack[-1])
    function_table.append(new_row)
    return new_row

    

def insert_data_table(name: str, type: Data_Table_Row_Type, access_modifier: Data_Table_Access_Modifier, type_modifier: str, data_table: List[Data_Table_Row] | None) -> bool:
    if data_table != None:
        for row in data_table:
            if row.name == name:
                return False
        new_row = Data_Table_Row(name, type, access_modifier, type_modifier)
        data_table.append(new_row)
        return True
    return False

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
    for i in range(len(scope_stack) - 1 , -1, -1):
        scope = scope_stack[i]
        for row in function_table:
            if row.name == name and row.scope == scope:
                return row

def search_function_in_function_table():
    for i in range(len(scope_stack) - 2, -1, -1):
        scope = scope_stack[i] 
        for j in range(len(scope_stack) - 1, -1, -1):
            row = function_table[j]
            if row.scope == scope and row.type.return_type:
                return row
            
def compatibility_for_two_operands(left_operand_type_and_dimensions: Function_Table_Row_Type, right_operand_type_and_dimensions: Function_Table_Row_Type, operator: str):
    left_operand_type = left_operand_type_and_dimensions.type
    left_operand_dimensions = left_operand_type_and_dimensions.array_dimensions
    right_operand_type = right_operand_type_and_dimensions.type
    right_operand_dimensions = right_operand_type_and_dimensions.array_dimensions
    
    compatibility_rules = {
        '+': ['number', 'string'],
        '-': ['number'],
        '*': ['number'],
        '/': ['number'],
        '%': ['number'],
        '<': ['number', 'string'],
        '>': ['number', 'string'],
        '=': ['string', 'number', 'boolean'],
        '!': ['boolean'],
        '&': ['boolean'],
        '|': ['boolean'],
        '==': ['string', 'number', 'boolean'],
        '!=': ['string', 'number', 'boolean'],
        '<=': ['number', 'string'],
        '>=': ['number', 'string'],
        '&&': ['boolean'],
        '||': ['boolean'],
        '+=': ['number', 'string'],
        '-=': ['number'],
        '*=': ['number'],
        '/=': ['number'],
        '%=': ['number']
    }

    relational_operators = ['>', '<', '>=', '<=', '==', '!=', '&&', '||']

    if left_operand_dimensions > 0 or right_operand_dimensions > 0:
        if operator != '=':
            return
        if left_operand_dimensions != right_operand_dimensions:
            return

    if operator in compatibility_rules:
        if operator == '=':
            if left_operand_type == right_operand_type:
                return left_operand_type
        if left_operand_type == right_operand_type and left_operand_type in compatibility_rules[operator] and right_operand_type in compatibility_rules[operator]:
            if operator in relational_operators:
                return 'boolean'
            return left_operand_type
        else:
            return

def compatibility_for_single_operand(operand_type: str, operator: str):
    compatibility_rules = {
        '!': ['boolean'],
        '++': ['number'],
        '--': ['number'],
    }

    if operator in compatibility_rules:
        if operand_type in compatibility_rules[operator]:
            return operand_type
        else:
            return


def create_scope():
    global current_scope
    current_scope += 1
    scope_stack.append(current_scope)

def destroy_scope():
    scope_stack.pop()