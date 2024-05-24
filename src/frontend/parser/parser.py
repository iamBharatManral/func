from typing import Optional

from .ast import Program, Statement, IntLiteral, StringLiteral, FloatLiteral, Expression
from ..lexer.lexer import Lexer
from ..lexer.tokn import TokenType


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
        return self._parse_expression()

    def _parse_expression(self) -> Optional[Expression]:
        if self._current_token.token_type == TokenType.INTEGER:
            return IntLiteral(self._current_token.value)
        elif self._current_token.token_type == TokenType.FLOAT:
            return FloatLiteral(self._current_token.value)
        elif self._current_token.token_type == TokenType.STRING:
            return StringLiteral(self._current_token.value)
        else:
            self.errors.append("error: illegal expression")
            return None

