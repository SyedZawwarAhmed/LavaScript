from Lexer.constants import *

breakers = {
    ONLY_BREAKERS: [
        ' ',   # Space
        '\t',  # Tab
        '\n',  # Newline (line feed)
        '\r',  # Carriage return
    ],
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
        '.',   # Period
    ],
    QUOTES: [
        # '\'',  # Single quote
        '\"',  # Double quote
    ],
    OTHERS: [
        '/',   # Forward slash
        '\\',  # Backward slash
        '#',   # Hash (used for comments in some languages)
        '|',   # Pipe
        '&',   # Ampersand
    ],
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
    ],
    DOUBLE_CHAR_OPERATORS: [
        '==',  # Equal to operator
        '!=',  # Not equal to operator
        '<=',  # Less than or equal to operator
        '>=',  # Greater than or equal to operator
        '&&',  # Logical AND operator
        '||',  # Logical OR operator
        '++',
        '--'
    ],
}
