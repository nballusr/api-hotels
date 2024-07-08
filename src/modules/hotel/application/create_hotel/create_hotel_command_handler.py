from src.modules.hotel.application.create_hotel.create_hotel_command import CreateHotelCommand
from src.modules.hotel.domain.exception.hotel_already_exists_exception import HotelAlreadyExistsException
from src.modules.hotel.domain.exception.hotel_nof_found_in_booking_exception import HotelNotFoundInBookingException
from src.modules.hotel.domain.service.get_hotel_information_service import GetHotelInformationService
from src.modules.hotel.domain.write.hotel import Hotel
from src.modules.hotel.domain.write.hotel_repository import HotelRepository
from src.shared.application.command_handler import CommandHandler


class CreateHotelCommandHandler(CommandHandler):
    def __init__(self, get_hotel_information_service: GetHotelInformationService, hotel_repository: HotelRepository):
        self.__get_hotel_information_service = get_hotel_information_service
        self.__hotel_repository = hotel_repository

    def __call__(self, command: CreateHotelCommand) -> None:
        existing_hotel_with_uuid = self.__hotel_repository.of_uuid(command.uuid)
        if existing_hotel_with_uuid is not None:
            raise HotelAlreadyExistsException.of_uuid(command.uuid)

        hotel_information = self.__get_hotel_information_service.from_name(command.name)
        if hotel_information is None:
            raise HotelNotFoundInBookingException.create(command.name)

        existing_hotel_with_name = self.__hotel_repository.of_name(hotel_information.name)
        if existing_hotel_with_name is not None:
            raise HotelAlreadyExistsException.of_name(hotel_information.name)

        hotel = Hotel(
            uuid=command.uuid,
            name=hotel_information.name,
            location=hotel_information.location,
            description=hotel_information.description,
            has_swimming_pool=hotel_information.has_swimming_pool,
        )
        self.__hotel_repository.save(hotel)
