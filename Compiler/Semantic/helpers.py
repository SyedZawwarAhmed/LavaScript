from typing import List
from data_table_row import Data_Table_Row
from main_table_row import Main_Table_Row
from tables import *

def create_data_table(name, type, access_modifier, category, parent, link) -> List[Data_Table_Row]:
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
    return False

def insert_data_table(name, type, access_modifier, type_modifier) -> bool:
    return False

def lookup_main_table():
    return

def lookup_attribute_data_table():
    return

def lookup_function_data_table(name, scope):
    return

def lookup_funtion_table():
    return

def compatibility_for_two_operands(left_operand_type, right_operand_type):
    return

def compatibility_for_single_operand(operand_type):
    return

def create_scope():
    return

def destroy_scope():
    return