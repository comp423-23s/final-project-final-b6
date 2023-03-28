"""Sample Organization models to use in the development environment.

These were intially designed to be used by the `script.reset_database` module."""

from ...models.organization import Organization

__authors__ = ["Kris Jordan, Jackson Davis"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


org1 = Organization(id=1, 
                    name="ACM at Carolina", 
                    overview="ACM overview", 
                    description="We are a professional community of Tar Heels who study computing; we are dedicated to exploring our field.",
                    image="https://se-images.campuslabs.com/clink/images/b8ab1d8e-ee34-449f-ae5f-e843896455c704688f5b-d1b0-411e-9f69-14c063114d55.jpg?preset=med-sq")

org2 = Organization(id=2, 
                name="Ackland Art Museum", 
                overview="Ackland overview", 
                description="Ackland description",
               image="https://se-images.campuslabs.com/clink/images/ee0bc303-002e-4aca-aaba-81ad270d3901c0ac95ac-7e47-4ee6-95bf-c6f9598dd2fd.jpg?preset=med-sq")

org3 = Organization(id=3, 
                name="Active Minds at Carolina", 
                overview="Active Minds at Carolina overview", 
                description="Active Minds at Carolina overview",
               image="https://se-images.campuslabs.com/clink/images/074a951c-704c-4b35-9e81-f16da39f9f3ed291f0dd-d7c7-47c5-9ba9-e014a2a1dc04.jpg?preset=med-sq")


models = [
    org1,
    org2,
    org3
]
