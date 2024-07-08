from dependency_injector import containers, providers
from sqlalchemy.orm import Session

from src.modules.hotel.application.create_hotel.create_hotel_command_handler import CreateHotelCommandHandler
from src.modules.hotel.application.get_hotel.get_hotel_query_handler import GetHotelQueryHandler
from src.modules.hotel.application.get_hotels.get_hotels_query_handler import GetHotelsQueryHandler
from src.modules.hotel.application.remove_hotel.remove_hotel_command_handler import RemoveHotelCommandHandler
from src.modules.hotel.application.update_hotel.update_hotel_command_handler import UpdateHotelCommandHandler
from src.modules.hotel.domain.read.hotel_repository import HotelRepository as ReadHotelRepository
from src.modules.hotel.domain.service.get_hotel_information_service import GetHotelInformationService
from src.modules.hotel.domain.write.hotel_repository import HotelRepository
from src.modules.hotel.infrastructure.read.sql_hotel_repository import SQLHotelRepository
from src.modules.hotel.infrastructure.service.http_booking_get_hotel_information_service import \
    HttpBookingGetHotelInformationService
from src.modules.hotel.infrastructure.write.orm_hotel_repository import ORMHotelRepository
from src.modules.hotel.ui.controllers.create_hotel import create_hotel_controller
from src.modules.hotel.ui.controllers.get_hotel import get_hotel_controller
from src.modules.hotel.ui.controllers.get_hotels import get_hotels_controller
from src.modules.hotel.ui.controllers.remove_hotel import remove_hotel_controller
from src.modules.hotel.ui.controllers.update_hotel import update_hotel_controller
from src.shared.bus.infrastructure.command_bus import CommandBus
from src.shared.bus.infrastructure.query_bus import QueryBus


class HotelContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            create_hotel_controller,
            update_hotel_controller,
            remove_hotel_controller,
            get_hotel_controller,
            get_hotels_controller
        ],
        auto_wire=False,
    )
    CommandBus = providers.Dependency(instance_of=CommandBus)
    QueryBus = providers.Dependency(instance_of=QueryBus)
    Session = providers.Dependency(instance_of=Session)

    hotel_repository = providers.AbstractSingleton(HotelRepository)
    hotel_repository.override(
        providers.Singleton(
            ORMHotelRepository,
            db=Session,
        )
    )

    read_hotel_repository = providers.AbstractSingleton(ReadHotelRepository)
    read_hotel_repository.override(
        providers.Singleton(
            SQLHotelRepository,
            db=Session,
        )
    )

    get_hotel_information_service = providers.AbstractSingleton(GetHotelInformationService)
    get_hotel_information_service.override(
        providers.Singleton(
            HttpBookingGetHotelInformationService,
        )
    )

    create_hotel_command_handler = providers.Singleton(
        CreateHotelCommandHandler,
        get_hotel_information_service=get_hotel_information_service,
        hotel_repository=hotel_repository,
    )

    update_hotel_command_handler = providers.Singleton(
        UpdateHotelCommandHandler,
        hotel_repository=hotel_repository,
    )

    remove_hotel_command_handler = providers.Singleton(
        RemoveHotelCommandHandler,
        hotel_repository=hotel_repository,
    )

    get_hotel_query_handler = providers.Singleton(
        GetHotelQueryHandler,
        hotel_repository=read_hotel_repository,
    )

    get_hotels_query_handler = providers.Singleton(
        GetHotelsQueryHandler,
        hotel_repository=read_hotel_repository,
    )
