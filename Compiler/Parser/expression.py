from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Lexer.constants import *
from Semantic.symbol_table import *
from Semantic.helpers import *

def merge_two_lists(first_list, second_list):
    return first_list + list(set(second_list) - set(first_list))

first_of_F = [THIS, IDENTIFIER, INTEGER_CONSTANT, FLOAT_CONSTANT, STRING_CONSTANT, BOOL_CONSTANT, NOT]
first_of_T = first_of_F
first_of_E = first_of_T
first_of_RE = first_of_E
first_of_AE = first_of_RE
first_of_OE = first_of_AE
first_of_E1 = [PLUS_MINUS]
first_of_OE1 = [OR]
first_of_AE1 = [AND]
first_of_RE1 = [COMPARISON]

follow_of_OE = [SEMICOLON, CLOSING_BRACKET, CLOSING_PARENTHESIS, COMMA]
follow_of_OE1 = follow_of_OE
follow_of_AE = merge_two_lists(first_of_OE1, follow_of_OE)
follow_of_AE1 = follow_of_AE
follow_of_RE = merge_two_lists(first_of_AE1, follow_of_AE)
follow_of_RE1 = follow_of_RE
follow_of_E = merge_two_lists(first_of_RE1, follow_of_RE)
follow_of_E1 = follow_of_E
follow_of_T = merge_two_lists(first_of_E1, follow_of_E)
follow_of_T1 = follow_of_T

follow_of_F = [MULTIPLY_DIVIDE_MODULUS, PLUS_MINUS, COMPARISON, AND, OR, SEMICOLON, CLOSING_BRACKET, CLOSING_PARENTHESIS, COMMA]
follow_of_F1 = follow_of_F
follow_of_F2 = follow_of_F1

primitive_data_types = ['string', 'number', 'boolean']

def OE():
    if select_rule(first_of_OE):
        if AE():
            if OE1():
                return True
    return False

def AE() -> bool:
    if select_rule(first_of_AE):
        if RE():
            if AE1():
                return True
    return False

def OE1() -> bool:
    if select_rule([OR]):
        if match_terminal(OR):
            if AE():
                if OE1():
                    return True
    elif select_rule(follow_of_OE1):
        return True
    return False

def RE() -> bool:
    if select_rule(first_of_RE):
        if E():
            if RE1():
                return True
    return False

def AE1() -> bool:
    if select_rule([AND]):
        if match_terminal(AND):
            if RE():
                if AE1():
                    return True
    elif select_rule(follow_of_AE1):
        return True
    return False

def E() -> bool:
    if select_rule(first_of_E):
        if T():
            if E1():
                return True
    return False

def E1() -> bool:
    if select_rule([PLUS_MINUS]):
        if match_terminal(PLUS_MINUS):
            if T():
                if E1():
                    return True
    elif select_rule(follow_of_E1):
        return True
    return False


def RE1() -> bool:
    if select_rule([COMPARISON]):
        if match_terminal(COMPARISON):
            if E():
                if RE1():
                    return True
    elif select_rule(follow_of_RE1):
        return True
    return False

def T() -> bool:
    if select_rule(first_of_T):
        if F():
            if T1():
                return True
    return False

def T1() -> bool:
    if select_rule([MULTIPLY_DIVIDE_MODULUS]):
        if match_terminal(MULTIPLY_DIVIDE_MODULUS):
            if F():
                if T1():
                    return True
    elif select_rule(follow_of_T1):
        return True
    return False

def F() -> bool:
    if select_rule([THIS, IDENTIFIER]):
        this_check = P()
        if this_check:
            if(this_check == "this"):
                name = match_terminal(IDENTIFIER)
                if name:
                    if F1(name, current_class_data_table):
                        return True
            else:
                function_table_row = lookup_funtion_table(name)
                if not function_table_row:
                    print(f"{name} is not defined")
                    return False
                if primitive_data_types in function_table_row.type:
                    if F1(function_table_row.type, current_class_data_table):
                        return True
                else:
                    main_table_row = lookup_main_table(function_table_row.type)
                    if not main_table_row:
                        print(f"{function_table_row.type} is not defined")
                        return False
                    if F1(main_table_row.name ,main_table_row.link):
                        return True
                    
    elif select_rule([INTEGER_CONSTANT, STRING_CONSTANT, FLOAT_CONSTANT, BOOL_CONSTANT]):
        if const():
            return True
    elif select_rule([NOT]):
        if match_terminal(NOT):
            if F():
                return True
    return False

def P() -> bool:
    if select_rule([THIS]):
        name = match_terminal(THIS)
        if name:
            if match_terminal(DOT):
                return name
    elif select_rule([IDENTIFIER]):
        return True
    return False

def F1(name_type: str, data_table: List[Data_Table_Row]) -> bool:
    if select_rule(follow_of_F1):
        return True
    elif select_rule([OPENING_BRACKET]):
        data_table_row = lookup_attribute_data_table(name_type, data_table)
        if not data_table_row:
            print(f"{name_type} does not exist")
            return False
        if match_terminal(OPENING_BRACKET):
            type_of_expression = OE()
            if type_of_expression:
                if type_of_expression != 'number':
                    print("index must be of type number.")
                    return False
                if match_terminal(CLOSING_BRACKET):
                    data_table_row = data_table_row
                    if data_table_row.type in primitive_data_types:
                        print("cannot access primitives data types")
                        return False
                    main_table_row = lookup_main_table(data_table_row.type)
                    if F1(main_table_row.name ,main_table_row.link):
                        return True
    elif select_rule([OPENING_PARENTHESIS]):
        if match_terminal(OPENING_PARENTHESIS):
            argument_list = AL()
            if argument_list:
                if match_terminal(CLOSING_PARENTHESIS):
                    function_data_table_row = lookup_function_data_table(name_type, argument_list, data_table)
                    if not function_data_table_row:
                        print(f"{name_type} does not exist")
                        return False
                    if F2(function_data_table_row.type):
                        return True
    elif select_rule([DOT]):
        if match_terminal(DOT):
            if name_type in primitive_data_types:
                print("cannot access primitives data types")
                return False
            main_table_row = lookup_main_table(name_type)
            if match_terminal(IDENTIFIER):
                if F1(main_table_row.name, main_table_row.link):
                    return True
    elif select_rule([INCREMENT_DECREMENT]):
        operator = match_terminal(INCREMENT_DECREMENT)
        if operator:
            if not compatibility_for_single_operand(name_type, operator):
                print(f"{name_type} is not compatible with {operator}")
            return True
    return False

def F2(name_type: str) -> bool:
    if select_rule([DOT]):
        if match_terminal(DOT):
            if name_type in primitive_data_types:
                print("cannot access primitives data types")
                return False
            main_table_row = lookup_main_table(name_type)
            if match_terminal(IDENTIFIER):
                if F1(main_table_row.name, main_table_row.link):
                    return True
    elif select_rule([OPENING_BRACKET]):
        if match_terminal(OPENING_BRACKET):
            type_of_expression = OE()
            if type_of_expression:
                if type_of_expression != 'number':
                    print("index must be of type number.")
                    return False
                if match_terminal(CLOSING_BRACKET):
                    data_table_row = data_table_row
                    if data_table_row.type in primitive_data_types:
                        print("cannot access primitives data types")
                        return False
                    main_table_row = lookup_main_table(data_table_row.type)
                    if F1(main_table_row.name ,main_table_row.link):
                        return True
    elif select_rule(follow_of_F2):
        return True
    return False

def AL() -> bool:
    argument_list:List[str] = [] 
    if select_rule(first_of_OE):
        if arguement(argument_list):
            if next_arguement(argument_list):
                return argument_list
    elif select_rule([CLOSING_PARENTHESIS]):
        return True
    return False

def const() -> bool:
    if select_rule([INTEGER_CONSTANT]):
        if match_terminal(INTEGER_CONSTANT):
            return True
    elif select_rule([FLOAT_CONSTANT]):
        if match_terminal(FLOAT_CONSTANT):
            return True
    elif select_rule([STRING_CONSTANT]):
        if match_terminal(STRING_CONSTANT):
            return True
    elif select_rule([BOOL_CONSTANT]):
        if match_terminal(BOOL_CONSTANT):
            return True
    return False

def arguement(argument_list: List[str]) -> bool:
    if select_rule(first_of_OE):
        type_of_expression = OE()
        if type_of_expression:
            argument_list.append(type_of_expression)
            return True
    return False

def next_arguement(argument_list: List[str]) -> bool:
    if select_rule([COMMA]):
        if match_terminal(COMMA):
            type_of_expression = OE()
            if type_of_expression:
                argument_list.append(type_of_expression)
                return True
    elif select_rule([CLOSING_PARENTHESIS]):
        return True
    return False

