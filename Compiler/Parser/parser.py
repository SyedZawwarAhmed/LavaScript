from typing import List
from Lexer.constants import *
from Lexer.token import Token

i = 0

def select_rule(tokens: List[Token], selection_set: List) -> bool:
    return tokens[i].token_type in selection_set

def check_is_syntax_valid(tokens: List[Token]):
    if S(tokens):
        if tokens[i].token_type == END_MARKER:
            return True
    return False

def S(tokens) -> bool:
    return MST(tokens)

def MST(tokens) -> bool:
    if SST(tokens):
        if MST(tokens):
            return True
    return False

def SST(tokens) -> bool:
    if select_rule(tokens, [DYNAMIC_STATIC]):
        if var_declaration(tokens):
            return True
    elif select_rule(tokens, [IF]):
        if if_statement(tokens):
            return True
    elif select_rule(tokens, [UNTIL]):
        if loop(tokens):
            return True  
    elif select_rule(tokens, [PROC]):
        if function_definition(tokens):
            return True 
    elif select_rule(tokens, [SEALED, CLASS]):
        if class_definition(tokens):
            return True 
    elif select_rule(tokens, [INTERFACE]):
        if interface_defintion(tokens):
            return True 
    elif select_rule(tokens, [RETURN]):
        if return_statement(tokens):
            return True
    elif select_rule(tokens, [ASSIGNMENT]):
        if variable_assignment(tokens):
            return True  
    elif select_rule(tokens, [EXIT_SKIP]):
        if exit_skip(tokens):
            return True        
    return False

def var_declaration(tokens) -> bool:
    # if tokens
    return False

def if_statement(tokens) -> bool:
    return False

def loop(tokens) -> bool:
    return False

def function_definition(tokens) -> bool:
    return False

def class_definition(tokens) -> bool:
    return False

def interface_defintion(tokens) -> bool:
    return False

def return_statement(tokens) -> bool:
    return False

def variable_assignment(tokens) -> bool:
    return False

def exit_skip(tokens) -> bool:
    return False
