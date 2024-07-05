import os
from typing import Generator, Any

from dependency_injector import containers, providers, resources
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.shared.database.infrastructure.flush_database_transaction_middleware import (
    FlushDatabaseTransactionMiddleware,
)


def url_is_sqlite(url):
    return url.startswith("sqlite")


def connection_arguments(url):
    is_sqlite = url_is_sqlite(url)
    return {"check_same_thread": False} if is_sqlite else {}


def get_db_session(session_local: sessionmaker) -> Generator[Session, Any, None]:
    db: Session = session_local()
    try:
        yield db
    finally:
        db.close()


class DBResource(resources.Resource):
    def init(self, session_local: sessionmaker) -> Session:
        db = session_local()
        return db

    def shutdown(self, resource: Session) -> None:
        resource.close()


class DatabaseContainer(containers.DeclarativeContainer):
    config = providers.Configuration("database", strict=True)
    connect_args = providers.Callable(
        connection_arguments,
        url=config.dal.connections.relational.url,
    )
    engine = providers.Singleton(
        create_engine,
        config.dal.connections.relational.url,
        connect_args=connect_args,
    )
    session_local = providers.Factory(sessionmaker, autocommit=False, autoflush=False, bind=engine)
    db_session = providers.Resource(DBResource, session_local=session_local)

    flush_middleware = providers.Singleton(
        FlushDatabaseTransactionMiddleware,
        session=db_session,
    )
