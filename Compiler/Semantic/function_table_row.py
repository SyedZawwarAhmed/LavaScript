from typing import List
class Function_Table_Row_Type:
    def __init__(self, type = None, parameter_list: List[str] = [], return_type = None):
        self.type = type
        self.parameter_list = parameter_list
        self.return_type = return_type

class Function_Table_Row:
    def __init__(self, name: str, type: Function_Table_Row_Type, scope: int):
        self.name = name
        self.type = type        
        self.scope = scope