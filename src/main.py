import sys

import filerunner
import repl


def main():
    args = sys.argv
    if len(args) == 1:
        repl.start_repl()
    elif len(args) == 2:
        filerunner.execute_file(args[1])


if __name__ == "__main__":
    main()
