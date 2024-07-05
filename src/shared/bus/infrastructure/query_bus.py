from abc import ABC, abstractmethod
from typing import Any


class QueryBus(ABC):
    @abstractmethod
    def handle(self, query) -> Any:
        pass
