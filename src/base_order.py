from abc import ABC, abstractmethod


class BaseOrder(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass
