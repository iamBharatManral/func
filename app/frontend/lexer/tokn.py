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

    LT = 9
    GT = 10
    LE = 11
    GE = 12
    EQ = 13
    NE = 14

    NOT = 15
    AND = 16
    OR = 17

    BAND = 18
    BOR = 19

    ASSIGN = 20

    LPAREN = 21
    RPAREN = 22

    IDENTIFIER = 23

    ILLEGAL = 24
    EOF = 25


@dataclass
class Token:
    start: int
    token_type: TokenType
    lexeme: Optional[str]
    value: Optional[Any]
