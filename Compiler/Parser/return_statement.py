from Lexer.constants import *
from Parser.expression import OE
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal
from Parser.expression import first_of_OE
from Semantic.function_table_row import Function_Table_Row_Type
from Semantic.helpers import *
import Utils.config as config

def return_statement():
    global config
    if select_rule([RETURN]):
        if match_terminal(RETURN):
            isInFunction, isInMethod = check_scope(Scope_Type.FUNCTION), check_scope(Scope_Type.METHOD)
            if not (isInFunction or isInMethod):
                print("Return statement must be inside a function or a class method")
                return False
            return_type = OE_or_null()
            if return_type and type(return_type) == Function_Table_Row_Type:
                current_procedure = None
                if isInFunction:
                    current_procedure = search_function_in_function_table()
                elif isInMethod:
                    current_procedure = search_method_in_data_table()

                if not current_procedure:
                    print("Return statement must be inside a function or a class method")
                    return False
                if return_type.type != current_procedure.type.return_type or return_type.array_dimensions != current_procedure.type.array_dimensions:
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