from app.scanner.token_map import TokenType


class Token:
    def __init__(self, token_type, lexeme, literal):
        self.token_type: TokenType = token_type
        self.lexeme = lexeme
        self.literal = literal

    def __str__(self):
        if not self.literal:
            return f"{self.token_type.name} {self.lexeme} null"
        return f"{self.token_type.name} {self.lexeme} {self.literal}"
