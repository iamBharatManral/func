import sys

from app.filerunner import execute_file
from app.repl import start_repl


def main():
    args = sys.argv
    if len(args) == 1:
        start_repl()
    elif len(args) == 2:
        execute_file(args[1])


if __name__ == "__main__":
    main()
