from typing import List
from app.lox import Lox
from app.scanner.token import Token
from app.scanner.token_map import CONDITION_EQUAL_MAP, TOKEN_MAP, TokenType
from decimal import Decimal


class Scanner:
    def __init__(self, source: str, lox: Lox) -> None:
        self.source: str = source
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
        c = self.advance()
        if token_type := TOKEN_MAP.get(c):
            if token_type in CONDITION_EQUAL_MAP.keys():
                token_type = (
                    CONDITION_EQUAL_MAP[token_type]
                    if self.is_match("=")
                    else token_type
                )
            elif token_type == TokenType.SLASH:
                if self.is_match("/"):
                    while self.peek() != "\n" and not self.is_end_of_content():
                        self.advance()
                    return
            elif token_type in [
                TokenType.WHITE_SPACE,
                TokenType.TABSPACE,
                TokenType.CARRIAGE_RETURN,
            ]:
                return
            elif token_type == TokenType.NEW_LINE:
                self.line += 1
                return
            elif token_type == TokenType.STRING:
                self.string()
                return
            self.add_token(token_type)
        elif c.isdigit():
            self.number()
        else:
            self.lox.error(self.line, f"Unexpected character: {c}")

    def add_token(self, token_type, literal=None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))

    def is_match(self, expected):
        if self.is_end_of_content():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        return True

    def peek(self) -> str:
        if self.is_end_of_content():
            return "\0"
        return self.source[self.current]

    def peek_next(self) -> str:
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def string(self) -> None:
        while self.peek() != '"' and not self.is_end_of_content():
            if self.peek() == "\n":
                self.line += 1
            self.advance()
        if self.is_end_of_content():
            self.lox.error(self.line, "Unterminated string.")
            return
        self.advance()
        value = self.source[self.start + 1 : self.current - 1]
        self.add_token(TokenType.STRING, value)

    def number(self) -> None:
        while self.peek().isdigit():
            self.advance()
        if self.peek() == "." and self.peek_next().isdigit():
            self.advance()
            while self.peek().isdigit():
                self.advance()
        value = self.source[self.start : self.current]
        self.add_token(TokenType.NUMBER, float(value))
