from src.modules.hotel.application.create_hotel.create_hotel_command import CreateHotelCommand
from src.shared.application.command_handler import CommandHandler


class CreateHotelCommandHandler(CommandHandler):
    def __call__(self, command: CreateHotelCommand) -> None:
        pass
