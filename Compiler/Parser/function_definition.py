from typing import Literal
from Parser.expression import OE
import Parser.parser as parser
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *
from Parser.variable_declaration import *

def function_definition() -> bool:    
    if select_rule([PROC]):
        if match_terminal(PROC):
            name = match_terminal(IDENTIFIER)
            if name:
                new_type: Function_Table_Row_Type = Function_Table_Row_Type()
                if not insert_function_table(name, new_type):
                    print(f"{name} is already declared")
                    return False
                if match_terminal(OPENING_PARENTHESIS):
                    create_scope(Scope_Type.PROCEDURE)
                    parameter_type_list = params()
                    if parameter_type_list:
                        if match_terminal(CLOSING_PARENTHESIS):
                            type_and_array_dimensions = return_type()
                            if type_and_array_dimensions and type(type_and_array_dimensions) == Function_Table_Row_Type:
                                return_type_name = type_and_array_dimensions.type
                                if return_type_name:
                                    new_type.parameter_list = parameter_type_list
                                    new_type.return_type = return_type_name
                                    new_type.array_dimensions = type_and_array_dimensions.array_dimensions
                                    if match_terminal(OPENING_BRACE, False):
                                        if parser.MST():
                                            if match_terminal(CLOSING_BRACE):
                                                return True
    return False

def params() -> List[Function_Table_Row_Type] | bool:
    parameter_type_list = []
    if select_rule([IDENTIFIER]):
        if parameter(parameter_type_list):
            if next_parameter(parameter_type_list):
                return parameter_type_list
        
    elif select_rule([CLOSING_PARENTHESIS]):
        return True
    return False

def next_parameter(parameter_type_list: List[Function_Table_Row_Type]):
    if select_rule([COMMA]):
        if match_terminal(COMMA):
            if parameter(parameter_type_list):
                return True
    elif select_rule([CLOSING_PARENTHESIS]):
        return True
    return False

def parameter(parameter_type_list: List[Function_Table_Row_Type]):
    if select_rule([IDENTIFIER]):
        parameter_name = match_terminal(IDENTIFIER)
        if parameter_name:
            type_and_array_dimensions = variable_type()
            if type_and_array_dimensions:
                parameter_type = type_and_array_dimensions.type
                if parameter_type:
                    if not insert_function_table(parameter_name, type_and_array_dimensions):
                        print(f"Parameter {parameter_name} is already declared.")
                        return False
                parameter_type_list.append(type_and_array_dimensions)
                return True
    return False

def return_type():
    if select_rule([COLON]):
        if match_terminal(COLON):
            dto = data_type_or_void()
            if dto:
                return dto

    return False

def data_type_or_void() -> Function_Table_Row_Type | Literal[False]:
    if select_rule([VOID]):
        name = match_terminal(VOID)
        if name:
            return Function_Table_Row_Type(name)
    elif select_rule([IDENTIFIER, DATA_TYPES]):
        name = type_name()
        if name:
            array_dimensions = array_def()
            if type(array_dimensions) == int:
                return Function_Table_Row_Type(name, [], None, array_dimensions)
    return False