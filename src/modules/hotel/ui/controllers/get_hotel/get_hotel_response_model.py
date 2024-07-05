from uuid import UUID

from pydantic import BaseModel

class GetHotelResponseModel(BaseModel):
    uuid: UUID
    name: str
    location: str
    description: str
    has_swimming_pool: bool
