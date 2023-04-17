"""Events associated with an organization in the application.

This file includes the columns associated with an event, two methods to return an event model and an event entity, 
and a method to update an event.

Typical usage:

event1 = Event(id=1, 
                name="ACM Meet and Greet", 
                description="Meet your fellow ACMers!",
                date_time = datetime.strptime('01/06/24 14:15', '%m/%d/%y %H:%M'),
                location="Student Union",
                organization_id=1,
                image="https://se-images.campuslabs.com/clink/images/b8ab1d8e-ee34-449f-ae5f-e843896455c704688f5b-d1b0-411e-9f69-14c063114d55.jpg?preset=med-sq")
"""

from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from .entity_base import EntityBase
from ..models.event import Event
from .organization_entity import OrganizationEntity
from datetime import datetime

class EventEntity(EntityBase):
    __tablename__ = 'event'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False, default='') 
    description: Mapped[str] = mapped_column(String, nullable=False, default='')
    date_time: Mapped[DateTime] = mapped_column(DateTime, default=DateTime(datetime.utcnow))
    location: Mapped[str] = mapped_column(String, nullable=False, default='')
    image: Mapped[str] = mapped_column(String, nullable=False, default='')
    organization_id = mapped_column(Integer, ForeignKey(OrganizationEntity.id))
    organization = relationship("OrganizationEntity", back_populates="events")

    @classmethod
    def from_model(cls, model: Event) -> Self:
        return cls(
            name=model.name,
            description=model.description,
            date_time=model.date_time,
            location=model.location,
            organization_id = model.organization_id,
            image=model.image
        )

    def to_model(self) -> Event:
        return Event(
            id=self.id,
            name=self.name,
            description=self.description,
            date_time=self.date_time,
            location=self.location,
            organization_id = self.organization_id,
            image=self.image
        )

    def update(self, model: Event) -> None:
        self.name = model.name
        self.description = model.description
        self.date_time = model.date_time
        self.location = model.location
        self.image = model.image
