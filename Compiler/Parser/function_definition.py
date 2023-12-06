from Parser.expression import OE
import Parser.parser as parser
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *
from Parser.variable_declaration import *

def function_definition() -> bool:    
    if select_rule([PROC]):
        if match_terminal(PROC):
            if match_terminal(IDENTIFIER):
                if match_terminal(OPENING_PARENTHESIS):
                    create_scope()
                    parameter_type_list = params()
                    if parameter_type_list:
                        if match_terminal(CLOSING_PARENTHESIS):
                            return_type = data_type()
                            if return_type:
                                if match_terminal(OPENING_BRACE, False):
                                    if parser.MST():
                                        if match_terminal(CLOSING_BRACE):
                                            return True
    return False

def params():
    parameter_type_list = []
    if select_rule([IDENTIFIER]):
        if parameter(parameter_type_list):
            if next_parameter(parameter_type_list):
                return parameter_type_list
        
    elif select_rule([CLOSING_PARENTHESIS]):
        return True
    return False

def next_parameter(parameter_type_list: List[str]):
    if select_rule([COMMA]):
        if match_terminal(COMMA):
            if parameter(parameter_type_list):
                return True
    elif select_rule([CLOSING_PARENTHESIS]):
        return True
    return False

def parameter(parameter_type_list: List[str]):
    if select_rule([IDENTIFIER]):
        parameter_name = match_terminal(IDENTIFIER)
        if parameter_name:
            parameter_type = data_type()
            if parameter_type:
               new_type = Function_Table_Row_Type(parameter_type)
               if not insert_function_table(parameter_name, new_type):
                   print(f"Parameter {parameter_name} is already declared.")
                   return False
               parameter_type_list.append(parameter_type)
               return True
    return False