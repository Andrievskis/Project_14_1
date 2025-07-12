from typing import Any

from src.category import Category
from src.product import Product


def test_category(first_category_info: Any, second_category_info: Any) -> None:
    """Тесты на корректность инициализации объектов класса Category,
    подсчет количества продуктов и категорий."""
    assert first_category_info.name == "Смартфоны"
    assert first_category_info.description == "Смартфоны, как средство коммуникации"

    assert second_category_info.name == "Телевизоры"
    assert second_category_info.description == "Современный телевизор"

    assert first_category_info.product_count == 5
    assert second_category_info.product_count == 5

    assert first_category_info.category_count == 2
    assert second_category_info.category_count == 2


def test_products_property(first_category_info: Category) -> None:
    """Тест на вывод списка товаров в виде строк."""
    assert first_category_info.products == (
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Xiaomi, 50000 руб. Остаток: 5 шт.\n"
        "Xiaomi Note, 25000.0 руб. Остаток: 4 шт.\n"
    )


def test_add_product(first_category_info: Category, products_info: Product) -> None:
    """Тест на добавление товаров в категорию."""
    first_category_info.add_product(products_info)
    assert first_category_info.products == (
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Xiaomi, 50000 руб. Остаток: 5 шт.\n"
        "Xiaomi Note, 25000.0 руб. Остаток: 4 шт.\n"
        "iPhone, 31000.0 руб. Остаток: 14 шт.\n"
    )
