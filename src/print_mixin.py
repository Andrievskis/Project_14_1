class PrintMixin:
    """Класс-миксин."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        """Вывод в консоль информации (по заданному шаблону):
        от какого класса и с какими параметрами был создан объект."""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
