import dataclasses


@dataclasses.dataclass(frozen=False, eq=True)
class NotFoundException(Exception):
    message: str
