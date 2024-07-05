from uuid import UUID

from pydantic import BaseModel


class GetHotelQuery(BaseModel):
    uuid: UUID
