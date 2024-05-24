from frontend.lexer.lexer import Lexer
from frontend.lexer.tokn import TokenType


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
            token = lexer.next_token()
            while token.token_type != TokenType.EOF:
                print(token)
                token = lexer.next_token()
            print(token)


def print_banner():
    print("   ______  ___  _______")
    print("  / __/ / / / |/ / ___/")
    print(" / _// /_/ /    / /__  ")
    print("/_/  \\____/_/|_/\\___/  ")
    print()
