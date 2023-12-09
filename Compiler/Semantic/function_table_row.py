class Function_Table_Row_Type:
    def __init__(self, type: str | None = None, parameter_list = [], return_type = None, array_dimensions = 0):
        self.type = type
        self.parameter_list = parameter_list
        self.return_type = return_type
        self.array_dimensions = array_dimensions

class Function_Table_Row:
    def __init__(self, name: str, type: Function_Table_Row_Type, scope: int):
        self.name = name
        self.type = type        
        self.scope = scope