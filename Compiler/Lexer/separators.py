# lexer/separators.py

# White-space separators
WHITESPACE = [
    ' ',   # Space
    '\t',  # Tab
    '\n',  # Newline (line feed)
    '\r',  # Carriage return
]

# Punctuation separators
PUNCTUATION = [
    ',',   # Comma
    ';',   # Semicolon
    '(',   # Left parenthesis
    ')',   # Right parenthesis
    '{',   # Left curly brace
    '}',   # Right curly brace
    '[',   # Left square bracket
    ']',   # Right square bracket
    ':',   # Colon
    '.',   # Period
]

# Quote separators
QUOTES = [
    '\'',  # Single quote
    '\"',  # Double quote
]

# Other separators
OTHER = [
    '/',   # Forward slash
    '\\',  # Backward slash
    '#',   # Hash (used for comments in some languages)
    '|',   # Pipe
    '&',   # Ampersand
    '!',   # Exclamation mark
    '%',   # Percent sign
    '<',   # Less than sign
    '>',   # Greater than sign
    '=',   # Equal sign
]

# Operators
OPERATORS = [
    '+',   # Plus sign
    '-',   # Minus sign
    '*',   # Asterisk
    '/',   # Forward slash
    '%',   # Percent sign
    '<',   # Less than sign
    '>',   # Greater than sign
    '=',   # Equal sign
    '==',  # Equal to operator
    '!=',  # Not equal to operator
    '<=',  # Less than or equal to operator
    '>=',  # Greater than or equal to operator
    '&&',  # Logical AND operator
    '||',  # Logical OR operator
]

separators = WHITESPACE + PUNCTUATION + QUOTES + OTHER

def check_is_separator(char):
    if char == '"':
        return False
    return char in separators
