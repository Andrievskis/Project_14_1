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

    @property
    def price(self) -> float:
        """Геттер цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Для обработки цены"""
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


# if __name__ == "__main__":
#     product_data: Any = {
#         "name": "Samsung Galaxy S23 Ultra",
#         "description": "256GB, Серый цвет, 200MP камера",
#         "price": 180000.0,
#         "quantity": 5,
#     }
#     new_product = Product(**product_data)
#
#     print(new_product.name)
#     print(new_product.description)
#     print(new_product.price)
#     print(new_product.quantity)
#
#     new_product.price = 800
#     print(new_product.price)
#
#     new_product.price = -100
#     print(new_product.price)
#     new_product.price = 0
#     print(new_product.price)
