import Parser.parser as parser
from Utils.get_name import get_name

def match_terminal(terminal: str):
    from tokenset import tokens
    if tokens[parser.i].token_type == terminal:
        name = get_name()
        parser.i += 1
        return name
    else:
        return False