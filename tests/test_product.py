from typing import Any


def test_product(products_info: Any) -> None:
    """Тесты на корректность инициализации объектов класса
    Product."""
    assert products_info.name == "Xiaomi Redmi Note 11"
    assert products_info.description == "1024GB, Синий"
    assert products_info.price == 31000.0
    assert products_info.quantity == 14
