from enum import Enum, auto
from typing import Dict


class TokenType(Enum):
    # Single-character tokens.
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    EOF = auto()
    COMMA = auto()
    DOT = auto()
    MINUS = auto()
    PLUS = auto()
    SEMICOLON = auto()
    SLASH = auto()
    STAR = auto()

    # Operators
    EQUAL = auto()
    EQUAL_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    BANG = auto()
    BANG_EQUAL = auto()

    # WHITESPACE
    WHITE_SPACE = auto()
    TABSPACE = auto()
    CARRIAGE_RETURN = auto()
    NEW_LINE = auto()

    # Strings
    STRING = auto()

    # Number
    NUMBER = auto()
    IDENTIFIER = auto()

    # KEYWORDS
    AND = auto()
    CLASS = auto()
    ELSE = auto()
    FALSE = auto()
    FOR = auto()
    FUN = auto()
    IF = auto()
    NIL = auto()
    OR = auto()
    PRINT = auto()
    RETURN = auto()
    SUPER = auto()
    THIS = auto()
    TRUE = auto()
    VAR = auto()
    WHILE = auto()


TOKEN_MAP: Dict[str, TokenType] = {
    # Single Char Tokens
    "(": TokenType.LEFT_PAREN,
    ")": TokenType.RIGHT_PAREN,
    "{": TokenType.LEFT_BRACE,
    "}": TokenType.RIGHT_BRACE,
    ",": TokenType.COMMA,
    ".": TokenType.DOT,
    "-": TokenType.MINUS,
    "+": TokenType.PLUS,
    ";": TokenType.SEMICOLON,
    "/": TokenType.SLASH,
    "*": TokenType.STAR,
    "=": TokenType.EQUAL,
    "==": TokenType.EQUAL_EQUAL,
    "<": TokenType.LESS,
    "<=": TokenType.LESS_EQUAL,
    ">": TokenType.GREATER,
    ">=": TokenType.GREATER_EQUAL,
    "!": TokenType.BANG,
    "!=": TokenType.BANG_EQUAL,
    " ": TokenType.WHITE_SPACE,
    "\t": TokenType.TABSPACE,
    "\r": TokenType.CARRIAGE_RETURN,
    "\n": TokenType.NEW_LINE,
    '"': TokenType.STRING,
}

CONDITION_EQUAL_MAP: Dict[TokenType, TokenType] = {
    TokenType.LESS: TokenType.LESS_EQUAL,
    TokenType.GREATER: TokenType.GREATER_EQUAL,
    TokenType.EQUAL: TokenType.EQUAL_EQUAL,
    TokenType.BANG: TokenType.BANG_EQUAL,
}

KEYWORDS_MAP: Dict[str, TokenType] = {
    "and": TokenType.AND,
    "class": TokenType.CLASS,
    "else": TokenType.ELSE,
    "false": TokenType.FALSE,
    "for": TokenType.FOR,
    "fun": TokenType.FUN,
    "if": TokenType.IF,
    "nil": TokenType.NIL,
    "or": TokenType.OR,
    "print": TokenType.PRINT,
    "return": TokenType.RETURN,
    "super": TokenType.SUPER,
    "this": TokenType.THIS,
    "true": TokenType.TRUE,
    "var": TokenType.VAR,
    "while": TokenType.WHILE,
}
