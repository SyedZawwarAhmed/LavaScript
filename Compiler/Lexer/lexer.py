from Lexer.separators import check_is_separator

def tokenize(source_code):
    tokens = []
    current_token = ''
    for char in source_code:
        if check_is_separator(char):
            if current_token:
                tokens.append(current_token)
                current_token = ''
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)
    return tokens
