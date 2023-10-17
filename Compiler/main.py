from Utils.io import read_file
from Lexer.lexer import getWords, get_tokens
from Lexer.token import Token
from typing import List
  
from Parser.parser import check_is_syntax_valid
file = read_file("source.lava")
print(file)
words = getWords(file)
print(words)
tokens = get_tokens(words)
for token in tokens:
    print(token)

is_syntax_valid = check_is_syntax_valid(tokens)
print(f'\n================================\n{is_syntax_valid}')
