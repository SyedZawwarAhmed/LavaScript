from main import tokens
from typing import List
from Lexer.constants import *
from Lexer.token import Token
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal

from Parser.variable_declaration import var_declaration
from Parser.variable_assignment import variable_assignment
from Parser.if_statement import if_statement
from Parser.loop import loop
from Parser.function_definition import function_definition
from Parser.return_statement import return_statement
from Parser.exit_skip import exit_skip
from Parser.class_definition import class_definition
from Parser.interface_definition import interface_defintion

i = 0

def check_is_syntax_valid():
    if S():
        if tokens[i].token_type == END_MARKER:
            return True
    print(f'Error at line number {tokens[i].line}')
    return False

def S() -> bool:
    if select_rule([]):
        if MST():
            if S():
                return True
    elif select_rule([SEALED, CLASS]):
        if class_definition():
            if S():
                return True 
    elif select_rule([INTERFACE]):
        if interface_defintion():
            if S():
                return True 
    return False

def MST() -> bool:
    if SST():
        if MST():
            return True
    return False

def SST() -> bool:
    if select_rule([DYNAMIC_STATIC]):
        if var_declaration():
            if match_terminal(SEMICOLON):
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
    elif select_rule([RETURN]):
        if return_statement():
            if match_terminal(SEMICOLON):
                return True  
    elif select_rule([ASSIGNMENT]):
        if variable_assignment():
            if match_terminal(SEMICOLON):
                return True  
    elif select_rule([EXIT_SKIP]):
        if exit_skip():
            if match_terminal(SEMICOLON):
                return True        
    return False
