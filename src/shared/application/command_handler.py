from abc import ABC, abstractmethod


class CommandHandler(ABC):
    @abstractmethod
    def __call__(self, command) -> None:
        pass
