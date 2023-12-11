from Semantic.enums import *
from typing import List

class Data_Table_Row_Type:
    def __init__(self, type = None, parameter_list: List[str] | None = None, return_type = None, array_dimensions = 0):
        self.type = type
        self.parameter_list = parameter_list
        self.return_type = return_type
        self.array_dimensions = array_dimensions

class Data_Table_Row:
    def __init__(self, name: str, type: Data_Table_Row_Type, access_modifier: Data_Table_Access_Modifier, type_modifier):
        self.name = name
        self.type = type        
        self.access_modifier = access_modifier
        self.type_modifier = type_modifier