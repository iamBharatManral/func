from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional


class TokenType(Enum):
    INTEGER = 1
    FLOAT = 2
    STRING = 3

    PLUS = 4
    MINUS = 5
    STAR = 6
    SLASH = 7
    MOD = 8

    LBRACE = 9
    RBRACE = 10

    ILLEGAL = 11
    EOF = 12


@dataclass
class Token:
    start: int
    token_type: TokenType
    lexeme: Optional[str]
    value: Optional[Any]
