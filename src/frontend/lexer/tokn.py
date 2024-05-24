from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional


class TokenType(Enum):
    INTEGER = 1
    FLOAT = 2
    STRING = 3
    ILLEGAL = 4
    EOF = 5


@dataclass
class Token:
    start: int
    token_type: TokenType
    lexeme: Optional[str]
    value: Optional[Any]
