import unittest

from app.backend.interpreter import Interpreter
from app.frontend.lexer.lexer import Lexer
from app.frontend.parser.parser import Parser


class TestParser(unittest.TestCase):
    def test_parsing_integer(self):
        lexer = Lexer("123")
        parser = Parser(lexer)
        expected = 123
        pg = parser.parse()
        interp = Interpreter()
        got = interp.eval(pg)[0]
        self.assertEqual(expected, got)

    def test_eval_binary_expression(self):
        lexer = Lexer("1 + 4 * 9")
        parser = Parser(lexer)
        expected = 37
        pg = parser.parse()
        interp = Interpreter()
        got = interp.eval(pg)[0]
        self.assertEqual(expected, got)

    def test_eval_binary_expressions_with_parenthesis(self):
        lexer = Lexer("1 * (4 * 5) + 6")
        parser = Parser(lexer)
        expected = 26
        pg = parser.parse()
        interp = Interpreter()
        got = interp.eval(pg)[0]
        self.assertEqual(expected, got)

    def test_eval_string(self):
        lexer = Lexer('"evaluating string"')
        parser = Parser(lexer)
        expected = "evaluating string"
        pg = parser.parse()
        interp = Interpreter()
        got = interp.eval(pg)[0]
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
