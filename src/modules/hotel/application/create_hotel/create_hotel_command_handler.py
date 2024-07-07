from uuid import uuid4

from src.modules.hotel.application.create_hotel.create_hotel_command import CreateHotelCommand
from src.modules.hotel.domain.exception.hotel_already_exists_exception import HotelAlreadyExistsException
from src.modules.hotel.domain.write.hotel import Hotel
from src.modules.hotel.domain.write.hotel_repository import HotelRepository
from src.shared.application.command_handler import CommandHandler


class CreateHotelCommandHandler(CommandHandler):
    def __init__(self, hotel_repository: HotelRepository):
        self.__hotel_repository = hotel_repository

    def __call__(self, command: CreateHotelCommand) -> None:
        existing_hotel = self.__hotel_repository.of_name(command.name)
        if existing_hotel is not None:
            raise HotelAlreadyExistsException.create(command.name)

        hotel = Hotel(
            uuid=uuid4(),
            name=command.name,
            location="location",
            description="description",
            has_swimming_pool=False
        )
        self.__hotel_repository.save(hotel)
