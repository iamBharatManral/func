from typing import Optional

from .tokn import Token, TokenType


class Lexer:
    def __init__(self, source: str):
        self._source = source
        self._char = None
        self._next_position = 0

    def next_token(self) -> Token:
        self._read_char()
        if self._char is None:
            return Token(self._next_position, TokenType.EOF, None, None)
        elif self._char.isdigit():
            return self._number_token()
        elif self._char == '"':
            return self._string_token()
        elif self._char == "+":
            return Token(self._next_position, TokenType.PLUS, "+", None)
        elif self._char == "-":
            return Token(self._next_position, TokenType.MINUS, "-", None)
        elif self._char == "*":
            return Token(self._next_position, TokenType.STAR, "*", None)
        elif self._char == "/":
            return Token(self._next_position, TokenType.SLASH, "/", None)
        elif self._char == "(":
            return Token(self._next_position, TokenType.LBRACE, "(", None)
        elif self._char == ")":
            return Token(self._next_position, TokenType.RBRACE, ")", None)
        elif self._char == "%":
            return Token(self._next_position, TokenType.MOD, "%", None)
        else:
            return Token(self._next_position, TokenType.ILLEGAL, None, None)

    def _read_char(self):
        if self._end_of_source():
            self._next_position += 1
            self._char = None
        else:
            self._char = self._source[self._next_position]
            self._next_position += 1

    def _end_of_source(self):
        return self._next_position >= len(self._source)

    def _peek_char(self) -> Optional[str]:
        if self._end_of_source():
            return None
        return self._source[self._next_position]

    def _number_token(self) -> Token:
        start = self._next_position
        lexeme = self._char
        peek_char = self._peek_char()
        while peek_char and (peek_char.isdigit() or peek_char == "."):
            self._read_char()
            lexeme += self._char
            peek_char = self._peek_char()
        if lexeme.find(".") == -1:
            number = int(lexeme)
            return Token(start, TokenType.INTEGER, lexeme, number)
        else:
            number = float(lexeme)
            return Token(start, TokenType.FLOAT, lexeme, number)

    def _string_token(self) -> Token:
        lexeme = self._char
        start = self._next_position
        peek_char = self._peek_char()
        while peek_char and peek_char != '"':
            self._read_char()
            lexeme += self._char
            peek_char = self._peek_char()
        self._read_char()
        lexeme += self._char
        return Token(start, TokenType.STRING, lexeme, lexeme[1 : len(lexeme) - 1])
