from src.di.containers import ApplicationContainer


class ContainerBuilder:
    def __init__(self):
        self.container = None

    @staticmethod
    def build_container() -> ApplicationContainer:
        container = ApplicationContainer()
        container.hotel_package.wire()
        container.check_dependencies()

        return container
