from unittest import TestCase
from uuid import uuid4

from src.modules.hotel.application.get_hotel.get_hotel_query import GetHotelQuery
from src.modules.hotel.application.get_hotel.get_hotel_query_handler import GetHotelQueryHandler
from src.modules.hotel.domain.exception.hotel_not_found_exception import HotelNotFoundException
from tests.infrastructure.modules.hotel.domain.read.in_memory_hotel_repository import InMemoryHotelRepository
from tests.infrastructure.modules.hotel.domain.read.stub_hotel_builder import StubHotelBuilder


class GetHotelQueryHandlerTest(TestCase):
    def setUp(self):
        self.__in_memory_hotel_repository = InMemoryHotelRepository()
        self.__handler = GetHotelQueryHandler(self.__in_memory_hotel_repository)

    def test_non_existing_hotel_raises_exception(self) -> None:
        query = GetHotelQuery(uuid=(uuid := uuid4()))

        with self.assertRaises(HotelNotFoundException) as e:
            self.__handler(query)

        self.assertEqual(f"Hotel with uuid {uuid} not found", e.exception.message)

    def test_hotel_is_returned(self) -> None:
        self.__in_memory_hotel_repository.save(
            StubHotelBuilder()
            .with_uuid(hotel_uuid := uuid4())
            .with_name("Name")
            .with_location("Location")
            .with_description("Description")
            .with_has_swimming_pool(False)
            .build()
        )

        query = GetHotelQuery(uuid=hotel_uuid)

        hotel = self.__handler(query)

        self.assertIsNotNone(hotel)
        self.assertEqual(hotel_uuid, hotel.uuid)
        self.assertEqual("Name", hotel.name)
        self.assertEqual("Location", hotel.location)
        self.assertEqual("Description", hotel.description)
        self.assertFalse(hotel.has_swimming_pool)
