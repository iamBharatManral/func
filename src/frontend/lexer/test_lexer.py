import unittest

from .lexer import Lexer, TokenType, Token


class TestLexer(unittest.TestCase):

    def test_illegal_token(self):
        lexer = Lexer("&")
        expected = [
            Token(1, TokenType.ILLEGAL, None, None),
            Token(2, TokenType.EOF, None, None),
        ]
        got = []
        token = lexer.next_token()
        while token.token_type != TokenType.EOF:
            got.append(token)
            token = lexer.next_token()
        got.append(token)
        self.assertEqual(expected, got)

    def test_int_literal(self):
        lexer = Lexer("123")
        expected = [
            Token(1, TokenType.INTEGER, "123", 123),
            Token(4, TokenType.EOF, None, None),
        ]
        got = []
        token = lexer.next_token()
        while token.token_type != TokenType.EOF:
            got.append(token)
            token = lexer.next_token()
        got.append(token)
        self.assertEqual(expected, got)

    def test_float_literal(self):
        lexer = Lexer("123.345")
        expected = [
            Token(1, TokenType.FLOAT, "123.345", 123.345),
            Token(8, TokenType.EOF, None, None),
        ]
        got = []
        token = lexer.next_token()
        while token.token_type != TokenType.EOF:
            got.append(token)
            token = lexer.next_token()
        got.append(token)
        self.assertEqual(expected, got)

    def test_string_literal(self):
        lexer = Lexer('"hello"')
        expected = [
            Token(1, TokenType.STRING, '"hello"', "hello"),
            Token(8, TokenType.EOF, None, None),
        ]
        got = []
        token = lexer.next_token()
        while token.token_type != TokenType.EOF:
            got.append(token)
            token = lexer.next_token()
        got.append(token)
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
