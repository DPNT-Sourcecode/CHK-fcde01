from collections import Counter
from io import StringIO


def _read_prices():
    _input = """
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    | F    | 10    | 2F get one F free      |
    """
    f = StringIO(_input)
    input_data = {}

    for line in f.readlines():
        parts = line.split('|')
        if len(parts) < 4:
            continue
        sku = parts[1].strip()
        price = parts[2].strip()
        specials = parts[3].strip()
        input_data[sku] = {'price': price, 'specials': specials}

    return input_data


def _x_items_for_price(counter, sku, number, price):
    # Calculate number of specials
    special_qty = counter[sku] // number
    # Adjust remaining number
    counter[sku] = counter[sku] % number
    return special_qty * price


def _buy_x_get_y_free(counter, x_sku, x_qty, y_sku, y_qty):
    if x_sku == y_sku:
        free_ys = counter[x_sku] // (x_qty + y_qty)
        counter[y_sku] -= free_ys
    else:
        # When this problem is specified, y_qty should always be 1
        assert y_qty == 1
        free_ys = counter[x_sku] // x_qty
        # We cannot have negative quantities of y_sku
        if counter[y_sku] >= free_ys:
            counter[y_sku] -= free_ys
        else:
            counter[y_sku] = 0


def _deal_with_specials(counter, sku, special_str):
    if special_str and special_str.endswith('free'):
        parts = special_str.split(' ')
        x = parts[0].strip()
        y = parts[3].strip()

        print(x)
        print(y)
        assert len(x) == 2
        assert len(y) == 1

        x_sku = x[1]
        assert sku == x_sku
        x_qty = x[0]

        _buy_x_get_y_free(counter, x_sku, int(x_qty), y, 1)

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    input_data = _read_prices()

    if not isinstance(skus, str):
        return -1

    for char in skus:
        if char not in input_data:
            return -1

    counter = Counter(skus)
    total = 0

    # Deal with "2E get one B free"
    # _buy_x_get_y_free(counter, 'E', 2, 'B', 1)

    # Deal with "2F get one F free"
    # _buy_x_get_y_free(counter, 'F', 2, 'F', 1)

    # Deal with A specials
    total += _x_items_for_price(counter, 'A', 5, 200)
    total += _x_items_for_price(counter, 'A', 3, 130)

    # Deal with B specials
    total += _x_items_for_price(counter, 'B', 2, 45)

    # Nothing should be negative
    for sku in input_data:
        _deal_with_specials(counter, sku, input_data[sku]['specials'])

        assert counter[sku] >= 0
        total += counter[sku] * int(input_data[sku]['price'])

    return total



