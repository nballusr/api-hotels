from abc import ABC, abstractmethod

from src.modules.hotel.domain.write.hotel import Hotel


class HotelRepository(ABC):
    @abstractmethod
    def save(self, hotel: Hotel) -> None:
        pass

    @abstractmethod
    def of_name(self, name: str) -> Hotel | None:
        pass
