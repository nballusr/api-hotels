from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.modules.hotel.application.remove_hotel.remove_hotel_command import RemoveHotelCommand
from src.shared.bus.infrastructure.command_bus import CommandBus

router = APIRouter(tags=["hotel"])


@router.delete("/hotels/{hotel_uuid}")
@inject
def remove_hotel(
        hotel_uuid: UUID,
        command_bus: CommandBus = Depends(Provide["CommandBus"]),
) -> None:
    command = RemoveHotelCommand(uuid=hotel_uuid)
    command_bus.handle(command)
