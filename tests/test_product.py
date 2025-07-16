from typing import Any
from unittest.mock import patch

import pytest

from src.product import Product


def test_product(products_info: Any) -> None:
    """Тесты на корректность инициализации объектов класса
    Product."""
    assert products_info.name == "iPhone"
    assert products_info.description == "200GB, Синий"
    assert products_info.price == 31000.0
    assert products_info.quantity == 14


def test_new_product() -> None:
    """Тест на создание новой задачи."""
    product_data: Any = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }

    new_product = Product(**product_data)
    new_product.name = "Samsung Galaxy S23 Ultra"
    new_product.description = "256GB, Серый цвет, 200MP камера"
    new_product.price = 180000.0
    new_product.quantity = 5


@patch("builtins.input", return_value="y")
def test_set_positive_price(mock_input: Any) -> None:
    """Тест на установку положительной цены."""
    product = Product("iPhone 15", "512GB, Gray space", 120000.0, 8)
    product.price = 100000
    assert product.price == 100000


def test_set_negative_price() -> None:
    """Тест на установку отрицательной цены."""
    product = Product("iPhone 15", "512GB, Gray space", 120000.0, 8)
    product.price = -100
    assert product.price == 120000


@patch("builtins.input", return_value="y")
def test_decrease_price_with_confirm(mock_input: Any) -> None:
    """Тест на снижение цены с подтверждением."""
    product = Product("iPhone 15", "512GB, Gray space", 120000.0, 8)
    product.price = 100000
    assert product.price == 100000


@patch("builtins.input", return_value="n")
def test_decrease_price_without_confirm(mock_input: Any) -> None:
    """Тест на снижение цены без подтверждения"""
    product = Product("iPhone 15", "512GB, Gray space", 120000.0, 8)
    product.price = 100000
    assert product.price == 120000


def test_str(products_info: Product) -> None:
    """Тест на получение строкового значения."""
    assert str(products_info) == "iPhone, 31000.0 руб. Остаток: 14 шт."


def test_sum(products_info: Product) -> None:
    """Тест на общее суммарное значение."""
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    result = products_info.total_value + product1.total_value
    assert result == 2114000.0


def test_sum_error(products_info: Product) -> None:
    """Тест на ошибку."""
    with pytest.raises(ValueError):
        products_info + 123
