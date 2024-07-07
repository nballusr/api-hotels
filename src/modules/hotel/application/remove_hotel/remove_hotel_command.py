from uuid import UUID

from pydantic import BaseModel


class RemoveHotelCommand(BaseModel):
    uuid: UUID
