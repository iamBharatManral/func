from app.backend.interpreter import Interpreter
from app.frontend.lexer.lexer import Lexer
from app.frontend.parser.parser import Parser


def execute_file(filename):
    with open(filename) as f:
        source = f.read()
        if len(source) == 0:
            exit(0)
        lexer = Lexer(source)
        parser = Parser(lexer)
        pg = parser.parse()
        if len(parser.errors) > 0:
            print(parser.errors)
        else:
            interpreter = Interpreter()
            output = interpreter.eval(pg)
            for out in output:
                print(out)
