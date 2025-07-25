from src.base_order import BaseOrder
from src.product import Product


class Order(BaseOrder):
    """Класс заказ."""
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity

    def __str__(self) -> str:
        """Вывод на печать информации о заказе и его итоговой стоимости."""
        return (
            f'Заказан товар "{self.product.name}" в количестве {self.quantity} шт.\n'
            f"Сумма к оплате {self.total_price:.2f} руб."
        )
