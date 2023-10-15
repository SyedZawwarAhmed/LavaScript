from Lexer.constants import *

breakers = {
    ONLY_BREAKERS: [
        ' ',   # Space
        '\t',  # Tab
        '\r',  # Carriage return
        '?',   # Forward slash
        '@'
    ],
    NEW_LINE: [
        '\n'
    ],
    # DOT: [
    #     '.',   # Period
    # ],
    PUNCTUATORS: [
        ';',   # Semicolon
        ',',   # Comma
        ';',   # Semicolon
        ',',   # Comma
        '(',   # Left parenthesis
        ')',   # Right parenthesis
        '{',   # Left curly brace
        '}',   # Right curly brace
        '[',   # Left square bracket
        ']',   # Right square bracket
        ':',   # Colon
    ],
    QUOTES: [
        # '\'',  # Single quote
        '"',  # Double quote
    ],
    # SLASHES: [
    #     '\\',  # Backward slash
    # ],
    OPERATORS: [
        '+',   # Plus sign
        '-',   # Minus sign
        '*',   # Asterisk
        '/',   # Forward slash
        '%',   # Percent sign
        '<',   # Less than sign
        '>',   # Greater than sign
        '=',   # Equal sign
        '!',   # Exclamation mark
        '&',   # Ampersand
        '|',   # Pipe
    ],
    DOUBLE_CHAR_OPERATORS: [
        '==',  # Equal to operator
        '!=',  # Not equal to operator
        '<=',  # Less than or equal to operator
        '>=',  # Greater than or equal to operator
        '&&',  # Logical AND operator
        '||',  # Logical OR operator
        '+=',
        '-=',
        '*=',
        '/=',
        '%=',
        '++',
        '--'
    ],
}
