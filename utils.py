def find_shops(index: dict, products: list) -> set:
    """
    Find all the shops that contain all the products
    :param index: Index of products
    :param products: Products to match
    :return: Set of all shops that sell all mentioned products
    """
    try:
        final_set = index[products[0]]['shops']  # Initial initialization
        for i in products[1:]:  # All but first
            final_set.intersection_update(index[i]['shops'])
        return final_set
    except KeyError:  # The item was not in any shop
        return set()


def calculate_price(index: dict, products: list, shop: int) -> float:
    """
    Calculate total for given products from a shop
    :param index: Index of products
    :param products: List of products to buy
    :param shop: ID of shp[
    :return: Total price
    """
    price = 0.
    for i in products:
        price += index[i]['price'][shop]
    return price
