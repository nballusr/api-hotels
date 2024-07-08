from urllib.parse import urlencode

from httpx import Client
from parsel import Selector

from src.modules.hotel.domain.service.get_hotel_information_service import GetHotelInformationService, HotelInformation


class HttpBookingGetHotelInformationService(GetHotelInformationService):
    def __init__(self):
        self.__search_hotels_url = "https://www.booking.com/searchresults.es.html"
        self._client = Client(
            # enable http2
            http2=True,
            # add basic browser like headers to prevent getting blocked
            headers={
                "Accept-Language": "en-US,en;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
            },
            follow_redirects=True
        )

    def from_name(self, name: str) -> HotelInformation | None:
        hotel_url = self.__get_hotel_url(name)

        if not hotel_url:
            return None

        return self.__get_hotel_information(hotel_url)

    def __get_hotel_url(self, name: str) -> str | None:
        url = self.__search_hotels_url + "?" + urlencode({"ss": name})
        response = self._client.get(url)

        if response.status_code != 200:
            return None

        selector = Selector(response.text)
        return selector.css(
            'div[data-testid="property-card"][aria-label="Alojamiento"] a::attr(href)'
        ).get()  # The first href in the div is the hotel url

    def __get_hotel_information(self, hotel_url) -> HotelInformation | None:
        response = self._client.get(hotel_url)

        if response.status_code != 200:
            return None

        selector = Selector(response.text)
        return self.__scrape_hotel(selector)

    def __scrape_hotel(self, selector: Selector) -> HotelInformation:
        hotel_name = selector.css('h2.pp-header__title::text').get()
        location = selector.css('span.hp_address_subtitle::text').get().replace("\n", "")
        description = selector.css('p[data-testid="property-description"]::text').get().replace("\n", " ")
        has_swimming_pool = any(
            "piscina" in text.lower()
            for text in selector.css(
                'div[data-testid="property-most-popular-facilities-wrapper"] ul:first-of-type > li '
                'div div span div span::text'
            ).getall()
        )

        return HotelInformation(
            name=hotel_name,
            location=location,
            description=description,
            has_swimming_pool=has_swimming_pool,
        )
