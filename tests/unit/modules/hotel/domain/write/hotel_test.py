from unittest import TestCase

from tests.infrastructure.modules.hotel.domain.write.stub_hotel_builder import StubHotelBuilder


class HotelTest(TestCase):
    def test_update(self) -> None:
        hotel = StubHotelBuilder().build()

        hotel.update(
            name="New name",
            location="New location",
            description="New description",
            has_swimming_pool=True
        )

        self.assertEqual(
            ["New name", "New location", "New description", True],
            [hotel.name, hotel.location, hotel.description, hotel.has_swimming_pool]
        )
