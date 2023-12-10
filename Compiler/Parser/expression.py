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

def OE() -> bool | Function_Table_Row_Type:
    if select_rule(first_of_OE):
        first_operand_return_type = AE()
        if first_operand_return_type and type(first_operand_return_type) == str:
            resultant_type = OE1(first_operand_return_type)
            if resultant_type and type(resultant_type) == str:
                final_type = Function_Table_Row_Type(resultant_type)
                return final_type
    return False

def AE() -> bool | str:
    if select_rule(first_of_AE):
        first_operand_return_type = RE()
        if first_operand_return_type and type(first_operand_return_type) == str:
            resultant_type = AE1(first_operand_return_type)
            if resultant_type:
                return resultant_type
    return False

def OE1(first_operand_type: str) -> bool | str:
    if select_rule([OR]):
        operator = match_terminal(OR)
        if operator:
            second_operand_return_type = AE()
            if second_operand_return_type and type(second_operand_return_type) == str:
                resultant_type = compatibility_for_two_operands(Function_Table_Row_Type(first_operand_type), Function_Table_Row_Type(second_operand_return_type), operator)
                if not resultant_type:
                    print(f"{first_operand_type} is not compatible with {second_operand_return_type} on {operator} operator")
                    return False
                remaining_operand_return_type = OE1(resultant_type)
                if remaining_operand_return_type:
                    return remaining_operand_return_type
    elif select_rule(follow_of_OE1):
        return first_operand_type
    return False

def RE() -> bool | str:
    if select_rule(first_of_RE):
        first_operand_return_type = E()
        if first_operand_return_type and type(first_operand_return_type) == str:
            resultant_type = RE1(first_operand_return_type)
            if resultant_type:
                return resultant_type
    return False

def AE1(first_operand_type: str) -> bool | str:
    if select_rule([AND]):
        operator = match_terminal(AND)
        if operator:
            second_operand_return_type = RE()
            if second_operand_return_type and type(second_operand_return_type) == str:
                resultant_type = compatibility_for_two_operands(Function_Table_Row_Type(first_operand_type), Function_Table_Row_Type(second_operand_return_type), operator)
                if not resultant_type:
                    print(f"{first_operand_type} is not compatible with {second_operand_return_type} on {operator} operator")
                    return False
                remaining_operand_return_type = AE1(resultant_type)
                if remaining_operand_return_type:
                    return remaining_operand_return_type
    elif select_rule(follow_of_AE1):
        return first_operand_type
    return False

def E() -> bool | str:
    if select_rule(first_of_E):
        first_operand_return_type = T()
        if first_operand_return_type and type(first_operand_return_type) == str:
            resultant_type = E1(first_operand_return_type)
            if resultant_type:
                return resultant_type
    return False

def E1(first_operand_type: str) -> bool | str:
    if select_rule([PLUS_MINUS]):
        operator = match_terminal(PLUS_MINUS)
        if operator:
            second_operand_return_type = T()
            if second_operand_return_type and type(second_operand_return_type) == str:
                resultant_type = compatibility_for_two_operands(Function_Table_Row_Type(first_operand_type), Function_Table_Row_Type(second_operand_return_type), operator)
                if not resultant_type:
                    print(f"{first_operand_type} is not compatible with {second_operand_return_type} on {operator} operator")
                    return False
                remaining_operand_return_type = T1(resultant_type)
                if remaining_operand_return_type:
                    return remaining_operand_return_type
    elif select_rule(follow_of_E1):
        return first_operand_type
    return False


def RE1(first_operand_type: str) -> bool | str:
    if select_rule([COMPARISON]):
        operator = match_terminal(COMPARISON)
        if operator:
            second_operand_return_type = E()
            if second_operand_return_type and type(second_operand_return_type) == str:
                resultant_type = compatibility_for_two_operands(Function_Table_Row_Type(first_operand_type), Function_Table_Row_Type(second_operand_return_type), operator)
                if not resultant_type:
                    print(f"{first_operand_type} is not compatible with {second_operand_return_type} on {operator} operator")
                    return False
                remaining_operand_return_type = RE1(resultant_type)
                if remaining_operand_return_type:
                    return remaining_operand_return_type
    elif select_rule(follow_of_RE1):
        return first_operand_type
    return False

def T() -> bool | str: # a * b * c
    if select_rule(first_of_T):
        first_operand_return_type = F()
        if first_operand_return_type and type(first_operand_return_type) == str:
            resultant_type = T1(first_operand_return_type)
            if resultant_type:
                return resultant_type
    return False

def T1(first_operand_type: str) -> bool | str: 
    if select_rule([MULTIPLY_DIVIDE_MODULUS]):
        operator = match_terminal(MULTIPLY_DIVIDE_MODULUS)
        if operator:
            second_operand_return_type = F()
            if second_operand_return_type and type(second_operand_return_type) == str:
                resultant_type = compatibility_for_two_operands(Function_Table_Row_Type(first_operand_type), Function_Table_Row_Type(second_operand_return_type), operator)
                if not resultant_type:
                    print(f"{first_operand_type} is not compatible with {second_operand_return_type} on {operator} operator")
                    return False
                remaining_operand_return_type = T1(resultant_type)
                if remaining_operand_return_type:
                    return remaining_operand_return_type
    elif select_rule(follow_of_T1):
        return first_operand_type
    return False

def F() -> bool | str:
    if select_rule([THIS, IDENTIFIER]):
        this_check = P()
        if this_check:
            if(this_check == "this"):
                name = match_terminal(IDENTIFIER)
                if name:
                    if not current_class_data_table:
                        print("this must be used inside a class")
                        return False
                    data_type = F1(name, name, current_class_data_table, True)
                    if data_type:
                        return data_type
            else:
                name = match_terminal(IDENTIFIER) #a
                if name:
                    function_table_row = lookup_funtion_table(name, None)
                    if not function_table_row:
                        print(f"{name} is not defined")
                        return False
                    if not function_table_row.type.type:
                        data_type = F1(name, function_table_row.type, function_table, False)
                        return data_type

                    if function_table_row.type.type in primitive_data_types:
                        # if not current_class_data_table:
                        #     print("this must be used inside a class")
                        #     return False
                        # data_type = F1(name, function_table_row.type, current_class_data_table, False)
                        data_type = function_table_row.type.type
                        if data_type:
                            return data_type
                    else:
                        main_table_row = lookup_main_table(function_table_row.type.type)
                        if not main_table_row:
                            print(f"Type {function_table_row.type.type} is not defined")
                            return False
                        if main_table_row.link == None:
                            print("data table not found")
                            return False
                        data_type = F1(name, function_table_row.type, main_table_row.link, True)
                        if data_type:
                            return data_type
                    
    elif select_rule([INTEGER_CONSTANT, STRING_CONSTANT, FLOAT_CONSTANT, BOOL_CONSTANT]):
        constant_type = const()
        if constant_type:
            return constant_type
    elif select_rule([NOT]):
        operator = match_terminal(NOT)
        if operator:
            return_type = F()
            if return_type and type(return_type) == str:
                if not compatibility_for_single_operand(return_type, operator):
                    print("Type of operand must be a boolean")
                    return False
                return return_type
    return False

def P() -> bool | str:
    if select_rule([THIS]):
        name = match_terminal(THIS)
        if name:
            if match_terminal(DOT):
                return name
    elif select_rule([IDENTIFIER]):
        return True
    return False

    # Function type
    # {
    #     type: ,
    #     return_type: ,
    #     parameter_list: ,
    # }
    
    # Array Type
    # {
    #     type: ,
    #     array_dimension: ,
    # }
    
    # this.a().b.c[]
    # c.d.a()[]
    # c[].b().a

def F1(name:str, name_type: str | Function_Table_Row_Type | Data_Table_Row_Type | None, data_table: List[Data_Table_Row] | List[Function_Table_Row], is_object: bool) -> bool | str:
    if select_rule(follow_of_F1):
        if type(name_type) == str:
            if len(data_table) == 0:
                print(f"{name} is empty")
                return False
            if is_object and type(data_table[0]) == Data_Table_Row:
                data_table_row = lookup_attribute_data_table(name, data_table)
                if not data_table_row:
                    print(f"{name} does not exist")
                    return False
                if data_table_row:
                    if data_table_row.access_modifier == Data_Table_Access_Modifier.PRIVATE:
                        print(f"Can not Access {name}")
                        return False
                    name_type = data_table_row.type.type
            else:
                function_table_row = lookup_funtion_table(name, None)
                if not function_table_row:
                    print(f"{name} does not exist")
                    return False
                name_type = function_table_row.type.type
        if type(name_type) == Function_Table_Row_Type or type(name_type) == Data_Table_Row_Type:
            if name_type.array_dimensions < 0:
                print(f"{name} dimension not valid")
                return False
            if name_type.return_type:
                print(f"{name} is a function")
                return False
            if name_type.type:
                return name_type.type
        if type(name_type) == str:
            return name_type
    elif select_rule([OPENING_BRACKET]): # suppose type of array is stored like this int[][]
        if not name_type:
            data_table_row = None
            if len(data_table) == 0:
                print(f"{name} is empty")
                return False
            if is_object and type(data_table[0]) == Data_Table_Row:
                data_table_row = lookup_attribute_data_table(name, data_table)
            else:
                data_table_row = lookup_funtion_table(name, None)
            if data_table_row == None:
                print(f"{name} does not exist")
                return False
            name_type = data_table_row.type
        if match_terminal(OPENING_BRACKET):
            if not name_type.array_dimensions:
                print(f"{name} not an Array")
                return False
            # if !(name_type contains []):
                # print("Dimension Error")
            type_of_expression = OE()
            if type_of_expression:
                if type_of_expression != 'number':
                    print("index must be of type number.")
                    return False
                if match_terminal(CLOSING_BRACKET):
                    # if data_table_row.type is type list, case is missing
                    if not name_type.array_dimensions:
                        print(f"${name} is not of Array type or Dimension is incorrect")
                        return False
                    if name_type.type not in primitive_data_types:
                        # if data_table_row.type is an object list case
                        if not name_type.type:
                            print("type is undefined")
                            return False
                        main_table_row = lookup_main_table(name_type.type)
                        if not main_table_row:
                            print(f"{name_type.type} does not exist")
                            return False
                        if not main_table_row.link:
                            print(f"{main_table_row.name} class is empty")
                            return False
                        data_type = F1(main_table_row.name, return_new_type(name_type) ,main_table_row.link, True)
                        if data_type:
                            return data_type
                    data_type = F1(data_table_row.name, return_new_type(name_type) ,data_table, False)
                    if data_type:
                        return data_type
    elif select_rule([OPENING_PARENTHESIS]):
        if match_terminal(OPENING_PARENTHESIS):
            argument_list = AL()
            print(argument_list)
            if argument_list != None and type(argument_list) == list:
                if match_terminal(CLOSING_PARENTHESIS):
                    if type(name_type) != str:
                        if name_type.array_dimensions:
                            print('wrong Dimension')
                            return False
                    function_data_table_row = None
                    if len(data_table) == 0:
                        print(f"{name} does not exist")
                        return False
                    if is_object and type(data_table[0]) == Data_Table_Row:
                        function_data_table_row = lookup_function_data_table(name, argument_list, data_table)
                    else:
                        print(name, argument_list)
                        function_data_table_row = lookup_funtion_table(name, argument_list)
                    if not function_data_table_row:
                        print(f"{name} method does not exist")
                        return False
                    if not function_data_table_row.type.return_type:
                        print("not a function")
                        return False
                    return_type = F2(function_data_table_row.name, function_data_table_row.type, data_table)
                    if return_type and type(return_type) == str:
                        if return_type not in primitive_data_types:
                            main_table_row = lookup_main_table(return_type)
                            if not main_table_row:
                                print(f"{return_type} does not exist")
                                return False
                            return main_table_row.name
                        return return_type
    elif select_rule([DOT]):
        data_table_row = None
        if not name_type or type(name_type) == str:
            if len(data_table) == 0:
                print(f"{name} does not exist")
                return False
            if is_object and type(data_table[0]) == Data_Table_Row:
                data_table_row = lookup_attribute_data_table(name, data_table)
                if data_table_row and data_table_row.access_modifier == Data_Table_Access_Modifier.PRIVATE:
                    print(f"Can not Access {name}")
                    return False     
            else:
                data_table_row = lookup_funtion_table(name, None)
            if not data_table_row:
                print(f"{name} does not exist")
                return False
        if match_terminal(DOT):
            if type(name_type) == str:
                main_table_row = lookup_main_table(data_table_row.type.type)
                if not main_table_row:
                    print(f"can not access properties of {data_table_row.type.type}")
                    return False
                if not main_table_row.link:
                    print(f"{main_table_row.name} class is empty")
                    return False
                data_table = main_table_row.link
                name_type = main_table_row.name
            if type(name_type) != str:
                if name_type.array_dimensions:
                    print("wrong Dimension")
                    return False
                if name_type.type in primitive_data_types:
                    print("cannot access primitives data types")
                    return False
            Name = match_terminal(IDENTIFIER)
            if Name:
                if type(name_type) == str:
                    object_type = F1(Name, name_type, data_table, True)
                    if object_type:
                        return object_type
                if type(name_type) != str:
                    object_type = F1(Name, name_type.type, data_table, True)
                    if object_type:
                        return object_type
    elif select_rule([INCREMENT_DECREMENT]):
        operator = match_terminal(INCREMENT_DECREMENT)
        if operator:
            if not name_type:
                print("type undefined")
                return False
            if type(name_type) == Function_Table_Row_Type or type(name_type) == Data_Table_Row_Type:
                compatibility_type = None
                if name_type.return_type:
                    compatibility_type = compatibility_for_single_operand(name_type.return_type, operator)
                if name_type.type:
                    compatibility_type = compatibility_for_single_operand(name_type.type, operator)
                if not compatibility_type:
                    print(f"{name_type} is not compatible with {operator}")
                    return False
                return compatibility_type
            if type(name_type) == str:
                compatibility_type = compatibility_for_single_operand(name_type, operator)
                if not compatibility_type:
                    print(f"{name_type} is not compatible with {operator}")
                    return False
                return compatibility_type
    return False

def F2(name: str, name_type: Function_Table_Row_Type | Data_Table_Row_Type, data_table: List[Data_Table_Row] | List[Function_Table_Row]) -> bool | str:
    if select_rule([DOT]):
        if match_terminal(DOT):
            if name_type.return_type in primitive_data_types:
                print("cannot access primitives data types")
                return False 
            main_table_row = lookup_main_table(name_type.return_type)
            if not main_table_row:
                print(f"{name_type.return_type} does not exist")
                return False
            if not main_table_row.link:
                print(f"{main_table_row.name} class is empty")
                return False
            Name = match_terminal(IDENTIFIER)
            if Name:
                object_type = F1(Name, name_type.return_type, main_table_row.link, True)
                if object_type:
                    return object_type
    elif select_rule([OPENING_BRACKET]): # a()[]
        if not name_type.array_dimensions:
            print(f"{name} does not return an array")
            return False
        if match_terminal(OPENING_BRACKET):
            type_of_expression = OE()
            if not type_of_expression:
                print('index not given')
                return False
            if type_of_expression != 'number':
                print("index must be of type number.")
                return False
            if match_terminal(CLOSING_BRACKET):
                if not name_type.array_dimensions:
                    print(f"${name_type} is not of Array type")
                    return False
                if name_type.return_type not in primitive_data_types and name_type.return_type != 'void':
                    # if data_table_row.type is an object list case
                    if not name_type.return_type:
                        print("type undefined")
                        return False
                    main_table_row = lookup_main_table(name_type.return_type)
                    if not main_table_row:
                        print(f"{name_type.type} does not exist")
                        return False
                    if not main_table_row.link:
                        print("data table does not exist")
                        return False
                    data_type = F1(main_table_row.name, return_new_type(name_type) ,main_table_row.link, True)
                    if data_type:
                        return data_type
                data_type = F1(name, return_new_type(name_type) ,data_table, False)
                if data_type:
                    return data_type
    elif select_rule(follow_of_F2):
        if not name_type.return_type:
            print('return type not defined')
            return False
        return name_type.return_type
    return False

def AL() -> bool | List[str]:
    argument_list:List[str] = [] 
    if select_rule(first_of_OE):
        if arguement(argument_list):
            if next_arguement(argument_list):
                return argument_list
    elif select_rule([CLOSING_PARENTHESIS]):
        return argument_list
    return False

def const() -> bool | str:
    if select_rule([INTEGER_CONSTANT]):
        if match_terminal(INTEGER_CONSTANT):
            return 'number'
    elif select_rule([FLOAT_CONSTANT]):
        if match_terminal(FLOAT_CONSTANT):
            return 'number'
    elif select_rule([STRING_CONSTANT]):
        if match_terminal(STRING_CONSTANT):
            return 'string'
    elif select_rule([BOOL_CONSTANT]):
        if match_terminal(BOOL_CONSTANT):
            return 'boolean'
    return False

def arguement(argument_list: List[str]) -> bool:
    if select_rule(first_of_OE):
        type_of_expression = OE()
        print(type_of_expression)
        if type_of_expression:
            if type(type_of_expression.type) == str:
                argument_list.append(type_of_expression.type)
                return True
    return False

def next_arguement(argument_list: List[str]) -> bool:
    if select_rule([COMMA]):
        if match_terminal(COMMA):
            type_of_expression = OE()
            if type_of_expression and type(type_of_expression) == str:
                argument_list.append(type_of_expression)
                return True
    elif select_rule([CLOSING_PARENTHESIS]):
        return True
    return False

def return_new_type(old_typ: Function_Table_Row_Type | Data_Table_Row_Type) -> Function_Table_Row_Type | Data_Table_Row_Type:
    if old_typ.return_type:
        old_typ.type = old_typ.return_type
        old_typ.return_type = None
    if type(old_typ) == Function_Table_Row_Type:
        return Function_Table_Row_Type(old_typ.type, old_typ.parameter_list, old_typ.return_type, old_typ.array_dimensions - 1)
    if type(old_typ) == Data_Table_Row_Type:
        return Data_Table_Row_Type(old_typ.type, old_typ.parameter_list, old_typ.return_type, old_typ.array_dimensions - 1)

