from uuid import uuid4

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.modules.hotel.application.create_hotel.create_hotel_command import CreateHotelCommand
from src.modules.hotel.application.get_hotel.get_hotel_query import GetHotelQuery
from src.modules.hotel.ui.controllers.response_models.custom_exception_response_model import \
    CustomExceptionResponseModel
from src.modules.hotel.ui.controllers.response_models.hotel_response_model import HotelResponseModel
from src.shared.bus.infrastructure.command_bus import CommandBus
from src.shared.bus.infrastructure.query_bus import QueryBus

router = APIRouter(tags=["hotel"])


class CreateHotelRequestModel(BaseModel):
    name: str


@router.post(
    "/hotels/scrape",
    summary="Create hotel based on information in Booking.com",
    description="Create a hotel. It takes the hotel information from Booking.com based on the given name, "
                "stores the information and returns it.",
    response_model=HotelResponseModel,
    responses={
        200: {"description": "Successful Response", "model": HotelResponseModel},
        400: {"description": "Bad Request", "model": CustomExceptionResponseModel},
        404: {"description": "Not Found", "model": CustomExceptionResponseModel},
        500: {"description": "Internal Server Error"},
    },
)
@inject
def post_hotel(
        request: CreateHotelRequestModel,
        command_bus: CommandBus = Depends(Provide["CommandBus"]),
        query_bus: QueryBus = Depends(Provide["QueryBus"]),
) -> HotelResponseModel:
    uuid = uuid4()
    command = CreateHotelCommand(
        uuid=uuid,
        name=request.name,
    )
    command_bus.handle(command)

    query = GetHotelQuery(uuid=uuid)
    hotel = query_bus.handle(query)

    return HotelResponseModel(
        uuid=hotel.uuid,
        name=hotel.name,
        location=hotel.location,
        description=hotel.description,
        has_swimming_pool=hotel.has_swimming_pool,
    )
