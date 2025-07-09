from typing import Any

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def products_info() -> Any:
    return Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14)


@pytest.fixture
def first_category_info() -> Any:
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство коммуникации",
        products=[
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
            Product("Xiaomi", "Black", 50000, 5),
            Product("Xiaomi Note", "Read", 25000.0, 4),
        ],
    )


@pytest.fixture
def second_category_info() -> Any:
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=[Product("Philips", "4K", 50000.0, 2), Product("Samsung", "3D", 60000.50, 7)],
    )
