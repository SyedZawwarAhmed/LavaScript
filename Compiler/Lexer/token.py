class Token:
    def __init__(self, token_type, lexeme, line):
        self.token_type = token_type
        self.lexeme = lexeme
        self.line = line

    def __str__(self):
        return f"Token({self.token_type}, {self.lexeme}, Line: {self.line})"