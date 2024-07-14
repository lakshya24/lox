from typing import List
from app.lox import Lox
from app.scanner.token import Token
from app.scanner.token_map import TOKEN_MAP, TokenType


class Scanner:
    def __init__(self, source: str, lox: Lox) -> None:
        self.source = source
        self.tokens: List[Token] = []
        self.start: int = 0
        self.current: int = 0
        self.line = 1
        self.lox = lox

    def is_end_of_content(self) -> bool:
        return self.current >= len(self.source)

    def tokenize(self) -> List[Token]:
        while not self.is_end_of_content():
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def advance(self) -> str:
        c: str = self.source[self.current]
        self.current += 1
        return c

    def scan_token(self) -> None:
        c: str = self.advance()
        if token_type := TOKEN_MAP.get(c):
            text = self.source[self.start : self.current]
            self.tokens.append(Token(token_type, text, None, self.line))
        else:
            self.lox.error(self.line, f"Unexpected character: {c}")
