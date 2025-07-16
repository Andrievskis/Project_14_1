from src.product import Product


class Category:
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
        if not isinstance(product, Product):
            raise TypeError("Продукт должен быть экземпляром класса Product.")

        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Продукт уже существует в категории.")

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


# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(str(product1))
#     print(str(product2))
#     print(str(product3))
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     print(str(category1))
#
#     print(category1.products)
#
#     print(product1 + product2)
#     print(product1 + product3)
#     print(product2 + product3)
