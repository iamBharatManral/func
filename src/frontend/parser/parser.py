from typing import Optional

from .ast import Program, Statement, StringLiteral, IntLiteral, FloatLiteral, Expression, BinaryExpression
from ..lexer.lexer import Lexer
from ..lexer.tokn import TokenType, Token


class Parser:
    def __init__(self, lexer: Lexer):
        self._lexer = lexer
        self._current_token = self._lexer.next_token()
        self.errors = []

    def _advance_token(self):
        self._current_token = self._lexer.next_token()

    def parse(self) -> Program:
        pg = Program([])
        while self._current_token.token_type != TokenType.EOF:
            statement = self._parse_statement()
            pg.statements.append(statement)
            self._advance_token()
        return pg

    def _parse_statement(self) -> Statement:
        return self._parse_expression(0)

    def _parse_expression(self, infix_precedence: int) -> Optional[Expression]:
        token = self._current_token
        self._advance_token()
        left = self._prefix(token)
        while infix_precedence < self._get_precedence(self._current_token):
            token = self._current_token
            self._advance_token()
            left = self._infix(token, left)
        return left

    def _prefix(self, token: Token) -> Expression:
        if token.token_type == TokenType.INTEGER:
            return IntLiteral(token.value)
        elif token.token_type == TokenType.FLOAT:
            return FloatLiteral(token.value)
        elif token.token_type == TokenType.MINUS:
            exp = self._parse_expression(100)
            if exp and str(exp.value).find(".") != -1:
                return FloatLiteral(exp.value * -1)
            else:
                return IntLiteral(exp.value * -1)
        elif token.token_type == TokenType.PLUS:
            exp = self._parse_expression(100)
            return IntLiteral(exp.value)
        elif token.token_type == TokenType.LPAREN:
            expr = self._parse_expression(0)
            self._advance_token()
            return expr
        elif token.token_type == TokenType.STRING:
            return StringLiteral(token.value)

    def _infix(self, token: Token, left: Expression) -> Expression:
        token_type = token.token_type
        if token_type == TokenType.PLUS:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "+")
        elif token_type == TokenType.MINUS:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "-")
        elif token_type == TokenType.STAR:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "*")
        elif token_type == TokenType.SLASH:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "/")
        elif token_type == TokenType.MOD:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "%")

    def _get_precedence(self, token) -> int:
        token_type = token.token_type
        if token_type == TokenType.PLUS or token_type == TokenType.MINUS:
            return 10
        if token_type == TokenType.STAR or token_type == TokenType.SLASH or token_type == TokenType.MOD:
            return 20
        return 0

