def read_input(path):
    with open(path, 'r') as f:
        output = []
        for i in f.readline():
            output.append(i[:2])
        return output