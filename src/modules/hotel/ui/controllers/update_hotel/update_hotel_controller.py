from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.modules.hotel.application.update_hotel.update_hotel_command import UpdateHotelCommand
from src.shared.bus.infrastructure.command_bus import CommandBus

router = APIRouter(tags=["hotel"])


class ReplaceHotelRequestModel(BaseModel):
    name: str
    name: str
    location: str
    description: str
    has_swimming_pool: bool


@router.put("/hotels/{hotel_uuid}")
@inject
def put_hotel(
    hotel_uuid: UUID,
    request: ReplaceHotelRequestModel,
    command_bus: CommandBus = Depends(Provide["CommandBus"]),
) -> None:
    command = UpdateHotelCommand(
        uuid=hotel_uuid,
        name=request.name,
        location=request.location,
        description=request.description,
        has_swimming_pool=request.has_swimming_pool,
    )
    command_bus.handle(command)
