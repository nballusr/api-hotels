from uuid import UUID

from sqlalchemy.orm import Session

from src.modules.hotel.domain.write.hotel import Hotel
from src.modules.hotel.domain.write.hotel_repository import HotelRepository


class ORMHotelRepository(HotelRepository):
    def __init__(self, db: Session):
        self.__db = db

    def save(self, hotel: Hotel) -> None:
        self.__db.add(hotel)

    def of_name(self, name: str) -> Hotel | None:
        return self.__db.query(Hotel).filter(Hotel.name == name).first()

    def of_uuid(self, uuid: UUID) -> Hotel | None:
        return self.__db.query(Hotel).filter(Hotel.uuid == uuid).first()

    def remove(self, hotel: Hotel) -> None:
        self.__db.delete(hotel)
