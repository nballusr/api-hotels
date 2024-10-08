import pybuses
from dependency_injector import containers, providers

from src.shared.bus.infrastructure.command_bus import CommandBus
from src.shared.bus.infrastructure.pybuses_command_bus import PyBusesCommandBus
from src.shared.bus.infrastructure.pybuses_query_bus import PyBusesQueryBus
from src.shared.bus.infrastructure.query_bus import QueryBus


class BusesContainer(containers.DeclarativeContainer):
    __self__ = providers.Self()
    middlewares = providers.Dependency()
    # Default to empty list
    middlewares.override(providers.List())
    CommandBus = providers.AbstractSingleton(CommandBus)
    CommandBus.override(
        providers.Singleton(
            PyBusesCommandBus,
            bus=providers.Singleton(
                pybuses.CommandBus,
                middlewares=middlewares,
            ),
            container=__self__,
        )
    )

    query_bus_middlewares = middlewares
    QueryBus = providers.AbstractSingleton(QueryBus)
    QueryBus.override(
        providers.Singleton(
            PyBusesQueryBus,
            middlewares=query_bus_middlewares,
            container=__self__,
        )
    )
