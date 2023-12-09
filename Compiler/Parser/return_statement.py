from Lexer.constants import *
from Parser.expression import OE
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Parser.expression import first_of_OE
from Semantic.function_table_row import Function_Table_Row_Type
from Semantic.helpers import *

def return_statement() -> bool:
    if select_rule([RETURN]):
        if match_terminal(RETURN):
            return_type = OE_or_null()
            if return_type:
                current_function_table_row = search_function_in_function_table()
                if not current_function_table_row:
                    print("Return statement must be inside a function")
                    return False
                if return_type.type != current_function_table_row.type.return_type and return_type.array_dimensions != current_function_table_row.type.array_dimensions:
                    print("Return statement must return as function return type")
                    return False

                if type(return_type) != bool:
                    return return_type
                else:
                    return Function_Table_Row_Type("void")
    return False

def OE_or_null() -> bool | Function_Table_Row_Type:
    if select_rule(first_of_OE):
        return_type = OE()
        if return_type:
            return return_type
    elif select_rule([SEMICOLON]):
        return Function_Table_Row_Type("void")
    return False