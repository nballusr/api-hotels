from dependency_injector import containers, providers
from sqlalchemy.orm import Session

from src.modules.hotel.application.create_hotel.create_hotel_command_handler import CreateHotelCommandHandler
from src.modules.hotel.ui.controllers.create_hotel import create_hotel_controller
from src.shared.bus.infrastructure.command_bus import CommandBus


class HotelContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[create_hotel_controller],
        auto_wire=False,
    )
    CommandBus = providers.Dependency(instance_of=CommandBus)
    Session = providers.Dependency(instance_of=Session)

    create_hotel_command_handler = providers.Singleton(
        CreateHotelCommandHandler,
        db_session=Session,
    )
