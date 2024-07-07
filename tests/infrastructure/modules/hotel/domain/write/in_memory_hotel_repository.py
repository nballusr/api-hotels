from uuid import UUID

from src.modules.hotel.domain.write.hotel import Hotel
from src.modules.hotel.domain.write.hotel_repository import HotelRepository


class InMemoryHotelRepository(HotelRepository):
    def __init__(self):
        self.__memory: dict[UUID, Hotel] = {}

    def save(self, hotel: Hotel) -> None:
        self.__memory[hotel.uuid] = hotel

    def of_name(self, name: str) -> Hotel | None:
        for hotel in self.__memory.values():
            if hotel.name == name:
                return hotel

        return None

    def of_uuid(self, uuid: UUID) -> Hotel | None:
        return self.__memory.get(uuid, None)