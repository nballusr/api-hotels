from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID

from src.shared.database.infrastructure.model_base import ModelBase


class Hotel(ModelBase):
    __tablename__ = "hotel"
    uuid = Column(UUID(as_uuid=True), primary_key=True)
