from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1

    for char in skus:
        if char not in 'ABCDEF':
            return -1

    c = Counter(skus.lower())
    a_count = c['a']
    b_count = c['b']
    c_count = c['c']
    d_count = c['d']
    e_count = c['e']
    f_count = c['f']

    # Deal with "2E get one B free"
    # We cannot have negative quantities of B
    free_bs = e_count // 2
    if b_count >= free_bs:
        b_count -= free_bs
    else:
        b_count = 0

    # Deal with "2F get one F free"
    free_fs = f_count // 3
    f_count -= free_fs

    # Deal with A specials
    a_5_200 = a_count // 5
    a_count = a_count % 5
    a_3_130 = a_count // 3
    a_count = a_count % 3

    # Deal with B specials
    b_special = b_count // 2
    b_count = b_count % 2

    # Nothing should be negative
    assert a_count >= 0
    assert b_count >= 0
    assert c_count >= 0
    assert d_count >= 0
    assert e_count >= 0
    assert f_count >= 0

    return ((a_5_200 * 200) + (a_3_130 * 130) + (a_count * 50) + (b_special * 45) + (b_count * 30)
            + (c_count * 20) + (d_count * 15) + (e_count * 40) + (f_count * 10))


