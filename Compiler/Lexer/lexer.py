import re

from Lexer.breakers import breakers
from Lexer.constants import *
from Lexer.words import *
from Lexer.token import * 

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

def check_is_sign(char: str, last_word) -> bool:
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
    words = []
    current_word = ''
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
                if current_word:
                    words.append(current_word)
                    current_word = ''
                if is_breaker[BREAKER_TYPE] != ONLY_BREAKERS:
                    if is_breaker[BREAKER_TYPE] != QUOTES and is_breaker[BREAKER_TYPE] != OPERATORS and is_breaker[BREAKER_TYPE] != DOT:
                        words.append(is_breaker[VALUE])
                    if is_breaker[BREAKER_TYPE] == DOUBLE_CHAR_OPERATORS:
                        i += 1
                    elif is_breaker[BREAKER_TYPE] == QUOTES:
                        is_string_constant = True
                        current_word += char
                    elif is_breaker[BREAKER_TYPE] == OPERATORS:
                        if (is_breaker[VALUE] == '+' or is_breaker[VALUE] == '-') and current_word == '':
                            if len(words) > 0:
                                if check_is_operator(words[-1]) or words[-1] == ';':
                                    is_number_constant = True
                                    current_word += char
                                else:
                                    words.append(is_breaker[VALUE])
                            else:
                                current_word += char 
                        else:
                                words.append(is_breaker[VALUE])
                else:
                    if is_breaker[VALUE] == '/':
                        if next_char == '/':
                            is_single_line_comment = True
                        elif next_char == '*':
                            is_multi_line_comment = True
                        else:
                            current_word += char
                        
            elif check_is_dot(char):
                if check_is_integer(current_word):
                    current_word += char
                else:
                    if current_word:
                        words.append(current_word)
                        current_word = char
                        words.append(char)
                        current_word = ''
                    else:
                        if check_is_number(next_char):
                            current_word += char
                        else:
                            words.append(char)
                            current_word = ''
            else:
                current_word += char
        elif is_string_constant:
            if check_is_quote(char):
                current_word += char
                is_string_constant = False
                words.append(current_word)
                current_word = ''
            elif check_is_backslash(char):
                if next_char == 'n':
                    current_word += '\n'
                elif next_char == 't':
                    current_word += '\t'
                elif next_char == 'r':
                    current_word == '\r'
                else:
                    current_word += next_char
                i += 1
            else:
                current_word += char

        elif is_single_line_comment:
            if char == '\n':
                is_single_line_comment = False
                words.append(char)
        elif is_multi_line_comment:
            if next_char and char == '*' and next_char == '/':
                is_multi_line_comment = False
                i += 1

        i += 1
    if current_word != '':
        words.append(current_word)
    return words

def find_word(input_string, keyword_dict):
    for keyword_category, keywords_list in keyword_dict.items():
        if input_string.lower() in keywords_list:
            return keyword_category
    return None


def get_tokens(words):
    tokens = []
    i = 0
    line_number = 1
    while i < len(words):
        # print(find_word(words[i], keywords))
        word = words[i]
        is_keyword = find_word(word, keywords)
        new_token = None
        if word == '\n':
            line_number += 1
        if is_keyword:
            new_token = Token(is_keyword, word, line_number)
        tokens.append(new_token)
        i += 1

    return tokens
