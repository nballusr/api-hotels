import random
import string
from uuid import uuid4, UUID

from src.modules.hotel.domain.read.hotel import Hotel


class StubHotelBuilder:
    def __init__(self):
        self.__uuid = uuid4()
        self.__name = ''.join(random.choices(string.ascii_lowercase, k=10))
        self.__location = ''.join(random.choices(string.ascii_lowercase, k=10))
        self.__description = ''.join(random.choices(string.ascii_lowercase, k=10))
        self.__has_swimming_pool = False

    def build(self) -> Hotel:
        return Hotel(
            uuid=self.__uuid,
            name=self.__name,
            location=self.__location,
            description=self.__description,
            has_swimming_pool=self.__has_swimming_pool,
        )

    def with_uuid(self, uuid: UUID) -> "StubHotelBuilder":
        self.__uuid = uuid
        return self

    def with_name(self, name: str) -> "StubHotelBuilder":
        self.__name = name
        return self

    def with_location(self, location: str) -> "StubHotelBuilder":
        self.__location = location
        return self

    def with_description(self, description: str) -> "StubHotelBuilder":
        self.__description = description
        return self

    def with_has_swimming_pool(self, has_swimming_pool: bool) -> "StubHotelBuilder":
        self.__has_swimming_pool = has_swimming_pool
        return self
