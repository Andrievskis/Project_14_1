from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
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
        # PrintMixin.__init__(self)
        super().__init__()

    def __str__(self) -> str:
        """Строковое отображение продукта."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def total_value(self) -> float:
        """Общая стоимость продукта (цена * количество)."""
        return self.__price * self.quantity

    def __add__(self, other: float) -> float | str:
        """Суммарное представление стоимости товаров."""
        if not isinstance(other, Product):
            raise ValueError("Other не является объектом класса Product.")
        elif type(self) is not type(other):
            raise TypeError("Нельзя складывать товары из разных классов продуктов.")
        else:
            return self.total_value + other.total_value

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


class Smartphone(Product):
    """Класс описания смартфонов."""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс описания газонно травы."""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
