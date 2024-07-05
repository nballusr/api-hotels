from contextlib import contextmanager
from typing import Generator

from sqlalchemy.orm import Session


class FlushDatabaseTransactionMiddleware:
    def __init__(self, session: Session):
        self.__session = session

    @contextmanager
    def __call__(self, command) -> Generator:
        # Before handling
        self.__session.begin()
        try:
            yield
        except Exception as e:
            self.__session.rollback()
            raise e
        else:
            # After handling
            self.__session.flush()
            self.__session.commit()
