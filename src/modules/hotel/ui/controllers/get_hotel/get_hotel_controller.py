from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.modules.hotel.application.get_hotel.get_hotel_query import GetHotelQuery
from src.modules.hotel.ui.controllers.response_models.custom_exception_response_model import \
    CustomExceptionResponseModel
from src.modules.hotel.ui.controllers.response_models.hotel_response_model import HotelResponseModel
from src.shared.bus.infrastructure.query_bus import QueryBus

router = APIRouter(tags=["hotel"])


@router.get(
    "/hotels/{hotel_uuid}",
    summary="Get hotel information by uuid",
    description="Get hotel information by uuid.",
    response_model=HotelResponseModel,
    responses={
        200: {"description": "Successful Response", "model": HotelResponseModel},
        404: {"description": "Not Found", "model": CustomExceptionResponseModel},
        500: {"description": "Internal Server Error"},
    },
)
@inject
def get_hotel(
    hotel_uuid: UUID,
    query_bus: QueryBus = Depends(Provide["QueryBus"]),
) -> HotelResponseModel:
    query = GetHotelQuery(uuid=hotel_uuid)
    hotel = query_bus.handle(query)

    return HotelResponseModel(
        uuid=hotel.uuid,
        name=hotel.name,
        location=hotel.location,
        description=hotel.description,
        has_swimming_pool=hotel.has_swimming_pool,
    )
