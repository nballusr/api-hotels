from src.shared.domain.exception.domain_exception import DomainException


class HotelAlreadyExistsException(DomainException):
    @classmethod
    def create(cls, name: str) -> "HotelAlreadyExistsException":
        return cls(f"Hotel with name {name} already exists")
