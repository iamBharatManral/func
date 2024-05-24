from abc import ABC
from dataclasses import dataclass


class Node(ABC):
    pass


class Statement(Node):
    pass


class Expression(Statement):
    pass


@dataclass
class Program:
    statements: [Node]


@dataclass
class IntLiteral(Expression):
    value: int


@dataclass
class FloatLiteral(Expression):
    value: float


@dataclass
class StringLiteral(Expression):
    value: str


@dataclass
class BinaryExpression(Expression):
    left: Statement
    right: Statement
    operator: str
