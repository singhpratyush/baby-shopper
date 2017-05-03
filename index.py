def build_index(data: list) -> dict:
    """
    Create an index with items for faster lookup. Format -
    {
        'product1': {
            'shops': set([1, 3, 5]),
             'price': {
                1: 10.0,
                3: 11.5,
                4: 8.0
             }
        },
        ...
    }
    :param data: List of tuples containg data about products and shops
    :return: An index based on products
    """
    index = {}  # Create an empty index
    for item in data:
        for product in item[2]:
            if product not in index:  # New, initialize
                index[product] = {
                    'shops': set(),
                    'price': {}
                }
            index[product]['shops'].add(item[0])  # Add to shop set
            index[product]['price'][item[0]] = item[1]  # Add price details
    return index
