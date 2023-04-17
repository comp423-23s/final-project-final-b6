"""Organizations in the application."""

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
