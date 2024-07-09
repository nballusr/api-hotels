import contextlib
import inspect
import typing

from dependency_injector import containers
from pybuses.foundation import get_subscribed
from pybuses.types import Subscribable, Listener

from src.shared.application.query_handler import QueryHandler
from src.shared.bus.infrastructure.query_bus import QueryBus


class PyBusesQueryBus(QueryBus):
    def __init__(
            self,
            container: containers.Container,
            middlewares: typing.Optional[typing.List[typing.Callable]] = None,
    ):
        if not middlewares:
            middlewares = []

        self.initialized = False
        self.container = container
        self._middlewares = middlewares
        self._handlers: typing.Dict[Subscribable, Listener] = {}

    def handle(self, query) -> typing.Any:
        if not self.initialized:
            self._initialize()

        try:
            handler = self._handlers[type(query)]
        except KeyError:
            raise Exception("No handler for {!r}".format(query))

        with contextlib.ExitStack() as stack:
            for middleware in self._middlewares:
                stack.enter_context(middleware(query))
            res = handler(query)

        return res

    def subscribe(self, listener: Listener) -> None:
        query = get_subscribed(listener)
        if query in self._handlers:
            raise ValueError("{} already has a handler ({})!".format(query, self._handlers[query]))
        self._handlers[query] = listener

    def _register(self, handler) -> None:
        self.subscribe(handler.__call__)

    def _initialize(self) -> None:
        providers = self.container.traverse()
        for provider in providers:
            if hasattr(provider, "cls") and inspect.isclass(provider.cls):
                if issubclass(provider.cls, QueryHandler):
                    self._register(provider())
        self.initialized = True
