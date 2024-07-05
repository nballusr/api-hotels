from dependency_injector import containers, providers
from sqlalchemy.orm import Session

from src.modules.hotel.application.create_hotel.create_hotel_command_handler import CreateHotelCommandHandler
from src.modules.hotel.application.update_hotel.update_hotel_command_handler import UpdateHotelCommandHandler
from src.modules.hotel.domain.write.hotel_repository import HotelRepository
from src.modules.hotel.infrastructure.write.orm_hotel_repository import ORMHotelRepository
from src.modules.hotel.ui.controllers.create_hotel import create_hotel_controller
from src.modules.hotel.ui.controllers.update_hotel import update_hotel_controller
from src.shared.bus.infrastructure.command_bus import CommandBus


class HotelContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[create_hotel_controller, update_hotel_controller],
        auto_wire=False,
    )
    CommandBus = providers.Dependency(instance_of=CommandBus)
    Session = providers.Dependency(instance_of=Session)

    hotel_repository = providers.AbstractSingleton(HotelRepository)
    hotel_repository.override(
        providers.Singleton(
            ORMHotelRepository,
            db=Session,
        )
    )

    create_hotel_command_handler = providers.Singleton(
        CreateHotelCommandHandler,
        hotel_repository=hotel_repository,
    )

    update_hotel_command_handler = providers.Singleton(
        UpdateHotelCommandHandler,
        hotel_repository=hotel_repository,
    )
