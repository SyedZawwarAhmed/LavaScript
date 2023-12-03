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