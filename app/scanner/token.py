from app.scanner.token_map import TokenType


class Token:
    def __init__(self, token_type, lexeme, literal, line):
        self.token_type: TokenType = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        if self.literal is None:
            return f"{self.token_type.name} {self.lexeme} null"
        return f"{self.token_type.name} {self.lexeme} {self.literal}"
