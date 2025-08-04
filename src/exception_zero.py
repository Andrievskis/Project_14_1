class ZeroQuantityError(Exception):
    """Исключение, возникающее при попытке добавить товар с нулевым количеством."""
    def __init__(self, message: str = "Нельзя добавить товар с нулевым количеством."):
        self.message: str = message
        super().__init__(self.message)
