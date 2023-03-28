"""Sample Event models to use in the development environment.

These were intially designed to be used by the `script.reset_database` module."""

from ...models.event import Event
from datetime import datetime
__authors__ = ["Jackson Davis, Antonio Tudela"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

event1 = Event(id=1, 
                name="ACM event", 
                description="ACM event desc",
                date_time = datetime.strptime('04/15/23 13:55', '%m/%d/%y %H:%M'),
                location="Student Union",
                organization_id=1,
                image="https://www.google.com/url?sa=i&url=https%3A%2F%2Fdeviniti.com%2Fblog%2Fproject-work-management%2Fhow-to-organize-event-step-by-step%2F&psig=AOvVaw2qY2qTIwSLPCQDhcMmgg7z&ust=1680128412233000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCNiCuZvU__0CFQAAAAAdAAAAABAE",
                )

event2 = Event(id=2, 
                name="Ackland event", 
                description="Ackland event desc",
                date_time = datetime.strptime('04/16/23 14:00', '%m/%d/%y %H:%M'),
                location="Ackland Art Museum",
                organization_id=2,
                image="https://www.google.com/url?sa=i&url=https%3A%2F%2Fdeviniti.com%2Fblog%2Fproject-work-management%2Fhow-to-organize-event-step-by-step%2F&psig=AOvVaw2qY2qTIwSLPCQDhcMmgg7z&ust=1680128412233000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCNiCuZvU__0CFQAAAAAdAAAAABAE",
                )

models = [
    event1,
    event2
]