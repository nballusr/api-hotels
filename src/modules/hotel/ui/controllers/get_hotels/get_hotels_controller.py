from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.modules.hotel.application.get_hotels.get_hotels_query import GetHotelsQuery
from src.modules.hotel.ui.controllers.response_models.hotel_response_model import HotelResponseModel
from src.modules.hotel.ui.controllers.get_hotels.get_hotels_response_model import GetHotelsResponseModel
from src.shared.bus.infrastructure.query_bus import QueryBus

router = APIRouter(tags=["hotel"])


@router.get(
    "/hotels",
    summary="Get hotel information of all hotels",
    description="Get hotel information of all hotels.",
    response_model=GetHotelsResponseModel,
    responses={
        200: {"description": "Successful Response", "model": GetHotelsResponseModel},
        500: {"description": "Internal Server Error"},
    },
)
@inject
def get_hotels(
    query_bus: QueryBus = Depends(Provide["QueryBus"]),
) -> GetHotelsResponseModel:
    query = GetHotelsQuery()
    hotels = query_bus.handle(query)

    return GetHotelsResponseModel(
        hotels=[
            HotelResponseModel(
                uuid=hotel.uuid,
                name=hotel.name,
                location=hotel.location,
                description=hotel.description,
                has_swimming_pool=hotel.has_swimming_pool,
            )
            for hotel in hotels
        ]
    )
