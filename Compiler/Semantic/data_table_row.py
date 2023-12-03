class Data_Table_Row_Type:
    def __init__(self, type = None, parameter_list = None, return_type = None):
        self.type = type
        self.parameter_list = parameter_list
        self.return_type = return_type

class Data_Table_Row:
    def __init__(self, name, type: Data_Table_Row_Type, access_modifier, type_modifier):
        self.name = name
        self.type = type        
        self.access_modifier = access_modifier
        self.type_modifier = type_modifier