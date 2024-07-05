from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["hotel"])


class ReplaceHotelRequestModel(BaseModel):
    name: str
    name: str
    location: str
    description: str
    has_swimming_pool: bool


@router.put("/hotels/{hotel_uuid}")
def put_hotel(
        hotel_uuid: UUID,
        request: ReplaceHotelRequestModel,
) -> None:
    pass
