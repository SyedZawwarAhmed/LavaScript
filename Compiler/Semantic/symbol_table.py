from typing import List
from Semantic.main_table_row import Main_Table_Row
from Semantic.function_table_row import Function_Table_Row
from Semantic.data_table_row import Data_Table_Row
from Semantic.enums import *

main_table: List[Main_Table_Row] = []
function_table: List[Function_Table_Row] = []
current_scope = 0
scope_stack: List[Scope] = [Scope(0, Scope_Type.GLOBAL)]
current_class_data_table: List[Data_Table_Row] | None = None
