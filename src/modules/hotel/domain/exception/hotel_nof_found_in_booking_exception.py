from src.shared.domain.exception.not_found_exception import NotFoundException


class HotelNotFoundInBookingException(NotFoundException):
    @classmethod
    def create(cls, name: str) -> "HotelNotFoundInBookingException":
        return cls(f"No hotel found in booking with name {name}")
