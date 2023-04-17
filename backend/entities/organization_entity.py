"""Organizations in the application.

This file includes the columns associated with an organization, two methods to return an organization model and an organization entity, 
and a method to update an anganization.

Typical usage:

org1 = Organization(id=1, #CS
                    name="ACM at Carolina", 
                    overview="ACM at Carolina is dedicated to helping encourage students find their passion in the computer science world and build a strong community of students, faculty, and professionals at Chapel Hill. Feel free to check out our page!", 
                    description="Mission Statement: ""We are a professional community of Tar Heels who study computing; we are dedicated to exploring our field, defining our interests, engaging with each other, discovering our strengths, and improving our skills."" If you are interested in joining, please visit this link: https://bit.ly/ACM-Sign-Up. Also, make sure to contact us with any questions!",
                    image="https://se-images.campuslabs.com/clink/images/b8ab1d8e-ee34-449f-ae5f-e843896455c704688f5b-d1b0-411e-9f69-14c063114d55.jpg?preset=med-sq")
"""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from .entity_base import EntityBase
from .user_organization_entity import user_organization_table
from ..models.organization import Organization


__authors__ = ['Jackson Davis']
__copyright__ = 'Copyright 2023'
__license__ = 'MIT'


class OrganizationEntity(EntityBase):
    __tablename__ = 'organization'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, default='') 
    overview: Mapped[str] = mapped_column(String(3000), nullable=False, default='')
    description: Mapped[str] = mapped_column(String(100000), nullable=False, default='')
    image: Mapped[str] = mapped_column(String(3000), nullable=False, default='')
    users: Mapped[list['UserEntity']] = relationship(secondary=user_organization_table, back_populates='organizations')
    events = relationship("EventEntity", back_populates="organization", cascade="all, delete-orphan")

    
    @classmethod
    def from_model(cls, model: Organization) -> Self:
        return cls(
            name=model.name,
            overview=model.overview,
            description=model.description,
            image=model.image
        )

    def to_model(self) -> Organization:
        return Organization(
            id=self.id,
            name=self.name,
            overview=self.overview,
            description=self.description,
            image=self.image
        )

    def update(self, model: Organization) -> None:
        self.name = model.name
        self.overview = model.overview
        self.description = model.description
        self.image = model.image
