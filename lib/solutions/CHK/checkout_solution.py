from collections import Counter
from io import StringIO


def _read_prices():
    _input = """
    | A    | 50    | 3A for 130, 5A for 200          |
    | B    | 30    | 2B for 45                       |
    | C    | 20    |                                 |
    | D    | 15    |                                 |
    | E    | 40    | 2E get one B free               |
    | F    | 10    | 2F get one F free               |
    | G    | 20    |                                 |
    | H    | 10    | 5H for 45, 10H for 80           |
    | I    | 35    |                                 |
    | J    | 60    |                                 |
    | K    | 70    | 2K for 120                      |
    | L    | 90    |                                 |
    | M    | 15    |                                 |
    | N    | 40    | 3N get one M free               |
    | O    | 10    |                                 |
    | P    | 50    | 5P for 200                      |
    | Q    | 30    | 3Q for 80                       |
    | R    | 50    | 3R get one Q free               |
    | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | U    | 40    | 3U get one U free               |
    | V    | 50    | 2V for 90, 3V for 130           |
    | W    | 20    |                                 |
    | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
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


def _group_discount(counter, group_skus, group_price=45):
    total_group_items = 0
    for sku in group_skus:
        total_group_items += counter[sku]

    group_discounts = total_group_items // 3
    group_total_cost = group_discounts * group_price

    # Remove the correct number of items from the various skus
    # These items will be charged as a group instead
    reduce_total = group_discounts * 3
    for sku, price in sorted(group_skus.items()):
        # Reduce the most expensive sku first

        sku_count = counter[sku]
        if sku_count >= reduce_total:
            counter[sku] -= reduce_total
            reduce_total -= reduce_total
        else:
            counter[sku] -= sku_count
            reduce_total -= sku_count

        if reduce_total <= 0:
            break

    return group_total_cost


def _process_free_special(counter, sku, special_str):
    parts = special_str.split(' ')
    x = parts[0].strip()
    y = parts[3].strip()

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

    items_qty = items[:-1]
    items_sku = items[-1]
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
    group_specials = {}

    # Organise and process specials (text)
    for sku in input_data:
        special_str = input_data[sku]['specials'].strip()
        if special_str:
            if special_str.endswith('free'):
                free_specials[sku] = special_str
            elif special_str.startswith('buy any'):
                group_specials[sku] = special_str
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
    print(group_specials)

    # Free specials first
    for sku, special_str in free_specials.items():
        _process_free_special(counter, sku, special_str)

    # Large specials next
    for sku, special_str in large_specials.items():
        total += _process_items_for_price_special(counter, sku, special_str)

    # Small specials last
    for sku, special_str in small_specials.items():
        total += _process_items_for_price_special(counter, sku, special_str)

    # Build a dict of group skus and prices
    group_skus = {}
    for sku in ['S', 'T', 'X', 'Y', 'Z']:
        group_skus[sku] = input_data[sku]['price']

    # Group specials (Buy Any X)
    for sku, special_str in group_specials.items():
        total += _group_discount(counter, group_skus, group_price=45)

    # Nothing should be negative
    for sku in input_data:
        assert counter[sku] >= 0
        total += counter[sku] * int(input_data[sku]['price'])

    return total


