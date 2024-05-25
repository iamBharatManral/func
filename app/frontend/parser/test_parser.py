import unittest

from app.environment.environment import SymbolTable
from .ast import IntLiteral, FloatLiteral, StringLiteral, BinaryExpression
from .parser import Parser
from ..lexer.lexer import Lexer


class TestParser(unittest.TestCase):
    def test_parsing_integer(self):
        symtable = SymbolTable()
        lexer = Lexer("123")
        parser = Parser(lexer, symtable)
        expected = IntLiteral(123)
        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_parsing_float(self):
        symtable = SymbolTable()
        lexer = Lexer("123.455")
        parser = Parser(lexer, symtable)
        expected = FloatLiteral(123.455)
        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_parsing_string(self):
        lexer = Lexer("\"hello world\"")
        symtable = SymbolTable()
        parser = Parser(lexer, symtable)
        expected = StringLiteral("hello world")
        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_addition(self):
        lexer = Lexer("-1+2")
        symtable = SymbolTable()
        parser = Parser(lexer, symtable)
        expected = BinaryExpression(left=IntLiteral(value=-1), right=IntLiteral(value=2), operator='+')
        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_multi_binary_expression(self):
        lexer = Lexer("1 + 2 * 3")
        symtable = SymbolTable()
        parser = Parser(lexer,symtable)
        expected = BinaryExpression(left=IntLiteral(value=1),
                                    right=BinaryExpression(left=IntLiteral(value=2), right=IntLiteral(value=3),
                                                           operator='*'),
                                    operator='+')

        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_multi_binary_expression_with_parenthesis(self):
        lexer = Lexer("((1+2) * 3 + 4")
        symtable = SymbolTable()
        parser = Parser(lexer,symtable)
        expected = BinaryExpression(left=BinaryExpression(
            left=BinaryExpression(left=IntLiteral(value=1), right=IntLiteral(value=2), operator='+'),
            right=IntLiteral(value=3), operator='*'), right=IntLiteral(value=4), operator='+')

        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_multi_parenthesis_binary_expression(self):
        lexer = Lexer("((1+ 2 * (3*4)) + 4)")
        symtable = SymbolTable()
        parser = Parser(lexer,symtable)
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
        symtable = SymbolTable()
        parser = Parser(lexer,symtable)
        expected = BinaryExpression(left=IntLiteral(value=1), right=IntLiteral(value=4), operator='<')

        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)

    def test_parsing_logical_and(self):
        lexer = Lexer("(1 >= 2) && 2 != 2")
        symtable = SymbolTable()
        parser = Parser(lexer,symtable)
        expected = BinaryExpression(
            left=BinaryExpression(left=IntLiteral(value=1), right=IntLiteral(value=2), operator='>='),
            right=BinaryExpression(left=IntLiteral(value=2), right=IntLiteral(value=2), operator='!='), operator='&&')
        pg = parser.parse()
        got = pg.statements[0]
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
