from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.modules.hotel.application.remove_hotel.remove_hotel_command import RemoveHotelCommand
from src.modules.hotel.ui.controllers.response_models.custom_exception_response_model import \
    CustomExceptionResponseModel
from src.shared.bus.infrastructure.command_bus import CommandBus

router = APIRouter(tags=["hotel"])


@router.delete(
    "/hotels/{hotel_uuid}",
    summary="Remove hotel by uuid",
    description="Remove hotel by uuid.",
    responses={
        200: {"description": "Successful Response"},
        404: {"description": "Not Found", "model": CustomExceptionResponseModel},
        500: {"description": "Internal Server Error"},
    },
)
@inject
def remove_hotel(
        hotel_uuid: UUID,
        command_bus: CommandBus = Depends(Provide["CommandBus"]),
) -> None:
    command = RemoveHotelCommand(uuid=hotel_uuid)
    command_bus.handle(command)
