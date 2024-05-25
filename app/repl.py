from app.backend.interpreter import Interpreter
from app.environment.environment import SymbolTable
from app.frontend.lexer.lexer import Lexer
from app.frontend.parser.parser import Parser


def start_repl():
    symtable = SymbolTable()
    print_banner()
    while True:
        source = input("λ: ")
        if source == ":q" or source == "quit":
            exit(0)
        elif len(source) == 0:
            continue
        else:
            lexer = Lexer(source)
            parser = Parser(lexer, symtable)
            pg = parser.parse()
            if len(parser.errors) > 0:
                for err in parser.errors:
                    print(err)
            else:
                interpreter = Interpreter(symtable)
                output = interpreter.eval(pg)
                for out in output:
                    if out is not None:
                        print(out)


def print_banner():
    print("   ______  ___  _______")
    print("  / __/ / / / |/ / ___/")
    print(" / _// /_/ /    / /__  ")
    print("/_/  \\____/_/|_/\\___/  ")
    print()
