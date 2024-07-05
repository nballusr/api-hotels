from uuid import UUID, uuid4

from fastapi import APIRouter

from src.modules.hotel.ui.controllers.get_hotel.get_hotel_response_model import GetHotelResponseModel

router = APIRouter(tags=["hotel"])


@router.get("/hotels/{hotel_uuid}", response_model=GetHotelResponseModel)
def get_hotel(
    hotel_uuid: UUID,
) -> GetHotelResponseModel:
    return GetHotelResponseModel(
        uuid=uuid4(),
        name="Test name",
        location="C/ Test",
        description="Test description",
        has_swimming_pool=False,
    )
