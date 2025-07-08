from typing import Any


def test_category(first_category_info: Any, second_category_info: Any) -> None:
    """Тесты на корректность инициализации объектов класса Category,
    подсчет количества продуктов и категорий."""
    assert first_category_info.name == "Смартфоны"
    assert first_category_info.description == "Смартфоны, как средство коммуникации"

    assert second_category_info.name == "Телевизоры"
    assert second_category_info.description == "Современный телевизор"

    assert first_category_info.product_count == 2
    assert second_category_info.product_count == 2

    assert first_category_info.category_count == 5
    assert second_category_info.category_count == 5
