from Utils.io import read_file
from Lexer.lexer import getWords, get_tokens

if __name__ == "__main__":
    file = read_file("source.lava")
    print(file)
    words = getWords(file)
    print(words)
    tokens = get_tokens(words)
    print([vars(token) for token in tokens])