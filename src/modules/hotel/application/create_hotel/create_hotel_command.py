from pydantic import BaseModel


class CreateHotelCommand(BaseModel):
    name: str
