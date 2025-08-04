from src.base_order import BaseOrder
from src.exception_zero import ZeroQuantityError
from src.product import Product


class Order(BaseOrder):
    """Класс заказ."""
    def __init__(self, product: Product, quantity: int):
        try:
            if quantity <= 0:
                raise ZeroQuantityError()

            self.product = product
            self.quantity = quantity
            self.total_price = self.product.price * self.quantity
            print(f"Товар {self.product.name} успешно добавлен в заказ.")
        except ZeroQuantityError as e:
            print(e)
        finally:
            print("Обработка добавления товара завершена.")

    def __str__(self) -> str:
        """Вывод на печать информации о заказе и его итоговой стоимости."""
        if hasattr(self, 'error') and self.error:
            return "Заказ не может быть сформирован из-за ошибки."
        if not all(hasattr(self, attr) for attr in ['product', 'quantity', 'total_price']):
            return "Заказ не может быть сформирован из-за ошибки."
        return (
            f'Заказан товар "{self.product.name}" в количестве {self.quantity} шт.\n'
            f"Сумма к оплате {self.total_price:.2f} руб."
        )


if __name__ == '__main__':
    product4 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    order1 = Order(product4, 9)
    print(order1)
