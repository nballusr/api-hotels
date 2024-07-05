from abc import ABC, abstractmethod


class QueryHandler(ABC):
    @abstractmethod
    def __call__(self, query) -> None:
        pass
