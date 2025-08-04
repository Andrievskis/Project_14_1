from src.base_order import BaseOrder
from src.exception_zero import ZeroQuantityError
from src.product import Product


class Category(BaseOrder):
    """Класс описания категории, в который входит информация о продукте класса Product."""

    name: str
    description: str
    __products: list[Product]
    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        """Строковое представление категории."""
        total_product = 0
        for product in self.__products:
            total_product += product.quantity
        return f"{self.name}, количество продуктов: {total_product} шт.\n"

    def add_product(self, product: Product) -> None:
        """Добавление товаров в категорию."""
        try:
            if not isinstance(product, Product):
                raise TypeError("Продукт должен быть экземпляром класса Product.")

            if product.quantity <= 0:
                raise ZeroQuantityError(f"Товар {product.name} имеет нулевое количество")

            if product in self.__products:
                print("Продукт уже существует в категории.")

            else:
                self.__products.append(product)
                Category.product_count += 1
                print(f"Товар {product.name} успешно добавлен в категорию.")
        except ZeroQuantityError as e:
            print(e)
        finally:
            print("Обработка добавления товара завершена.")

    @property
    def products(self) -> str:
        """Вывод списка товаров в виде строк."""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def list_products(self) -> list:
        """Получение списка продуктов."""
        return self.__products

    def middle_price(self) -> float:
        """Метод, который подсчитывает средний ценник всех товаров."""
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
