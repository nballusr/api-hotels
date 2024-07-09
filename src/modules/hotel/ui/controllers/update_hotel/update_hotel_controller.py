from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.modules.hotel.application.get_hotel.get_hotel_query import GetHotelQuery
from src.modules.hotel.application.update_hotel.update_hotel_command import UpdateHotelCommand
from src.modules.hotel.ui.controllers.response_models.custom_exception_response_model import \
    CustomExceptionResponseModel
from src.modules.hotel.ui.controllers.response_models.hotel_response_model import HotelResponseModel
from src.shared.bus.infrastructure.command_bus import CommandBus
from src.shared.bus.infrastructure.query_bus import QueryBus

router = APIRouter(tags=["hotel"])


class UpdateHotelRequestModel(BaseModel):
    name: str
    name: str
    location: str
    description: str
    has_swimming_pool: bool


@router.put(
    "/hotels/{hotel_uuid}",
    summary="Update hotel information by uuid",
    description="Update hotel information by uuid.",
    response_model=HotelResponseModel,
    responses={
        200: {"description": "Successful Response", "model": HotelResponseModel},
        400: {"description": "Bad Request", "model": CustomExceptionResponseModel},
        404: {"description": "Not Found", "model": CustomExceptionResponseModel},
        500: {"description": "Internal Server Error"},
    },
)
@inject
def put_hotel(
    hotel_uuid: UUID,
    request: UpdateHotelRequestModel,
    command_bus: CommandBus = Depends(Provide["CommandBus"]),
    query_bus: QueryBus = Depends(Provide["QueryBus"]),
) -> HotelResponseModel:
    command = UpdateHotelCommand(
        uuid=hotel_uuid,
        name=request.name,
        location=request.location,
        description=request.description,
        has_swimming_pool=request.has_swimming_pool,
    )
    command_bus.handle(command)

    query = GetHotelQuery(uuid=hotel_uuid)
    hotel = query_bus.handle(query)

    return HotelResponseModel(
        uuid=hotel.uuid,
        name=hotel.name,
        location=hotel.location,
        description=hotel.description,
        has_swimming_pool=hotel.has_swimming_pool,
    )
