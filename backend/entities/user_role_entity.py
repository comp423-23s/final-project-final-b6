"""User roles in the application.

This file contains the relationship between a user and their role.

It should not be directly accessable."""

from sqlalchemy import Table, Column, ForeignKey
from .entity_base import EntityBase

user_role_table = Table(
    "user_role",
    EntityBase.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('role_id', ForeignKey('role.id'), primary_key=True)
)