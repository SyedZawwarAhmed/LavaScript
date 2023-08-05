from Utils.io import read_file
from Lexer.lexer import tokenize

if __name__ == "__main__":
    file = read_file("Compiler/source.lava")
    print(file)
    tokens = tokenize(file)
    print(tokens)