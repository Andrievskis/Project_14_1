import pytest

from src.category import Category
from src.category_iter import CategoryIterator


def test_category_iter(first_category_info: Category) -> None:
    """Тест на корректную работу вспомогательного класса."""
    iterator = CategoryIterator(first_category_info)
    products_str = ""
    for product in iterator:
        products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

    assert products_str == (
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Xiaomi, 50000 руб. Остаток: 5 шт.\n"
        "Xiaomi Note, 25000.0 руб. Остаток: 4 шт.\n"
    )


def test_category_iter_(first_category_info: Category) -> None:
    """Тест на корректную работу вспомогательного класса
    и обработка ошибки в случае отсутствия следующей итерации."""
    iterator = CategoryIterator(first_category_info)

    assert next(iterator).name == "Xiaomi Redmi Note 11"
    assert next(iterator).name == "Xiaomi"
    assert next(iterator).name == "Xiaomi Note"

    with pytest.raises(StopIteration):
        next(iterator)
