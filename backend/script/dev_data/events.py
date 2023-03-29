"""Sample Event models to use in the development environment.

These were intially designed to be used by the `script.reset_database` module."""

from ...models.event import Event
from datetime import datetime
__authors__ = ["Jackson Davis, Antonio Tudela"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

event1 = Event(id=1, 
                name="ACM Meet and Greet", 
                description="Meet your fellow ACMers!",
                date_time = datetime.strptime('01/06/24 13:55', '%m/%d/%y %H:%M'),
                location="Student Union",
                organization_id=1,
                image="https://se-images.campuslabs.com/clink/images/b8ab1d8e-ee34-449f-ae5f-e843896455c704688f5b-d1b0-411e-9f69-14c063114d55.jpg?preset=med-sq",
                )

event2 = Event(id=2, 
                name="Ackland Icecream Meetup", 
                description="Join us for icecream in Lenoir!",
                date_time = datetime.strptime('04/16/23 14:00', '%m/%d/%y %H:%M'),
                location="Lenoir",
                organization_id=2,
                image="https://www.google.com/url?sa=i&url=https%3A%2F%2Fdeviniti.com%2Fblog%2Fproject-work-management%2Fhow-to-organize-event-step-by-step%2F&psig=AOvVaw2qY2qTIwSLPCQDhcMmgg7z&ust=1680128412233000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCNiCuZvU__0CFQAAAAAdAAAAABAE",
                )

event3 = Event(id=3,
                name="Active Minds Get Together!",
                description="Come join us for a get together of our Active Minds! >:)",
                date_time = datetime.strptime('04/05/23 14:59', '%m/%d/%y %H:%M'),
                location="Fetzer Gym",
                organization_id=3,
                image="https://se-images.campuslabs.com/clink/images/074a951c-704c-4b35-9e81-f16da39f9f3ed291f0dd-d7c7-47c5-9ba9-e014a2a1dc04.jpg?preset=med-sq")

event4 = Event(id=4,
                name="Culture Club Meeting",
                description="The Culture Club is having a meeting!",
                date_time = datetime.strptime('04/06/23 17:00', '%m/%d/%y %H:%M'),
                location="The Quad",
                organization_id=4,
                image="https://se-images.campuslabs.com/clink/images/78a6be92-aa7f-46d3-b731-c3f92da37039571a72b6-5e51-48e9-b8a4-74ae42ac858d.JPG?preset=small-sq")

event5 = Event(id=5,
                name="Culture Club Meething Round Two",
                description="The follow up meeting for the aCc",
                date_time = datetime.strptime('04/07/23 17:00', '%m/%d/%y %H:%M'),
                location="The Quad",
                organization_id=4,
                image="https://se-images.campuslabs.com/clink/images/78a6be92-aa7f-46d3-b731-c3f92da37039571a72b6-5e51-48e9-b8a4-74ae42ac858d.JPG?preset=small-sq")

event6 = Event(id=6,
                name="BeAM Workshop: Woodworking",
                description="A workshop for woodworking",
                date_time = datetime.strptime('04/01/23 13:00', '%m/%d/%y %H:%M'),
                location="BeAM at Murray",
                organization_id=8,
                image="https://se-images.campuslabs.com/clink/images/f04982cd-f95e-4fbf-807b-54e54860b75648c5a2fd-675c-4caf-98f7-7f34349b9504.jpg?preset=med-sq")

event7 = Event(id=7,
                name="BeAM Workshop: 3D Printing",
                description="A workshop for 3D printing",
                date_time = datetime.strptime('04/01/23 14:00', '%m/%d/%y %H:%M'),
                location="BeAM at Murray",
                organization_id=8,
                image="https://se-images.campuslabs.com/clink/images/f04982cd-f95e-4fbf-807b-54e54860b75648c5a2fd-675c-4caf-98f7-7f34349b9504.jpg?preset=med-sq")

event8 = Event(id=8,
                name="BeAM Workshop: Laser Cutting",
                description="A workshop for laser cutting",
                date_time = datetime.strptime('04/01/23 15:00', '%m/%d/%y %H:%M'),
                location="BeAM at Murray",
                organization_id=8,
                image="https://se-images.campuslabs.com/clink/images/f04982cd-f95e-4fbf-807b-54e54860b75648c5a2fd-675c-4caf-98f7-7f34349b9504.jpg?preset=med-sq")


event9 = Event(id=9,
                name="Pearl Hacks Workshop on APIs",
                description="A workshop on APIs",
                date_time = datetime.strptime('05/15/23 16:00', '%m/%d/%y %H:%M'),
                location="Sitterson 014",
                organization_id=10,
                image="https://se-images.campuslabs.com/clink/images/4f1a4ee2-315a-4001-98b8-bdaba68215a5dbf8cb84-0c1c-4e90-be8b-5c0273a9cac0.png?preset=med-sq")

event10 = Event(id=10,
                name="Cybersec Meetup",
                description="Join us for a gathering where we talk about cybersec",
                date_time = datetime.strptime('03/30/23 19:00', '%m/%d/%y %H:%M'),
                location="Zoom",
                organization_id=14,
                image="https://se-images.campuslabs.com/clink/images/b7015dec-588a-478f-9813-b0d6ef694eaa48fdeded-7fd8-4170-b5b6-aa17b0dd7fd2.png?preset=med-sq")
models = [
    event1,
    event2,
    event3,
    event4,
    event5,
    event6,
    event7,
    event8,
    event9,
    event10
]