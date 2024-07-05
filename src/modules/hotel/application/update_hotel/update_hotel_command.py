from uuid import UUID

from pydantic import BaseModel


class UpdateHotelCommand(BaseModel):
    uuid: UUID
    name: str
    location: str
    description: str
    has_swimming_pool: bool
