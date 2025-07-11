import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    """Функция, которая читает файл."""
    path_json = os.path.abspath(path)
    with open(path_json, "r", encoding="UTF-8") as file:
        data_json = json.load(file)
    return data_json


def create_objects_from_json(data_json: list[dict]) -> Any:
    """Функция, которая создает объекты классов."""
    categories = []
    for category in data_json:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


# if __name__ == "__main__":
#     data = read_json("../data/products.json")
#     from_json = create_objects_from_json(data)
#
#     print(from_json[0].name)
#     print(from_json[0].description)
#     print(from_json[1].name)
