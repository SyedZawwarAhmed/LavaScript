from Utils.io import read_file
from Lexer.lexer import getWords, get_tokens
from Parser.parser import check_is_syntax_valid

if __name__ == "__main__":
    file = read_file("source.lava")
    print(file)
    words = getWords(file)
    print(words)
    tokens: list = get_tokens(words)
    for token in tokens:
        print(token)

    is_syntax_valid = check_is_syntax_valid(tokens)
    print(f'\n================================\n{is_syntax_valid}')
