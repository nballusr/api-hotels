from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID

from src.shared.database.infrastructure.model_base import ModelBase


class Hotel(ModelBase):
    __tablename__ = "hotel"
    uuid = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)
    has_swimming_pool = Column(Boolean(), nullable=False)

    def update(
            self,
            name: str,
            location: str,
            description: str,
            has_swimming_pool: bool
    ) -> None:
        self.name = name
        self.location = location
        self.description = description
        self.has_swimming_pool = has_swimming_pool
