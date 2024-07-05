from src.modules.hotel.application.get_hotels.get_hotels_query import GetHotelsQuery
from src.modules.hotel.domain.read.hotel_repository import HotelRepository
from src.modules.hotel.domain.write.hotel import Hotel
from src.shared.application.query_handler import QueryHandler


class GetHotelsQueryHandler(QueryHandler):
    def __init__(self, hotel_repository: HotelRepository):
        self.__hotel_repository = hotel_repository

    def __call__(self, query: GetHotelsQuery) -> list[Hotel]:
        return self.__hotel_repository.all()
