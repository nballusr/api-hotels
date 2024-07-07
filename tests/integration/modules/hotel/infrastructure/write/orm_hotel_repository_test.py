from uuid import uuid4

from src.modules.hotel.domain.write.hotel import Hotel
from src.modules.hotel.infrastructure.write.orm_hotel_repository import ORMHotelRepository
from tests.infrastructure.modules.hotel.domain.write.stub_hotel_builder import StubHotelBuilder
from tests.integration.integration_test_case import IntegrationTestCase


class ORMHotelRepositoryTest(IntegrationTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.clear_tables(["hotel"])
        self.__repository: ORMHotelRepository = self.container().hotel_package.hotel_repository()
        self.__session = self.database_session()

    def test_save_for_first_time(self) -> None:
        hotel = StubHotelBuilder().build()
        self.__repository.save(hotel)
        self.__session.flush()
        self.__session.expunge_all()

        hotels = self.database_session().query(Hotel).all()
        self.assertEqual(1, len(hotels))

    def test_save_existing_hotel(self) -> None:
        hotel = StubHotelBuilder().build()
        self.database_session().add(hotel)
        self.__session.flush()
        self.__session.expunge_all()

        self.__repository.save(hotel)
        self.__session.flush()
        self.__session.expunge_all()

        hotels = self.database_session().query(Hotel).all()
        self.assertEqual(1, len(hotels))

    def test_of_name_returns_none_if_any_hotel_matches(self) -> None:
        self.assertIsNone(self.__repository.of_name("No existing"))

    def test_of_name_returns_matching_hotel(self) -> None:
        hotel = StubHotelBuilder().with_name("Existing").build()
        self.database_session().add(hotel)
        self.__session.flush()
        self.__session.expunge_all()

        retrieved_hotel = self.__repository.of_name("Existing")

        self.assertIsNotNone(retrieved_hotel)
        self.assertIsInstance(retrieved_hotel, Hotel)

    def test_of_uuid_returns_none_if_any_hotel_matches(self) -> None:
        self.assertIsNone(self.__repository.of_uuid(uuid4()))

    def test_of_uuid_returns_matching_hotel(self) -> None:
        hotel = StubHotelBuilder().with_uuid(uuid := uuid4()).build()
        self.database_session().add(hotel)
        self.__session.flush()
        self.__session.expunge_all()

        retrieved_hotel = self.__repository.of_uuid(uuid)

        self.assertIsNotNone(retrieved_hotel)
        self.assertIsInstance(retrieved_hotel, Hotel)

    def test_remove_hotel(self) -> None:
        hotel = StubHotelBuilder().build()
        self.__session.add(hotel)
        self.__session.flush()
        self.__session.expunge_all()

        self.__repository.remove(hotel)
        self.__session.flush()
        self.__session.expunge_all()

        hotels = self.database_session().query(Hotel).all()
        self.assertEqual(0, len(hotels))
