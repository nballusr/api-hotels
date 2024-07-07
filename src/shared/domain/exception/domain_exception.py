import dataclasses
from abc import ABC


@dataclasses.dataclass(frozen=False, eq=True)
class DomainException(Exception, ABC):
    message: str
