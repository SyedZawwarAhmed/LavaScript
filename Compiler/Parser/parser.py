from typing import List
from Parser.function_definition import function_definition
from Parser.if_statement import if_statement
from Parser.loop import loop
from Lexer.constants import *
from Lexer.token import Token
from Utils.select_rule import select_rule
from variable_declaration import var_declaration
from main import tokens

i = 0

def check_is_syntax_valid():
    if S():
        if tokens[i].token_type == END_MARKER:
            return True
    return False

def S() -> bool:
    return MST()

def MST() -> bool:
    if SST():
        if MST():
            return True
    return False

def SST() -> bool:
    if select_rule([DYNAMIC_STATIC]):
        if var_declaration():
            return True
    elif select_rule([IF]):
        if if_statement():
            return True
    elif select_rule([UNTIL]):
        if loop():
            return True  
    elif select_rule([PROC]):
        if function_definition():
            return True 
    elif select_rule([SEALED, CLASS]):
        if class_definition():
            return True 
    elif select_rule([INTERFACE]):
        if interface_defintion():
            return True 
    elif select_rule([RETURN]):
        if return_statement():
            return True
    elif select_rule([ASSIGNMENT]):
        if variable_assignment():
            return True  
    elif select_rule([EXIT_SKIP]):
        if exit_skip():
            return True        
    return False


def class_definition() -> bool:
    return False

def interface_defintion() -> bool:
    return False

def return_statement() -> bool:
    return False

def variable_assignment() -> bool:
    return False

def exit_skip() -> bool:
    return False
