from typing import List
from Semantic.main_table_row import Main_Table_Row
from Semantic.function_table_row import Function_Table_Row

main_table: List[Main_Table_Row] = []
function_table: List[Function_Table_Row] = []
current_scope = 0
scope_stack = [0]