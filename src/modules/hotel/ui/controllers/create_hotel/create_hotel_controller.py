from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["hotel"])


class CreateHotelRequestModel(BaseModel):
    name: str

@router.post("/hotels/scrape")
def put_hotel(
    hotel_uuid: UUID,
    request: CreateHotelRequestModel,
) -> None:
    pass
