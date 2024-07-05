import inspect

from dependency_injector import containers
from pybuses import CommandBus as NativeCommandBus

from src.shared.application.command_handler import CommandHandler
from src.shared.bus.infrastructure.command_bus import CommandBus


class PybusesCommandBus(CommandBus):
    def __init__(self, bus: NativeCommandBus, container: containers.Container):
        self.bus = bus
        self.container = container
        self.initialized = False

    def handle(self, command) -> None:
        if not self.initialized:
            self._initialize()

        self.bus.handle(command)

    def _register(self, handler) -> None:
        self.bus.subscribe(handler.__call__)

    def _initialize(self) -> None:
        providers = self.container.traverse()
        for provider in providers:
            if hasattr(provider, "cls") and inspect.isclass(provider.cls):
                if issubclass(provider.cls, CommandHandler):
                    self._register(provider())
        self.initialized = True
