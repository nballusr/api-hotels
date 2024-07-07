from uuid import UUID

from fastapi import APIRouter

router = APIRouter(tags=["hotel"])


@router.delete("/hotels/{hotel_uuid}")
def remove_hotel(hotel_uuid: UUID) -> None:
    pass
