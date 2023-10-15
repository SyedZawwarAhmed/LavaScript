from Utils.io import read_file
from Lexer.lexer import getWords, get_tokens
from Lexer.token import Token
from Parser.parser import check_is_syntax_valid
from typing import List

if __name__ == "__main__":
    file = read_file("source.lava")
    print(file)
    words = getWords(file)
    print(words)
    tokens: List[Token] = get_tokens(words)
    for token in tokens:
        print(token)

    is_syntax_valid = check_is_syntax_valid()
    print(f'\n================================\n{is_syntax_valid}')
