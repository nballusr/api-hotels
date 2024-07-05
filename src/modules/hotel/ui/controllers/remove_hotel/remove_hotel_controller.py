from uuid import UUID

from fastapi import APIRouter

router = APIRouter(tags=["hotel"])


@router.delete("/hotels/{hotel_uuid}")
def put_hotel(hotel_uuid: UUID) -> None:
    pass
