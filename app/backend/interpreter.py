from ..frontend.parser.ast import *


class Interpreter:
    def __init__(self):
        self._output = []

    def eval(self, program: Program) -> []:
        for stmt in program.statements:
            if isinstance(stmt, Expression):
                self._output.append(self.eval_expression(stmt))
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
