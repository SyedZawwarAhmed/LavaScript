from typing import List
class Function_Table_Row_Type:
    def __init__(self, type = None, parameter_list = [], return_type = None, array_dimension = 0):
        self.type = type
        self.parameter_list = parameter_list
        self.return_type = return_type
        self.array_dimension = array_dimension

class Function_Table_Row:
    def __init__(self, name: str, type: Function_Table_Row_Type, scope: int):
        self.name = name
        self.type = type        
        self.scope = scope