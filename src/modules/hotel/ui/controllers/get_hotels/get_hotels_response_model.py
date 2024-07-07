from pydantic import BaseModel

from src.modules.hotel.ui.controllers.get_hotel.get_hotel_response_model import GetHotelResponseModel


class GetHotelsResponseModel(BaseModel):
    hotels: list[GetHotelResponseModel]
