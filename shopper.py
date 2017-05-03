import sys

import data
import index
import utils


def main() -> None:
    """
    Driver method
    """
    # Read arguments
    filename = sys.argv[1]
    products = sys.argv[2:]

    # Load data and create index
    items = data.read_data(filename)
    item_index = index.build_index(items)

    # Find relevant shops
    shops = utils.find_shops(item_index, products)

    # Calculate price for each of them and store in list of tuples format
    #  with first index as shop ID and second as final price -
    #  [
    #       (shop1, total1),
    #       (shop2, total2),
    #       ...
    #  ]
    price_list = [(i, utils.calculate_price(item_index, products, i))
                  for i in shops]

    if price_list:
        best_price = min(price_list, key=lambda x: x[1])  # Find the best price
    else:  # No relevant shop found
        best_price = None

    print(best_price)


if __name__ == '__main__':
    main()
