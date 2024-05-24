def execute_file(filename):
    with open(filename) as f:
        source = f.read()
        if len(source) == 0:
            exit(0)
        print(source)
