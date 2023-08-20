import re

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
                if double_char_operator in breakers[DOUBLE_CHAR_OPERATORS]:
                    result[BREAKER_TYPE] = DOUBLE_CHAR_OPERATORS
                    result[VALUE] = double_char_operator
            break
    return result

def check_is_quote(char: str) -> bool:
    return char in breakers[QUOTES]

def check_is_sign(char: str, last_token) -> bool:
    return

def check_is_operator(word: str) -> bool:
    return word in breakers[OPERATORS] or word in breakers[DOUBLE_CHAR_OPERATORS]

def check_is_number(char: str) -> bool:
    return char.isnumeric()

def check_is_integer(string) -> bool:
    return re.match(r'^[+-]?\d+$', string) is not None

def check_is_dot(char: str) -> bool:
    return char == '.'

def check_is_backslash(char: str) -> bool:
    return char == '\\'

def getWords(source_code: str):
    tokens = []
    current_token = ''
    i = 0
    is_string_constant = False
    is_single_line_comment = False
    is_multi_line_comment = False
    while i < len(source_code):
        char = source_code[i]
        next_char = source_code[i + 1] if i < len(source_code) - 1 else None
        is_breaker = check_is_breaker(char, next_char)
        if not is_string_constant and not is_single_line_comment and not is_multi_line_comment: 
            if is_breaker[IS_BREAKER]:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                if is_breaker[BREAKER_TYPE] != ONLY_BREAKERS:
                    if is_breaker[BREAKER_TYPE] != QUOTES and is_breaker[BREAKER_TYPE] != OPERATORS and is_breaker[BREAKER_TYPE] != DOT:
                        tokens.append(is_breaker[VALUE])
                    if is_breaker[BREAKER_TYPE] == DOUBLE_CHAR_OPERATORS:
                        i += 1
                    elif is_breaker[BREAKER_TYPE] == QUOTES:
                        is_string_constant = True
                        current_token += char
                    elif is_breaker[BREAKER_TYPE] == OPERATORS:
                        if (is_breaker[VALUE] == '+' or is_breaker[VALUE] == '-') and current_token == '':
                            if len(tokens) > 0:
                                if check_is_operator(tokens[-1]) or tokens[-1] == ';':
                                    is_number_constant = True
                                    current_token += char
                                else:
                                    tokens.append(is_breaker[VALUE])
                            else:
                                current_token += char 
                        else:
                                tokens.append(is_breaker[VALUE])
                else:
                    if is_breaker[VALUE] == '/':
                        if next_char == '/':
                            is_single_line_comment = True
                        elif next_char == '*':
                            is_multi_line_comment = True
                        else:
                            current_token += char
                        
            elif check_is_dot(char):
                if check_is_integer(current_token):
                    current_token += char
                else:
                    if current_token:
                        tokens.append(current_token)
                        current_token = char
                        tokens.append(char)
                        current_token = ''
                    else:
                        if check_is_number(next_char):
                            current_token += char
                        else:
                            tokens.append(char)
                            current_token = ''
            else:
                current_token += char
        elif is_string_constant:
            if check_is_quote(char):
                current_token += char
                is_string_constant = False
                tokens.append(current_token)
                current_token = ''
            elif check_is_backslash(char):
                if next_char == 'n':
                    current_token += '\n'
                elif next_char == 't':
                    current_token += '\t'
                elif next_char == 'r':
                    current_token == '\r'
                else:
                    current_token += next_char
                i += 1
            else:
                current_token += char

        elif is_single_line_comment:
            if char == '\n':
                is_single_line_comment = False
        elif is_multi_line_comment:
            if next_char and char == '*' and next_char == '/':
                is_multi_line_comment = False
                i += 1

        i += 1
    if current_token != '':
        tokens.append(current_token)
    return tokens
