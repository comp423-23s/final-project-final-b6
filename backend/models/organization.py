"""Organization is the data object representing organizations and their associated events/users."""

from pydantic import BaseModel


<<<<<<< HEAD
__authors__ = ["Kris Jordan", "Jackson Davis"]
=======
__authors__ = ["Jackson Davis"]
>>>>>>> b98fd39427300e541a0a95583b25bce101ebaabb
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class Organization(BaseModel):
    id: int | None = None
    name: str
    overview: str
    description: str
    image: str
    
