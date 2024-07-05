from uuid import uuid4

from fastapi import APIRouter

from src.modules.hotel.ui.controllers.get_hotel.get_hotel_response_model import GetHotelResponseModel

router = APIRouter(tags=["hotel"])


@router.get("/hotels", response_model=list[GetHotelResponseModel])
def get_hotels(
) -> list[GetHotelResponseModel]:
    return [
        GetHotelResponseModel(
            uuid=uuid4(),
            name="Test name",
            location="C/ Test",
            description="Test description",
            has_swimming_pool=False,
        ),
        GetHotelResponseModel(
            uuid=uuid4(),
            name="Test name 2",
            location="C/ Test 2",
            description="Test description 2",
            has_swimming_pool=False,
        ),
    ]
