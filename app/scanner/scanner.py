from typing import List
from app.scanner.token import Token
from app.scanner.token_map import TOKEN_MAP, TokenType


class Scanner:
    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens: List[Token] = []
        self.start: int = 0
        self.current: int = 0

    def is_end_of_content(self) -> bool:
        return self.current >= len(self.source)

    def tokenize(self) -> List[Token]:
        while not self.is_end_of_content():
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token(TokenType.EOF, "", None))
        return self.tokens

    def advance(self) -> str:
        c: str = self.source[self.current]
        self.current += 1
        return c

    def scan_token(self) -> None:
        c = self.advance()
        token_type = TOKEN_MAP[c]
        text = self.source[self.start : self.current]
        self.tokens.append(Token(token_type, text, None))
