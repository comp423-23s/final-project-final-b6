"""Basic model for fields of the role model.

This file contains the fields representing role details."""

from pydantic import BaseModel
from . import User, Permission

class RoleDetails(BaseModel):
    id: int | None = None
    name: str
    permissions: list[Permission]
    users: list[User]