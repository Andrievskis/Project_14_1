from src.order import Order
from src.product import Product


def test_order(products_info: Product) -> None:
    """Тест на корректный вывод информации о товаре."""
    order = Order(products_info, 2)
    assert order.product.name == "iPhone"
    assert order.quantity == 2
    assert order.total_price == 62000.0


def test_order_str(products_info: Product) -> None:
    """Тест на корректный строковый вывод информации о товаре."""
    order = Order(products_info, 2)
    assert str(order) == 'Заказан товар "iPhone" в количестве 2 шт.\nСумма к оплате 62000.00 руб.'
