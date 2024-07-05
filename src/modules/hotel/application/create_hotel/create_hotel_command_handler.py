import os

from src.modules.hotel.application.create_hotel.create_hotel_command import CreateHotelCommand
from src.shared.application.command_handler import CommandHandler


class CreateHotelCommandHandler(CommandHandler):
    def __init__(self, db_session):
        self.__db = db_session
    def __call__(self, command: CreateHotelCommand) -> None:
        print("Testing database: ", self.__db.get_transaction())
