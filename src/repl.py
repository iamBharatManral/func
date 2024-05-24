from frontend.lexer.lexer import Lexer
from frontend.parser.parser import Parser


def start_repl():
    print_banner()
    while True:
        source = input("λ: ")
        if source == ":q" or source == "quit":
            exit(0)
        elif len(source) == 0:
            continue
        else:
            lexer = Lexer(source)
            parser = Parser(lexer)
            pg = parser.parse()
            if len(parser.errors) > 0:
                print(parser.errors)
            else:
                print(pg.statements)


def print_banner():
    print("   ______  ___  _______")
    print("  / __/ / / / |/ / ___/")
    print(" / _// /_/ /    / /__  ")
    print("/_/  \\____/_/|_/\\___/  ")
    print()
