from src.modules.hotel.application.remove_hotel.remove_hotel_command import RemoveHotelCommand
from src.modules.hotel.domain.exception.hotel_not_found_exception import HotelNotFoundException
from src.modules.hotel.domain.write.hotel_repository import HotelRepository
from src.shared.application.command_handler import CommandHandler


class RemoveHotelCommandHandler(CommandHandler):
    def __init__(self, hotel_repository: HotelRepository):
        self.__hotel_repository = hotel_repository

    def __call__(self, command: RemoveHotelCommand) -> None:
        existing_hotel = self.__hotel_repository.of_uuid(command.uuid)
        if existing_hotel is None:
            raise HotelNotFoundException.create(command.uuid)

        self.__hotel_repository.remove(existing_hotel)
