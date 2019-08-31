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


def _process_free_special(counter, sku, special_str):
    parts = special_str.split(' ')
    x = parts[0].strip()
    y = parts[3].strip()

    # print(x)
    # print(y)
    assert len(x) == 2
    assert len(y) == 1

    x_sku = x[1]
    assert sku == x_sku
    x_qty = x[0]

    _buy_x_get_y_free(counter, x_sku, int(x_qty), y, 1)


def _process_items_for_price_special(counter, sku, special_str):
    parts = special_str.split(' ')
    items = parts[0].strip()
    price = parts[2].strip()

    items_qty = items[0]
    items_sku = items[1]
    assert sku == items_sku

    return _x_items_for_price(counter, items_sku, int(items_qty), int(price))


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

    free_specials = {}
    large_specials = {}
    small_specials = {}

    # Organise specials
    for sku in input_data:
        special_str = input_data[sku]['specials'].strip()
        if special_str:
            if special_str.endswith('free'):
                free_specials[sku] = special_str
            elif ',' in special_str:
                small_spec, large_spec = special_str.split(',')
                assert 'for' in large_spec
                assert 'for' in small_spec
                large_specials[sku] = large_spec.strip()
                small_specials[sku] = small_spec.strip()
            else:
                assert 'for' in special_str
                large_specials[sku] = special_str

    print(free_specials)
    print(large_specials)
    print(small_specials)

    # Free specials first
    for sku, special_str in free_specials.items():
        _process_free_special(counter, sku, special_str)

    # Large specials next
    for sku, special_str in large_specials.items():
        total += _process_items_for_price_special(counter, sku, special_str)

    # Deal with "2E get one B free"
    # _deal_with_specials(counter, 'E', input_data['E']['specials'])

    # Deal with "2F get one F free"
    # _deal_with_specials(counter, 'F', input_data['F']['specials'])

    # Deal with A specials
    # total += _process_items_for_price_special(counter, 'A', "5A for 200")
    total += _process_items_for_price_special(counter, 'A', "3A for 130")

    # Deal with B specials
    # total += _process_items_for_price_special(counter, 'B', "2B for 45")

    # Nothing should be negative
    for sku in input_data:
        assert counter[sku] >= 0
        total += counter[sku] * int(input_data[sku]['price'])

    return total



