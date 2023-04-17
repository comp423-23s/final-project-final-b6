"""Users associated with a given organizaiton in the applicaiton.

This file contains the relationship between a user and an organizaiton.

It should not be directly accessable."""

from sqlalchemy import Table, Column, ForeignKey
from .entity_base import EntityBase

user_organization_table = Table(
    "user_organization",
    EntityBase.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('organization_id', ForeignKey('organization.id'), primary_key=True)
)