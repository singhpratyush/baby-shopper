def read_data(filename: str, has_header: bool = False) -> list:
    """
    Reads a CSV file and stores result in the following format -
    [
        (shop1, price1, [product1, product2, ...]),
        ...
    ]
    :param filename: Filename to read from
    :param has_header: True indicates that CSV file has a header
    :return: Cleaned data from CSV file
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    if has_header:  # File has header, ignore first line
        lines = lines[1:]
    lines = [x for x in lines if len(x) > 0]  # Remove empty lines
    return list(map(clean_data, lines))


def clean_data(line: str) -> tuple:
    line = line.replace('\n', '').replace(' ', '').split(',')  # Clean
    line[0] = int(line[0])
    line[1] = float(line[1])
    return line[0], line[1], line[2:]  # All after 2nd are product names
