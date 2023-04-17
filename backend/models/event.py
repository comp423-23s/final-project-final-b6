"""Model representing events.

This file contains the fields representing an event.
"""

from pydantic import BaseModel
from datetime import datetime


__authors__ = ["Jackson Davis"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class Event(BaseModel):
    id: int | None = None
    name: str
    description: str
    date_time: datetime
    location: str
    image: str
    organization_id: int
