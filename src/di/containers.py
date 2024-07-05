import glob
import os

from dependency_injector import containers, providers
from dependency_injector.containers import Container
from src.shared.bus.di.containers import BusesContainer

from src.modules.hotel.di.containers import HotelContainer


class ApplicationContainer(containers.DeclarativeContainer):
    __self__ = providers.Self()
    app_config = providers.Configuration(
        "application",
        strict=True,
        yaml_files=[
          *glob.glob(os.getenv("WORKDIR") + "/config/*.yaml"),
          *glob.glob(os.getenv("WORKDIR") + "/config/*.yml"),
        ],
    )

    middlewares = providers.List()
    buses_package: BusesContainer | Container = providers.Container(
        BusesContainer,
        __self__=__self__,
        middlewares=middlewares,
    )

    hotel_package: HotelContainer | Container = providers.Container(
        HotelContainer,
        CommandBus=buses_package.CommandBus,
    )
