from Semantic.enums import *
from Semantic.data_table_row import Data_Table_Row
from typing import List

class Main_Table_Row:
    def __init__(self, name: str, type: Main_Table_Type, access_modifier: Main_Table_Access_Modifier, category: Main_Table_Category, parent: List[str], link: List[Data_Table_Row]):
        self.name = name
        self.type = type        
        self.access_modifier = access_modifier
        self.category = category
        self.parent = parent
        self.link = link        