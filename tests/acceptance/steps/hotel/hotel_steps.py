import json
from uuid import UUID

from behave import *
from behave.runner import Context
from sqlalchemy.orm import Session

from src.di.containers import ApplicationContainer
from src.modules.hotel.domain.write.hotel import Hotel
from tests.infrastructure.modules.hotel.domain.write.stub_hotel_builder import StubHotelBuilder


@given("hotel with uuid {uuid} exists with values")
def hotel_with_values_exists(context: Context, uuid: str):
    values: dict = json.loads(context.text)

    builder = StubHotelBuilder().with_uuid(uuid=UUID(uuid))
    if "name" in values.keys():
        builder.with_name(values["name"])

    hotel = builder.build()
    container: ApplicationContainer = context.container
    db: Session = container.database_package.db_session()
    db.add(hotel)
    db.commit()


@then("exists a hotel with name {name}")
def exists_a_hotel_with_name(context: Context, name: str):
    container: ApplicationContainer = context.container
    db: Session = container.database_package.db_session()
    hotel = db.query(Hotel).filter(Hotel.name == name).first()

    assert hotel is not None
