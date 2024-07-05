from abc import ABC, abstractmethod


class CommandBus(ABC):
    @abstractmethod
    def handle(self, command) -> None:
        pass
