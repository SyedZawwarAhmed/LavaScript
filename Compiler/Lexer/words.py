from Lexer.constants import *

valid_words = {
    KEYWORDS: {
        DYNAMIC_STATIC: [
            "dynamic",
            "static",
        ],
        DATA_TYPES: [
            "string",
            "number",
            "boolean"
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
        EXIT_SKIP: [
            "exit",
            "skip"
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
        ]
    },

    OPERATORS: {
        ARITHMETIC: [
            "+",
            "-",
            "*",
            "/",
            "%",
        ],
        COMPARISON: [
            "==",
            "!=",
            "<",
            "<=",
            ">",
            ">=",
        ],
        LOGICAL: [
            "&&",
            "||",
            "!",
        ],
        ASSIGNMENT: [
            "=",
        ],
        COMPOUNT_ASSIGNMENT: [
            "+=",
            "-=",
            "*=",
            "/=",
            "%="
        ],
        INCREMENT_DECREMENT: [
            "++",
            "--",
        ],
        BITWISE: [
            "&",
            "|"
        ],
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
