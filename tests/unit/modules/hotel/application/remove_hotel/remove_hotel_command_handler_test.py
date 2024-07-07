from unittest import TestCase
from uuid import uuid4

from src.modules.hotel.application.remove_hotel.remove_hotel_command import RemoveHotelCommand
from src.modules.hotel.application.remove_hotel.remove_hotel_command_handler import RemoveHotelCommandHandler
from src.modules.hotel.domain.exception.hotel_not_found_exception import HotelNotFoundException
from tests.infrastructure.modules.hotel.domain.write.in_memory_hotel_repository import InMemoryHotelRepository
from tests.infrastructure.modules.hotel.domain.write.stub_hotel_builder import StubHotelBuilder


class RemoveHotelCommandHandlerTest(TestCase):
    def setUp(self):
        self.__in_memory_hotel_repository = InMemoryHotelRepository()
        self.__handler = RemoveHotelCommandHandler(self.__in_memory_hotel_repository)

    def test_non_existing_hotel_raises_exception(self) -> None:
        command = RemoveHotelCommand(uuid=(uuid := uuid4()))

        with self.assertRaises(HotelNotFoundException) as e:
            self.__handler(command)

        self.assertEqual(f"Hotel with uuid {uuid} not found", e.exception.message)

    def test_hotel_is_removed(self) -> None:
        self.__in_memory_hotel_repository.save(
            StubHotelBuilder().with_uuid(hotel_uuid := uuid4()).build()
        )

        command = RemoveHotelCommand(uuid=hotel_uuid)
        self.__handler(command)

        retrieved_hotel = self.__in_memory_hotel_repository.of_uuid(hotel_uuid)
        self.assertIsNone(retrieved_hotel)
