from uuid import UUID

from pydantic import BaseModel


class Hotel(BaseModel):
    uuid: UUID
    name: str
    location: str
    description: str
    has_swimming_pool: bool
