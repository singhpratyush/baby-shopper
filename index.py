def build_index(data: list) -> tuple:
    """
    Create an index with items and shops for faster lookup. Format -
    {
        'product1': 'shops': set([1, 3, 5]),
        ...
    }
    {
        shop1: [
            (price1, [item1, item2, ...]),
            ...
        ],
        ...
    }
    :param data: List of tuples containg data about products and shops
    :return: An index based on products and shops
    """
    item_index = {}  # Create an empty item_index
    shop_index = {}
    for item in data:
        for product in item[2]:
            if product not in item_index:  # New, initialize
                item_index[product] = set()
            item_index[product].add(item[0])  # Add to shop set

        if item[0] not in shop_index:
            shop_index[item[0]] = []
        shop_index[item[0]].append((item[1], item[2:]))
    return item_index, shop_index
