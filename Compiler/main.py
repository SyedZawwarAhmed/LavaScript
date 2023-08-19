from Utils.io import read_file
from Lexer.lexer import getWords

if __name__ == "__main__":
    file = read_file("source.lava")
    print(file)
    words = getWords(file)
    print(words)