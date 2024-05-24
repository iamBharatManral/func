import unittest

from .ast import IntLiteral, FloatLiteral, StringLiteral
from .parser import Parser
from ..lexer.lexer import Lexer


class TestParser(unittest.TestCase):
    def test_parsing_integer(self):
        lexer = Lexer("123")
        parser = Parser(lexer)
        expected = IntLiteral(123)
        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_parsing_float(self):
        lexer = Lexer("123.455")
        parser = Parser(lexer)
        expected = FloatLiteral(123.455)
        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_parsing_string(self):
        lexer = Lexer("\"hello world\"")
        parser = Parser(lexer)
        expected = StringLiteral("hello world")
        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
