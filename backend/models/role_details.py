"""Basic model for fields of the role model."""

from pydantic import BaseModel
from . import User, Permission

class RoleDetails(BaseModel):
    id: int | None = None
    name: str
    permissions: list[Permission]
    users: list[User]