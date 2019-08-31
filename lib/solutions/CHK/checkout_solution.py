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


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    input_data = _read_prices()

    if not isinstance(skus, str):
        return -1

    for char in skus:
        if char not in input_data:
            return -1

    counter = Counter()

    # Deal with "2E get one B free"
    # We cannot have negative quantities of B
    free_bs = counter['E'] // 2
    if counter['B'] >= free_bs:
        counter['B'] -= free_bs
    else:
        counter['B'] = 0

    # Deal with "2F get one F free"
    free_fs = counter['F'] // 3
    counter['F'] -= free_fs

    # Deal with A specials
    a_5_200 = counter['A'] // 5
    counter['A'] = counter['A'] % 5
    a_3_130 = counter['A'] // 3
    counter['A'] = counter['A'] % 3

    # Deal with B specials
    b_special = counter['B'] // 2
    counter['B'] = counter['B'] % 2

    total = (a_5_200 * 200) + (a_3_130 * 130) + (b_special * 45)

    # Nothing should be negative
    for sku in input_data:
        assert counter[sku] >= 0
        total += counter[sku] * int(input_data[sku]['price'])

    return total


