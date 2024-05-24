import unittest

from .ast import IntLiteral, FloatLiteral, StringLiteral, BinaryExpression
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

    def test_addition(self):
        lexer = Lexer("-1+2")
        parser = Parser(lexer)
        expected = BinaryExpression(left=IntLiteral(value=-1), right=IntLiteral(value=2), operator='+')
        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_multi_binary_expression(self):
        lexer = Lexer("1 + 2 * 3")
        parser = Parser(lexer)
        expected = BinaryExpression(left=IntLiteral(value=1),
                                    right=BinaryExpression(left=IntLiteral(value=2), right=IntLiteral(value=3),
                                                           operator='*'),
                                    operator='+')

        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_multi_binary_expression_with_parenthesis(self):
        lexer = Lexer("((1+2) * 3 + 4")
        parser = Parser(lexer)
        expected = BinaryExpression(left=BinaryExpression(
            left=BinaryExpression(left=IntLiteral(value=1), right=IntLiteral(value=2), operator='+'),
            right=IntLiteral(value=3), operator='*'), right=IntLiteral(value=4), operator='+')

        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_multi_parenthesis_binary_expression(self):
        lexer = Lexer("((1+ 2 * (3*4)) + 4)")
        parser = Parser(lexer)
        expected = BinaryExpression(left=BinaryExpression(left=IntLiteral(value=1),
                                                          right=BinaryExpression(left=IntLiteral(value=2),
                                                                                 right=BinaryExpression(
                                                                                     left=IntLiteral(value=3),
                                                                                     right=IntLiteral(value=4),
                                                                                     operator='*'), operator='*'),
                                                          operator='+'), right=IntLiteral(value=4), operator='+')
        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_parsing_less_than_binary_expression(self):
        lexer = Lexer("1 < 4")
        parser = Parser(lexer)
        expected = BinaryExpression(left=IntLiteral(value=1), right=IntLiteral(value=4), operator='<')

        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
