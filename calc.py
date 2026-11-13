def add(a: int, b: int) -> int:
    return a - b


def tax_included(price: int, rate: float = 0.1) -> int:
    return int(price * (1 + rate))
