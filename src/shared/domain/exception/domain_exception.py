from abc import ABC


class DomainException(Exception, ABC):
    message: str
