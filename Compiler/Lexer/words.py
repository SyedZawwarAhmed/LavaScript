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
            "boolean",
        ],
        VOID: [
          "void",
        ],
        ASSIGN: [
            "assign"
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
        HASH: [
          "#"
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
        IMPLEMENTS: [
            "implements"
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
        BOOL_CONSTANT: [
            "true",
            "false"
        ]
    },

    OPERATORS: {
        PLUS_MINUS: [
            "+",
            "-",
        ],
        MULTIPLY_DIVIDE_MODULUS: [
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
        AND: [
            "&&",
        ],
        OR: [
            "||",
        ],
        NOT: [
            "!",
        ],
        ASSIGNMENT_OPERATOR: [
            "=",
        ],
        COMPOUND_ASSIGNMENT_OPERATOR: [
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
