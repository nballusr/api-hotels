from uuid import UUID

from src.modules.hotel.domain.read.hotel import Hotel
from src.modules.hotel.domain.read.hotel_repository import HotelRepository


class InMemoryHotelRepository(HotelRepository):
    def __init__(self):
        self.__memory: dict[UUID, Hotel] = {}

    def save(self, hotel: Hotel) -> None:
        self.__memory[hotel.uuid] = hotel

    def of_uuid(self, uuid: UUID) -> Hotel | None:
        return self.__memory.get(uuid, None)

    def all(self) -> list[Hotel]:
        return list(self.__memory.values())
