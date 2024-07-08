from pydantic import BaseModel

from src.modules.hotel.ui.controllers.response_models.hotel_response_model import HotelResponseModel


class GetHotelsResponseModel(BaseModel):
    hotels: list[HotelResponseModel]
