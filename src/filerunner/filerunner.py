def execute_file(filename):
    with open(filename) as f:
        source = f.read()
        print(source)
