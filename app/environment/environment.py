from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class Symbol:
    name: str
    scope: int
    value: Optional[Any]


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, name: str, scope: int = 0, value: Optional[Any] = None):
        self.symbols[name] = Symbol(name, scope, value)

    def update(self, name, scope, value):
        self.symbols[name] = Symbol(name, scope, value)

    def lookup(self, name: str, scope: int) -> Optional[Symbol]:
        return self.symbols.get(name, None)
