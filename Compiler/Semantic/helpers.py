from typing import List
from symbol_table import *
from main_table_row import Main_Table_Row
from function_table_row import Function_Table_Row
from data_table_row import Data_Table_Row

def create_data_table() -> List[Data_Table_Row]:
    new_table: List[Data_Table_Row] = []
    return new_table

def insert_main_table(name, type, access_modifier, type_modifier, category, parent, link) -> bool:
    for row in main_table:
        if row.name == name:
            return False
    new_row = Main_Table_Row(name, type, access_modifier, type_modifier, category, parent, link)
    main_table.append(new_row)
    return True

def insert_function_table(name, type, scope) -> bool:
    for row in function_table:
        if row.name == name and row.scope == scope:
            return False
    new_row = Function_Table_Row(name, type, scope)
    function_table.append(new_row)
    return True

def insert_data_table(name, type, access_modifier, type_modifier, data_table) -> bool:
    for row in data_table:
        if row.name == name:
            return False
    new_row = Data_Table_Row(name, type, access_modifier, type_modifier)
    data_table.append(new_row)
    return True

def lookup_main_table():
    return

def lookup_attribute_data_table():
    return

def lookup_function_data_table(name, scope):
    return

def lookup_funtion_table():
    return

def compatibility_for_two_operands(left_operand_type, right_operand_type, operator):
    return

def compatibility_for_single_operand(operand_type):
    return

def create_scope():
    global current_scope
    current_scope += 1
    scope_stack.append(current_scope)
    return

def destroy_scope():
    scope_stack.pop()
    return