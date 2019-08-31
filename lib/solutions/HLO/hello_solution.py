

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
    # "Hello, John!"
    return "Hello, {}!".format(friend_name.strip())
