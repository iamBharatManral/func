from app.environment.environment import SymbolTable
from ..frontend.parser.ast import *


class Interpreter:
    def __init__(self, symtable: SymbolTable):
        self._output = []
        self.symtable = symtable

    def eval(self, program: Program) -> []:
        for stmt in program.statements:
            if isinstance(stmt, Expression):
                self._output.append(self.eval_expression(stmt))
            if isinstance(stmt, Statement):
                self._output.append(self.eval_statement(stmt))
        return self._output

    def eval_expression(self, stmt: Statement):
        if (
            isinstance(stmt, IntLiteral)
            or isinstance(stmt, FloatLiteral)
            or isinstance(stmt, StringLiteral)
        ):
            return stmt.value
        if isinstance(stmt, BinaryExpression):
            if stmt.operator == "+":
                return self.eval_expression(stmt.left) + self.eval_expression(
                    stmt.right
                )
            if stmt.operator == "-":
                return self.eval_expression(stmt.left) - self.eval_expression(
                    stmt.right
                )
            if stmt.operator == "*":
                return self.eval_expression(stmt.left) * self.eval_expression(
                    stmt.right
                )
            if stmt.operator == "/":
                return int(
                    self.eval_expression(stmt.left) / self.eval_expression(stmt.right)
                )
            if stmt.operator == "%":
                return self.eval_expression(stmt.left) % self.eval_expression(
                    stmt.right
                )
            if stmt.operator == "<":
                return self.eval_expression(stmt.left) < self.eval_expression(
                    stmt.right
                )
            if stmt.operator == "<=":
                return self.eval_expression(stmt.left) <= self.eval_expression(
                    stmt.right
                )
            if stmt.operator == ">":
                return self.eval_expression(stmt.left) > self.eval_expression(
                    stmt.right
                )
            if stmt.operator == ">=":
                return self.eval_expression(stmt.left) >= self.eval_expression(
                    stmt.right
                )
            if stmt.operator == "!=":
                return self.eval_expression(stmt.left) != self.eval_expression(
                    stmt.right
                )
            if stmt.operator == "==":
                return self.eval_expression(stmt.left) == self.eval_expression(
                    stmt.right
                )
            if stmt.operator == "&&":
                return self.eval_expression(stmt.left) and self.eval_expression(
                    stmt.right
                )
            if stmt.operator == "||":
                return self.eval_expression(stmt.left) or self.eval_expression(
                    stmt.right
                )
            if stmt.operator == "&":
                return self.eval_expression(stmt.left) & self.eval_expression(
                    stmt.right
                )
            if stmt.operator == "|":
                return self.eval_expression(stmt.left) | self.eval_expression(
                    stmt.right
                )
        if isinstance(stmt, Identifier):
            return self.symtable.lookup(stmt.name, 0).value

    def eval_statement(self, stmt: Statement):
        if isinstance(stmt, NameBinding):
            self.symtable.update(stmt.left.name, 0, self.eval_expression(stmt.right))
