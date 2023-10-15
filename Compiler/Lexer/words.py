from Lexer.constants import *

valid_words = {
    KEYWORDS: {
        DYNAMIC: [
            "dynamic"
        ],
        STATIC:[
            "static"
        ],
        NUMBER:[
            'number'
        ],
        STRING : [
            'string'
        ],
        BOOLEAN: [
            'boolean'
        ],
        LOG: [
            "log"
        ],
        IF: [
            "if"
        ],
        ELSE: [
            "else"
        ],
        UNTIL: [
            "until"
        ],
        EXIT:[
            'exit'
        ],
        SKIP:[
            'skip'
        ],
        PROC: [
            "proc"
        ],
        RETURN: [
            "return"
        ],
        CLASS: [
            "class"
        ],
        CONSTRUCTOR: [
            "constructor"
        ],
        THIS: [
            "this"
        ],
        METHOD: [
            "method"
        ],
        INIT: [
            "init"
        ],
        EXTENDS: [
            "extends"
        ],
        SUPER: [
            "super"
        ],
        SEALED: [
            "sealed"
        ],
        INTERFACE: [
            "interface"
        ],
        ASS: [
            "ass:"
        ]
    },

    OPERATORS: {
        ADD: [
            '+'
        ],
        SUBTRACT:[
            '-'
        ],
        DIVIDE: [
            '/'
        ],
        MULTIPLY: [
            "*"
        ],
        MOD: [
            "%"
        ],
        POWER: [
            '^'
        ],
        EQUAL_TO: [
            "=="
        ],
        LESS_THAN: [
            "<"
        ],
        GREATER_THAN: [
            ">"
        ],
        LESS_THAN_EQUAL: [
            "<="
        ],
        GREATER_THAN_EQUAL: [
            ">="
        ],
        NOT_EQUAL_TO: [
            "!="
        ],
        AND: [
            "&&"
        ],
        OR: [
            "||"
        ],
        NOT: [
            "!"
        ],
        ASSIGNMENT: [
            "=",
        ],
        ADD_EQUAL: [
            "+="
        ],
        SUBTRACT_EQUAL: [
            "-="
        ],
        MULTIPLY_EQUAL: [
            "*="
        ],
        DIVIDE_EQUAL: [
            "\="
        ],
        MOD_EQUAL: [
            "%="
        ],
        INCREMENT: [
            "++"
        ],
        DECREMENT: [
            "--"
        ],
        BITWISE_AND: [
            "&"
        ],
        BITWISE_OR: [
            "|"
        ]
    },

    PUNCTUATORS: {
        OPENING_PARENTHESIS: [
            "(",
        ],
        CLOSING_PARENTHESIS: [
            ")",
        ],
        OPENING_BRACKET: [
            "[",
        ],
        CLOSING_BRACKET: [
            "]",
        ],
        OPENING_BRACE: [
            "{",
        ],
        CLOSING_BRACE: [
            "}",
        ],
        SEMICOLON: [
            ";",
        ],
        COMMA: [
            ",",
        ],
        DOT: [
            ".",
        ],
        COLON: [
            ":",
        ],
    }
}
