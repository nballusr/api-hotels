from src.modules.hotel.application.update_hotel.update_hotel_command import UpdateHotelCommand
from src.modules.hotel.domain.exception.hotel_already_exists_exception import HotelAlreadyExistsException
from src.modules.hotel.domain.exception.hotel_not_found_exception import HotelNotFoundException
from src.modules.hotel.domain.write.hotel_repository import HotelRepository
from src.shared.application.command_handler import CommandHandler


class UpdateHotelCommandHandler(CommandHandler):
    def __init__(self, hotel_repository: HotelRepository):
        self.__hotel_repository = hotel_repository

    def __call__(self, command: UpdateHotelCommand) -> None:
        existing_hotel = self.__hotel_repository.of_uuid(command.uuid)
        if existing_hotel is None:
            raise HotelNotFoundException.create(command.uuid)

        if existing_hotel.name != command.name:
            hotel_with_same_name = self.__hotel_repository.of_name(command.name)
            if hotel_with_same_name is not None:
                raise HotelAlreadyExistsException.of_name(command.name)

        existing_hotel.update(
            name=command.name,
            location=command.location,
            description=command.description,
            has_swimming_pool=command.has_swimming_pool,
        )
        self.__hotel_repository.save(existing_hotel)
