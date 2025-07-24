from typing import Any

from src.product import LawnGrass, Product, Smartphone


def test_print_mixin(capsys: Any) -> None:
    Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(55" QLED 4K, Фоновая подсветка, 123000.0, 7)'

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"

    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
