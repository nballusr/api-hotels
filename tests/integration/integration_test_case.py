import os
from unittest import TestCase

from sqlalchemy import text
from sqlalchemy.orm import Session

from src.di.container_builder import ContainerBuilder
from src.di.containers import ApplicationContainer
from src.env import load_by_environment


class IntegrationTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        os.chdir(os.getenv("WORKDIR"))
        self.__load_test_environment()
        self.__container = ContainerBuilder.build_container()

    def __load_test_environment(self) -> None:
        load_by_environment("test")

    def container(self) -> ApplicationContainer:
        return self.__container

    def database_session(self) -> Session:
        return self.__container.database_package.db_session()

    def clear_tables(self, tables: list[str]) -> None:
        session = self.database_session()
        session.begin()
        tables_string = ",".join(tables)
        session.execute(text(f"TRUNCATE TABLE {tables_string}"))
        session.commit()

    def tearDown(self) -> None:
        self.__container.database_package.db_session.shutdown()
        super().tearDown()
