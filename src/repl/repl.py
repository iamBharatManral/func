def start_repl():
    print_banner()
    while True:
        source = input("λ: ")
        if source == ":q" or source == "quit":
            exit(0)
        else:
            print(source)


def print_banner():
    print("   ______  ___  _______")
    print("  / __/ / / / |/ / ___/")
    print(" / _// /_/ /    / /__  ")
    print("/_/  \\____/_/|_/\\___/  ")
    print()
