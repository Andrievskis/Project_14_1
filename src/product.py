from typing import Any


class Product:
    """Класс описания продукта."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое отображение продукта."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def total_value(self) -> float:
        """Общая стоимость продукта (цена * количество)."""
        return self.__price * self.quantity

    def __add__(self, other: float) -> float | str:
        """Суммарное представление стоимости товаров."""
        if isinstance(other, Product):
            return self.total_value + other.total_value
        else:
            raise ValueError("Other не является объектом класса Product.")

    @property
    def price(self) -> float:
        """Геттер цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Обработка цены."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная.")
        elif new_price < self.__price:
            confirmation: str = input(f"Цена снижается с {self.__price} до {new_price}. Подтвердить (y/n)? ")
            if confirmation.lower() == "y":
                self.__price = new_price
            else:
                print("Отмена действия.")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int, new_list_products: Any) -> Any:
        """Класс-метод."""
        if new_list_products:
            for name_product in new_list_products:
                if name_product.name == name:
                    name_product.quantity += quantity
                    name_product.price = max(name_product.price, price)
                    return name_product
        return cls(name, description, price, quantity)


# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(str(product1))
#     print(str(product2))
#     print(str(product3))
#
#     print(product1 + product2)
#     print(product1 + product3)
#     print(product2 + product3)
