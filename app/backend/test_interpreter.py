import unittest

from app.backend.interpreter import Interpreter
from app.environment.environment import SymbolTable
from app.frontend.lexer.lexer import Lexer
from app.frontend.parser.parser import Parser


class TestParser(unittest.TestCase):
    def test_eval_integer(self):
        lexer = Lexer("123")
        symtable = SymbolTable()
        parser = Parser(lexer, symtable)
        expected = 123
        pg = parser.parse()
        interp = Interpreter(symtable)
        got = interp.eval(pg)[0]
        self.assertEqual(expected, got)

    def test_eval_binary_expression(self):
        lexer = Lexer("1 + 4 * 9")
        symtable = SymbolTable()
        parser = Parser(lexer, symtable)
        expected = 37
        pg = parser.parse()
        interp = Interpreter(symtable)
        got = interp.eval(pg)[0]
        self.assertEqual(expected, got)

    def test_eval_binary_expressions_with_parenthesis(self):
        lexer = Lexer("1 * (4 * 5) + 6")
        symtable = SymbolTable()
        parser = Parser(lexer, symtable)
        expected = 26
        pg = parser.parse()
        interp = Interpreter(symtable)
        got = interp.eval(pg)[0]
        self.assertEqual(expected, got)

    def test_eval_string(self):
        lexer = Lexer('"evaluating string"')
        symtable = SymbolTable()
        parser = Parser(lexer, symtable)
        expected = "evaluating string"
        pg = parser.parse()
        interp = Interpreter(symtable)
        got = interp.eval(pg)[0]
        self.assertEqual(expected, got)

    def test_eval_less_than_equal_to_operator(self):
        lexer = Lexer("1>=3")
        symtable = SymbolTable()
        parser = Parser(lexer, symtable)
        expected = False
        pg = parser.parse()
        interp = Interpreter(symtable)
        got = interp.eval(pg)[0]
        self.assertEqual(expected, got)

    def test_eval_equality(self):
        lexer = Lexer("44455 == 44455")
        symtable = SymbolTable()
        parser = Parser(lexer, symtable)
        expected = True
        pg = parser.parse()
        interp = Interpreter(symtable)
        got = interp.eval(pg)[0]
        self.assertEqual(expected, got)

    def test_logical_operator(self):
        lexer = Lexer("1 == 1 || 25 < 45")
        symtable = SymbolTable()
        parser = Parser(lexer, symtable)
        expected = True
        pg = parser.parse()
        interp = Interpreter(symtable)
        got = interp.eval(pg)[0]
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
