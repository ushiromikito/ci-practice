from calc import add, tax_included


def test_add() -> None:
    assert add(2, 3) == 5


def test_tax_included() -> None:
    assert tax_included(1000) == 1100
