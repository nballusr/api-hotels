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
    if "location" in values.keys():
        builder.with_location(values["location"])
    if "description" in values.keys():
        builder.with_description(values["description"])
    if "has_swimming_pool" in values.keys():
        builder.with_has_swimming_pool(values["has_swimming_pool"])

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


@then("exists a hotel with uuid {uuid} and values")
def exists_a_hotel_with_name(context: Context, uuid: str):
    values: dict = json.loads(context.text)

    container: ApplicationContainer = context.container
    db: Session = container.database_package.db_session()
    hotel = db.query(Hotel).filter(Hotel.uuid == uuid).first()

    assert hotel is not None
    if "name" in values.keys():
        assert hotel.name == values["name"]
    if "location" in values.keys():
        assert hotel.location == values["location"]
    if "description" in values.keys():
        assert hotel.description == values["description"]
    if "has_swimming_pool" in values.keys():
        assert hotel.has_swimming_pool == values["has_swimming_pool"]

@then("a hotel with uuid {uuid} does not exist")
def exists_a_hotel_with_name(context: Context, uuid: str):
    container: ApplicationContainer = context.container
    db: Session = container.database_package.db_session()
    hotel = db.query(Hotel).filter(Hotel.uuid == uuid).first()

    assert hotel is None

