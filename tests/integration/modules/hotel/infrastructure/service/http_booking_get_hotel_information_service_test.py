from unittest import TestCase
from unittest.mock import MagicMock

from httpx import Client

from src.modules.hotel.domain.service.get_hotel_information_service import HotelInformation
from src.modules.hotel.infrastructure.service.http_booking_get_hotel_information_service import \
    HttpBookingGetHotelInformationService


class HttpBookingGetHotelInformationServiceTest(TestCase):
    def setUp(self) -> None:
        self.__mock_client = MagicMock(spec=Client)
        self.__service = HttpBookingGetHotelInformationService()
        self.__service._client = self.__mock_client

    def test_search_page_not_found(self) -> None:
        self.__mock_client.get.return_value.status_code = 404

        hotel_info = self.__service.from_name("pato amarillo")
        self.assertIsNone(hotel_info)

    def test_search_page_found_but_not_hotel_url(self) -> None:
        self.__mock_client.get.return_value.status_code = 200
        self.__mock_client.get.return_value.text = ""

        hotel_info = self.__service.from_name("pato amarillo")
        self.assertIsNone(hotel_info)

    def test_hotel_url_not_found(self) -> None:
        self.__mock_client.get.side_effect = self.mock_get_response_with_not_found_for_hotel_page

        hotel_info = self.__service.from_name("pato amarillo")
        self.assertIsNone(hotel_info)

    def mock_get_response_with_not_found_for_hotel_page(self, url):
        if url.startswith("https://www.booking.com/searchresults.es.html"):
            # Simulate search results page
            return MagicMock(
                status_code=200,
                text='<html><body><div data-testid="property-card" aria-label="Alojamiento"><a '
                     'href="https://example.com/hotel"></a></div></body></html>')
        else:
            return MagicMock(status_code=404)  # Default to 404 for unknown URLs

    def test_hotel_information_is_returned(self) -> None:
        self.__mock_client.get.side_effect = self.mock_get_responses

        hotel_info = self.__service.from_name("pato amarillo")
        self.assertIsNotNone(hotel_info)
        self.assertEqual(
            HotelInformation(
                name="Hotel Name",
                location="Hotel Location",
                description="Hotel Description",
                has_swimming_pool=True,
            ),
            hotel_info,
        )

    def mock_get_responses(self, url):
        if url.startswith("https://www.booking.com/searchresults.es.html"):
            # Simulate search results page
            return MagicMock(
                status_code=200,
                text='<html><body><div data-testid="property-card" aria-label="Alojamiento"><a '
                     'href="https://example.com/hotel"></a></div></body></html>')
        elif url.startswith("https://example.com/hotel"):
            # Simulate hotel details page
            return MagicMock(
                status_code=200,
                text="""
                    <html>
                        <body>
                            <h2 class="pp-header__title">Hotel Name</h2>
                            <span class="hp_address_subtitle">Hotel Location</span>
                            <p data-testid="property-description">Hotel Description</p>
                            <div data-testid="property-most-popular-facilities-wrapper">
                                <ul>
                                    <li><div><div><span><div><span>Facility 1</span></div></span></div></div></li>
                                    <li><div><div><span><div><span>Facility 2</span></div></span></div></div></li>
                                    <li><div><div><span><div><span>Has Piscina</span></div></span></div></div></li>
                                </ul>
                            </div>
                        </body>
                    </html>
                """)
        else:
            return MagicMock(status_code=404)  # Default to 404 for unknown URLs
