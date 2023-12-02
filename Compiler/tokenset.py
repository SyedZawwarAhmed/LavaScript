from Utils.io import read_file
from Lexer.lexer import getWords, get_tokens
  
file = read_file("../source.lava")
# print(file)
words = getWords(file)
# print(words)
tokens = get_tokens(words)
# for token in tokens:
#     print(token)

