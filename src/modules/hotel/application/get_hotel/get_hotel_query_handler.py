from src.modules.hotel.application.get_hotel.get_hotel_query import GetHotelQuery
from src.modules.hotel.domain.exception.hotel_not_found_exception import HotelNotFoundException
from src.modules.hotel.domain.read.hotel_repository import HotelRepository
from src.modules.hotel.domain.write.hotel import Hotel
from src.shared.application.query_handler import QueryHandler


class GetHotelQueryHandler(QueryHandler):
    def __init__(self, hotel_repository: HotelRepository):
        self.__hotel_repository = hotel_repository

    def __call__(self, query: GetHotelQuery) -> Hotel:
        existing_hotel = self.__hotel_repository.of_uuid(query.uuid)
        if existing_hotel is None:
            raise HotelNotFoundException.create(query.uuid)

        return existing_hotel
