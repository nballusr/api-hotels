from unittest import TestCase

from src.modules.hotel.application.create_hotel.create_hotel_command import CreateHotelCommand
from src.modules.hotel.application.create_hotel.create_hotel_command_handler import CreateHotelCommandHandler
from src.modules.hotel.domain.exception.hotel_already_exists_exception import HotelAlreadyExistsException
from tests.infrastructure.modules.hotel.domain.write.in_memory_hotel_repository import InMemoryHotelRepository
from tests.infrastructure.modules.hotel.domain.write.stub_hotel_builder import StubHotelBuilder


class CreateHotelCommandHandlerTest(TestCase):
    def setUp(self):
        self.__in_memory_hotel_repository = InMemoryHotelRepository()
        self.__handler = CreateHotelCommandHandler(self.__in_memory_hotel_repository)

    def test_hotel_with_same_name_already_exists_throws_exception(self) -> None:
        self.__in_memory_hotel_repository.save(
            StubHotelBuilder().with_name(hotel_name := "Existing name").build()
        )

        command = CreateHotelCommand(name=hotel_name)

        with self.assertRaises(HotelAlreadyExistsException) as e:
            self.__handler(command)

        self.assertEqual(f"Hotel with name {hotel_name} already exists", e.exception.message)

    def test_hotel_is_created(self) -> None:
        command = CreateHotelCommand(name=(name := "New name"))

        self.__handler(command)

        retrieved_hotel = self.__in_memory_hotel_repository.of_name(name)

        self.assertIsNotNone(retrieved_hotel)
        self.assertEqual(name, retrieved_hotel.name)
