# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    raise NotImplementedError()


def sum(int_1: int, int_2: int) -> int:
    if (int_1 or int_2) > 100:
        raise ValueError("Argument out of bounds")
    elif (int_1 or int_2) < 0:
        raise ValueError("Argument out of bounds")
    # redfining builtin method
    return int_1 + int_2

