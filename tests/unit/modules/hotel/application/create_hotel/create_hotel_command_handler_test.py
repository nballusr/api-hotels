from unittest import TestCase
from unittest.mock import MagicMock

from src.modules.hotel.application.create_hotel.create_hotel_command import CreateHotelCommand
from src.modules.hotel.application.create_hotel.create_hotel_command_handler import CreateHotelCommandHandler
from src.modules.hotel.domain.exception.hotel_already_exists_exception import HotelAlreadyExistsException
from src.modules.hotel.domain.exception.hotel_nof_found_in_booking_exception import HotelNotFoundInBookingException
from src.modules.hotel.domain.service.get_hotel_information_service import GetHotelInformationService, HotelInformation
from tests.infrastructure.modules.hotel.domain.write.in_memory_hotel_repository import InMemoryHotelRepository
from tests.infrastructure.modules.hotel.domain.write.stub_hotel_builder import StubHotelBuilder


class CreateHotelCommandHandlerTest(TestCase):
    def setUp(self):
        self.__mock_service = MagicMock(spec=GetHotelInformationService)
        self.__in_memory_hotel_repository = InMemoryHotelRepository()
        self.__handler = CreateHotelCommandHandler(
            self.__mock_service,
            self.__in_memory_hotel_repository,
        )

    def test_hotel_not_found_in_booking_raises_exception(self) -> None:
        self.__mock_service.from_name.return_value = None

        command = CreateHotelCommand(name=(hotel_name := "Not found name"))

        with self.assertRaises(HotelNotFoundInBookingException) as e:
            self.__handler(command)

        self.assertEqual(f"No hotel found in booking with name {hotel_name}", e.exception.message)

    def test_hotel_with_same_name_already_exists_raises_exception(self) -> None:
        self.__mock_service.from_name.return_value = HotelInformation(
            name="Existing name",
            location="Hotel Location",
            description="Hotel Description",
            has_swimming_pool=True,
        )

        self.__in_memory_hotel_repository.save(
            StubHotelBuilder().with_name(hotel_name := "Existing name").build()
        )

        command = CreateHotelCommand(name="existing name")

        with self.assertRaises(HotelAlreadyExistsException) as e:
            self.__handler(command)

        self.assertEqual(f"Hotel with name {hotel_name} already exists", e.exception.message)

    def test_hotel_is_created(self) -> None:
        self.__mock_service.from_name.return_value = HotelInformation(
            name="New name",
            location="Hotel Location",
            description="Hotel Description",
            has_swimming_pool=True,
        )
        command = CreateHotelCommand(name=(name := "New name"))

        self.__handler(command)

        retrieved_hotel = self.__in_memory_hotel_repository.of_name(name)

        self.assertIsNotNone(retrieved_hotel)
        self.assertEqual("New name", retrieved_hotel.name)
        self.assertEqual("Hotel Location", retrieved_hotel.location)
        self.assertEqual("Hotel Description", retrieved_hotel.description)
        self.assertTrue(retrieved_hotel.has_swimming_pool)
