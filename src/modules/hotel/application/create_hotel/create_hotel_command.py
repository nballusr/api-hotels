from uuid import UUID

from pydantic import BaseModel


class CreateHotelCommand(BaseModel):
    name: str
