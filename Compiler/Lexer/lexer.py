from Lexer.breakers import breakers
from Lexer.constants import *

def check_is_breaker(char, next_char):
    result = {
        IS_BREAKER: False,
        BREAKER_TYPE: None,
        VALUE: None 
    }
    for breaker in list(breakers.keys()):
        breaker_list = breakers[breaker]
        if char in breaker_list:
            result[IS_BREAKER] = True
            result[BREAKER_TYPE] = breaker
            result[VALUE] = char
            if breaker == OPERATORS and next_char:
                double_char_operator = char + next_char
                print(double_char_operator)
                if double_char_operator in breakers[DOUBLE_CHAR_OPERATORS]:
                    result[BREAKER_TYPE] = DOUBLE_CHAR_OPERATORS
                    result[VALUE] = double_char_operator
            break
    return result

def check_is_quote(char: str):
    if char in breakers[QUOTES]:
        return True
    return False

def getWords(source_code: str):
    tokens = []
    current_token = ''
    i = 0
    is_constant = False
    while i < len(source_code):
        char = source_code[i]
        print(char)
        next_char = source_code[i + 1] if i < len(source_code) - 1 else None
        is_breaker = check_is_breaker(char, next_char)
        if not is_constant: 
            if is_breaker[IS_BREAKER]:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                if is_breaker[BREAKER_TYPE] != ONLY_BREAKERS:
                    if  is_breaker[BREAKER_TYPE] != QUOTES:
                        tokens.append(is_breaker[VALUE])
                    if is_breaker[BREAKER_TYPE] == DOUBLE_CHAR_OPERATORS:
                        i += 1
                    elif is_breaker[BREAKER_TYPE] == QUOTES:
                        is_constant = not is_constant
                        current_token += char
            else:
                current_token += char
        else:
            current_token += char
            is_constant = not is_constant if check_is_quote(char) else is_constant

        i += 1
    if current_token:
        tokens.append(current_token)
    return tokens
