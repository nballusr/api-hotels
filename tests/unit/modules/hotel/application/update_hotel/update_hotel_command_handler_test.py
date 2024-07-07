from unittest import TestCase
from uuid import uuid4

from src.modules.hotel.application.update_hotel.update_hotel_command import UpdateHotelCommand
from src.modules.hotel.application.update_hotel.update_hotel_command_handler import UpdateHotelCommandHandler
from src.modules.hotel.domain.exception.hotel_not_found_exception import HotelNotFoundException
from tests.infrastructure.modules.hotel.domain.write.in_memory_hotel_repository import InMemoryHotelRepository
from tests.infrastructure.modules.hotel.domain.write.stub_hotel_builder import StubHotelBuilder


class UpdateHotelCommandHandlerTest(TestCase):
    def setUp(self):
        self.__in_memory_hotel_repository = InMemoryHotelRepository()
        self.__handler = UpdateHotelCommandHandler(self.__in_memory_hotel_repository)

    def test_non_existing_hotel_raises_exception(self) -> None:
        command = UpdateHotelCommand(
            uuid=(uuid := uuid4()),
            name="New name",
            location="New location",
            description="New description",
            has_swimming_pool=True,
        )

        with self.assertRaises(HotelNotFoundException) as e:
            self.__handler(command)

        self.assertEqual(f"Hotel with uuid {uuid} not found", e.exception.message)

    def test_hotel_is_updated(self) -> None:
        self.__in_memory_hotel_repository.save(
            StubHotelBuilder().with_uuid(hotel_uuid := uuid4()).build()
        )

        command = UpdateHotelCommand(
            uuid=hotel_uuid,
            name="New name",
            location="New location",
            description="New description",
            has_swimming_pool=True,
        )

        self.__handler(command)

        retrieved_hotel = self.__in_memory_hotel_repository.of_uuid(hotel_uuid)

        self.assertIsNotNone(retrieved_hotel)
        self.assertEqual(hotel_uuid, retrieved_hotel.uuid)
        self.assertEqual("New name", retrieved_hotel.name)
        self.assertEqual("New location", retrieved_hotel.location)
        self.assertEqual("New description", retrieved_hotel.description)
        self.assertTrue(retrieved_hotel.has_swimming_pool)
