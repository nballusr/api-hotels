from uuid import uuid4

from src.modules.hotel.infrastructure.read.sql_hotel_repository import SQLHotelRepository
from tests.infrastructure.modules.hotel.domain.write.stub_hotel_builder import StubHotelBuilder
from tests.integration.integration_test_case import IntegrationTestCase


class SQLHotelRepositoryTest(IntegrationTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.clear_tables(["hotel"])
        self.__repository: SQLHotelRepository = self.container().hotel_package.read_hotel_repository()
        self.__session = self.database_session()

    def test_of_uuid_returns_none_if_any_hotel_matches(self) -> None:
        self.assertIsNone(self.__repository.of_uuid(uuid4()))

    def test_of_uuid_returns_matching_hotel(self) -> None:
        hotel = (
            StubHotelBuilder()
            .with_uuid(uuid := uuid4())
            .with_name("Name")
            .with_location("Location")
            .with_description("Description")
            .with_has_swimming_pool(True)
            .build()
        )
        self.database_session().add(hotel)
        self.__session.flush()
        self.__session.expunge_all()

        retrieved_hotel = self.__repository.of_uuid(uuid)

        self.assertIsNotNone(retrieved_hotel)
        self.assertEqual(uuid, retrieved_hotel.uuid)
        self.assertEqual("Name", retrieved_hotel.name)
        self.assertEqual("Location", retrieved_hotel.location)
        self.assertEqual("Description", retrieved_hotel.description)
        self.assertTrue(retrieved_hotel.has_swimming_pool)

    def test_all_returns_empty_list_if_no_hotels(self) -> None:
        self.assertEqual([], self.__repository.all())

    def test_all_returns_list_of_hotels(self) -> None:
        hotel_one = (
            StubHotelBuilder()
            .with_uuid(uuid_one := uuid4())
            .with_name("Name")
            .with_location("Location")
            .with_description("Description")
            .with_has_swimming_pool(True)
            .build()
        )
        hotel_two = (
            StubHotelBuilder()
            .with_uuid(uuid_two := uuid4())
            .with_name("Name 2")
            .with_location("Location 2")
            .with_description("Description 2")
            .with_has_swimming_pool(False)
            .build()
        )
        self.database_session().add(hotel_one)
        self.database_session().add(hotel_two)
        self.__session.flush()
        self.__session.expunge_all()

        retrieved_hotels = self.__repository.all()

        self.assertEqual(2, len(retrieved_hotels))

        self.assertEqual(uuid_one, retrieved_hotels[0].uuid)
        self.assertEqual("Name", retrieved_hotels[0].name)
        self.assertEqual("Location", retrieved_hotels[0].location)
        self.assertEqual("Description", retrieved_hotels[0].description)
        self.assertTrue(retrieved_hotels[0].has_swimming_pool)

        self.assertEqual(uuid_two, retrieved_hotels[1].uuid)
        self.assertEqual("Name 2", retrieved_hotels[1].name)
        self.assertEqual("Location 2", retrieved_hotels[1].location)
        self.assertEqual("Description 2", retrieved_hotels[1].description)
        self.assertFalse(retrieved_hotels[1].has_swimming_pool)
