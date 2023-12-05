def read_input(path):
    with open(path, 'r') as f:
        output = []
        for i in f.readlines():
            output.append(i[0:len(i)-1])
        return output