from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from src.modules.hotel.domain.read.hotel import Hotel
from src.modules.hotel.domain.read.hotel_repository import HotelRepository


class SQLHotelRepository(HotelRepository):
    def __init__(self, db: Session):
        self.__db = db

    def of_uuid(self, uuid: UUID) -> Hotel | None:
        result = self.__db.execute(
            text(
                """
                SELECT h.uuid, h.name, h.location, h.description, h.has_swimming_pool
                FROM hotel h
                WHERE h.uuid = :uuid
                """
            ),
            {"uuid": uuid}
        )

        row = result.fetchone()
        if row is None:
            return None

        return Hotel(
            uuid=row.uuid,
            name=row.name,
            location=row.location,
            description=row.description,
            has_swimming_pool=row.has_swimming_pool,
        )

    def all(self) -> list[Hotel]:
        result = self.__db.execute(
            text(
                """
                SELECT h.uuid, h.name, h.location, h.description, h.has_swimming_pool
                FROM hotel h
                """
            )
        )

        rows = result.fetchall()

        return [
            Hotel(
                uuid=row.uuid,
                name=row.name,
                location=row.location,
                description=row.description,
                has_swimming_pool=row.has_swimming_pool,
            )
            for row in rows
        ]
