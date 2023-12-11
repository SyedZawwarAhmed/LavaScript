import Parser.parser as parser

def get_name() -> str:
    from tokenset import tokens
    return tokens[parser.i].lexeme