from uuid import UUID

from pydantic import BaseModel


class CreateHotelCommand(BaseModel):
    uuid: UUID
    name: str
