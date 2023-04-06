"""Organization is the data object representing organizations and their associated events/users."""

from pydantic import BaseModel


__authors__ = ["Jackson Davis"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class Organization(BaseModel):
    id: int | None = None
    name: str
    overview: str
    description: str
    image: str

#Added this to try and model the user profile update method, but could not get it to work
# class OrganizationForm(BaseModel):
#     name: str
#     overview: str
#     description: str
#     image: str