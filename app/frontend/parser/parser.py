from typing import Optional

from .ast import Program, Statement, StringLiteral, IntLiteral, FloatLiteral, Expression, BinaryExpression, NameBinding, \
    Identifier
from ..lexer.lexer import Lexer
from ..lexer.tokn import TokenType, Token


class Parser:
    def __init__(self, lexer: Lexer, symbol_table):
        self._lexer = lexer
        self._current_token = self._lexer.next_token()
        self.errors = []
        self._symbol_table = symbol_table

    def _advance_token(self):
        self._current_token = self._lexer.next_token()

    def _peek_token(self):
        return self._lexer.peek_token()

    def parse(self) -> Program:
        pg = Program([])
        while self._current_token.token_type != TokenType.EOF:
            statement = self._parse_statement()
            pg.statements.append(statement)
            self._advance_token()
        return pg

    def _parse_statement(self) -> Statement:
        if self._peek_token().token_type == TokenType.ASSIGN:
            return self._parse_name_binding()
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
        elif token.token_type == TokenType.IDENTIFIER:
            return Identifier(name=token.lexeme)

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
        elif token_type == TokenType.EQ:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "==")
        elif token_type == TokenType.NE:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "!=")
        elif token_type == TokenType.LT:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "<")
        elif token_type == TokenType.LE:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "<=")
        elif token_type == TokenType.GT:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), ">")
        elif token_type == TokenType.GE:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), ">=")
        elif token_type == TokenType.AND:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "&&")
        elif token_type == TokenType.OR:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "||")
        elif token_type == TokenType.BAND:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "&")
        elif token_type == TokenType.BOR:
            return BinaryExpression(left, self._parse_expression(self._get_precedence(token)), "|")

    def _get_precedence(self, token) -> int:
        token_type = token.token_type
        plus_minus = [TokenType.PLUS, TokenType.MINUS]
        star_slash = [TokenType.STAR, TokenType.SLASH, TokenType.MOD]
        relation_operators = [TokenType.EQ, TokenType.LE, TokenType.LT, TokenType.GT, TokenType.GE, TokenType.NE]
        if token_type in plus_minus:
            return 10
        if token_type in star_slash:
            return 20
        if token_type in relation_operators:
            return 5
        if token_type == TokenType.BAND:
            return 4
        if token_type == TokenType.BOR:
            return 3
        if token_type == TokenType.AND:
            return 2
        if token_type == TokenType.OR:
            return 1
        return 0

    def _parse_name_binding(self):
        left = self._current_token
        self._advance_token()
        self._advance_token()
        self._symbol_table.insert(name=left.lexeme)
        right = self._parse_expression(0)
        return NameBinding(Identifier(name=left.lexeme), right)
