from uuid import UUID

from src.shared.domain.exception.domain_exception import DomainException


class HotelAlreadyExistsException(DomainException):
    @classmethod
    def of_name(cls, name: str) -> "HotelAlreadyExistsException":
        return cls(f"Hotel with name {name} already exists")

    @classmethod
    def of_uuid(cls, uuid: UUID) -> "HotelAlreadyExistsException":
        return cls(f"Hotel with uuid {uuid} already exists")
