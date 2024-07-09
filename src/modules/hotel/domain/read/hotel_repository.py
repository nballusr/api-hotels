from abc import ABC, abstractmethod
from uuid import UUID

from src.modules.hotel.domain.read.hotel import Hotel


class HotelRepository(ABC):
    @abstractmethod
    def of_uuid(self, uuid: UUID) -> Hotel | None:
        pass

    @abstractmethod
    def all(self) -> list[Hotel]:
        pass
