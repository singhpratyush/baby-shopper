def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return map(clean_data, lines)


def clean_data(line):
    line = line.replace('\n', '').split(',')
    line[0] = int(line[0])
    line[1] = float(line[1])
    return line[0], line[1], line[2:]
