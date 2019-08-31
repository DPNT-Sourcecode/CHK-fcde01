from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1

    for char in skus:
        if char not in 'ABCDE':
            return -1

    c = Counter(skus.lower())
    a_count = c['a']
    b_count = c['b']
    c_count = c['c']
    d_count = c['d']
    e_count = c['e']

    free_bs = e_count // 2
    b_count -= free_bs

    a_special = a_count // 3
    a_count = a_count % 3
    b_special = b_count // 2
    b_count = b_count % 2

    return ((a_special * 130) + (a_count * 50) + (b_special * 45) + (b_count * 30)
            + (c_count * 20) + (d_count * 15) + (e_count * 40))


