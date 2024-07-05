from uuid import UUID

from src.shared.domain.exception.not_found_exception import NotFoundException


class HotelNotFoundException(NotFoundException):
    @classmethod
    def create(cls, uuid: UUID) -> "HotelNotFoundException":
        return cls(f"Hotel with uuid {str(uuid)} not found")
