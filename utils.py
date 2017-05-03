def find_shops(index: dict, products: list) -> set:
    """
    Find all the shops that contain all the products
    :param index: Index of products
    :param products: Products to match
    :return: Set of all shops that sell all mentioned products
    """
    try:
        final_set = index[products[0]]  # Initial initialization
        for i in products[1:]:  # All but first
            final_set.intersection_update(index[i])
        return final_set
    except KeyError:  # The item was not in any shop
        return set()


def calculate_price(index: dict, products: list, shop: int) -> float:
    """
    Find the best purchase combination for a fiven list of items in the shop
    :param index: Index of shop
    :param products: List of items
    :param shop: ID of shop
    :return: Best price
    """
    price = 0.
    while products:  # While we do not have taken all the products
        i = products[0]  # Pick a product
        prices = []

        # Check for its price in all type of packages
        for j in index[shop]:
            if i in j[1][0]:
                prices.append((j[0], j[1][0]))

        # Get the best package
        best_price = min(prices)
        price += best_price[0]
        for k in best_price[1]:
            if k in products:
                products.remove(k)  # Get all required items from the package

    return price
