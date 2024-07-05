from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.modules.hotel.application.create_hotel.create_hotel_command import CreateHotelCommand
from src.shared.bus.infrastructure.command_bus import CommandBus

router = APIRouter(tags=["hotel"])


class CreateHotelRequestModel(BaseModel):
    name: str

@router.post("/hotels/scrape")
@inject
def put_hotel(
    hotel_uuid: UUID,
    request: CreateHotelRequestModel,
    command_bus: CommandBus = Depends(Provide["CommandBus"]),
) -> None:
    command = CreateHotelCommand(
        uuid=hotel_uuid,
        name=request.name,
    )
    command_bus.handle(command)
