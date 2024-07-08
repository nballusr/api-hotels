from abc import ABC, abstractmethod

from pydantic import BaseModel


class HotelInformation(BaseModel):
    name: str
    location: str
    description: str
    has_swimming_pool: bool


class GetHotelInformationService(ABC):
    @abstractmethod
    def from_name(self, name: str) -> HotelInformation | None:
        pass
