from abc import ABC, abstractmethod
from uuid import UUID

from src.modules.hotel.domain.write.hotel import Hotel


class HotelRepository(ABC):
    @abstractmethod
    def save(self, hotel: Hotel) -> None:
        pass

    @abstractmethod
    def of_name(self, name: str) -> Hotel | None:
        pass

    @abstractmethod
    def of_uuid(self, uuid: UUID) -> Hotel | None:
        pass
