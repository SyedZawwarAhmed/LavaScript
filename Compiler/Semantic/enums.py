from enum import Enum
 
class Main_Table_Type(Enum):
    CLASS = "CLASS"
    INTERFACE = "INTERFACE"

class Main_Table_Access_Modifier(Enum):
    GENERAL = "GENERAL"
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"

class Main_Table_Category(Enum):
    DEFAULT = "DEFAULT"
    SEALED = "SEALED"

class Data_Table_Access_Modifier(Enum):
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"

class Scope_Type(Enum):
    GLOBAL = "GLOBAL"
    IF = "IF"
    LOOP = "LOOP"
    CLASS = "CLASS"
    PROCEDURE = "PROCEDURE"
    INTERFACE = "INTERFACE"
    CONSTRUCTOR = "CONSTRUCTOR"

class Scope():
    def __init__(self, scope_number: int, scope_type: Scope_Type) -> None:
        self.Scope_Number = scope_number
        self.Scope_Type = scope_type