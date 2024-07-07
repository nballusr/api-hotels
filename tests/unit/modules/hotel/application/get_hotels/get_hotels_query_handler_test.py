from unittest import TestCase
from uuid import uuid4

from src.modules.hotel.application.get_hotel.get_hotel_query import GetHotelQuery
from src.modules.hotel.application.get_hotel.get_hotel_query_handler import GetHotelQueryHandler
from src.modules.hotel.application.get_hotels.get_hotels_query import GetHotelsQuery
from src.modules.hotel.application.get_hotels.get_hotels_query_handler import GetHotelsQueryHandler
from src.modules.hotel.domain.exception.hotel_not_found_exception import HotelNotFoundException
from tests.infrastructure.modules.hotel.domain.read.in_memory_hotel_repository import InMemoryHotelRepository
from tests.infrastructure.modules.hotel.domain.read.stub_hotel_builder import StubHotelBuilder


class GetHotelsQueryHandlerTest(TestCase):
    def setUp(self):
        self.__in_memory_hotel_repository = InMemoryHotelRepository()
        self.__handler = GetHotelsQueryHandler(self.__in_memory_hotel_repository)

    def test_non_existing_hotels_returns_empty_list(self) -> None:
        query = GetHotelsQuery()

        self.assertEqual([], self.__handler(query))

    def test_all_hotels_are_returned(self) -> None:
        self.__in_memory_hotel_repository.save(
            StubHotelBuilder()
            .with_uuid(hotel_uuid := uuid4())
            .with_name("Name")
            .with_location("Location")
            .with_description("Description")
            .with_has_swimming_pool(False)
            .build()
        )
        self.__in_memory_hotel_repository.save(
            StubHotelBuilder()
            .with_uuid(hotel_two_uuid := uuid4())
            .with_name("Name 2")
            .with_location("Location 2")
            .with_description("Description 2")
            .with_has_swimming_pool(True)
            .build()
        )

        query = GetHotelsQuery()

        hotels = self.__handler(query)

        self.assertEqual(2, len(hotels))

        self.assertEqual(hotel_uuid, hotels[0].uuid)
        self.assertEqual("Name", hotels[0].name)
        self.assertEqual("Location", hotels[0].location)
        self.assertEqual("Description", hotels[0].description)
        self.assertFalse(hotels[0].has_swimming_pool)

        self.assertEqual(hotel_two_uuid, hotels[1].uuid)
        self.assertEqual("Name 2", hotels[1].name)
        self.assertEqual("Location 2", hotels[1].location)
        self.assertEqual("Description 2", hotels[1].description)
        self.assertTrue(hotels[1].has_swimming_pool)
