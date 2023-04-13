import pytest
from sqlalchemy.orm import Session
from ...services.event import EventService
from ...models.event import Event
from ...models.organization import Organization
from ...entities import OrganizationEntity, EventEntity
from datetime import datetime

# mock events
event1 = Event(
                name="Culture Club Meeting",
                description="The Culture Club is having a meeting!",
                date_time = datetime.strptime('04/06/23 17:00', '%m/%d/%y %H:%M'),
                location="The Quad",
                organization_id=4,
                image="https://se-images.campuslabs.com/clink/images/78a6be92-aa7f-46d3-b731-c3f92da37039571a72b6-5e51-48e9-b8a4-74ae42ac858d.JPG?preset=small-sq")

event2 = Event(
                name="Culture Club Meething Round Two",
                description="The follow up meeting for the aCc",
                date_time = datetime.strptime('04/07/23 17:00', '%m/%d/%y %H:%M'),
                location="The Quad",
                organization_id=4,
                image="https://se-images.campuslabs.com/clink/images/78a6be92-aa7f-46d3-b731-c3f92da37039571a72b6-5e51-48e9-b8a4-74ae42ac858d.JPG?preset=small-sq")
event3 = Event(
                name="Active Minds Get Together!",
                description="Come join us for a get together of our Active Minds! >:)",
                date_time = datetime.strptime('04/05/23 14:59', '%m/%d/%y %H:%M'),
                location="Fetzer Gym",
                organization_id=3,
                image="https://se-images.campuslabs.com/clink/images/074a951c-704c-4b35-9e81-f16da39f9f3ed291f0dd-d7c7-47c5-9ba9-e014a2a1dc04.jpg?preset=med-sq")

# mock organizations
oneEventOrg = Organization(id=1, 
                    name="ACM at Carolina", 
                    overview="ACM at Carolina is dedicated to helping encourage students find their passion in the computer science world and build a strong community of students, faculty, and professionals at Chapel Hill. Feel free to check out our page!", 
                    description="Mission Statement: ""We are a professional community of Tar Heels who study computing; we are dedicated to exploring our field, defining our interests, engaging with each other, discovering our strengths, and improving our skills."" If you are interested in joining, please visit this link: https://bit.ly/ACM-Sign-Up. Also, make sure to contact us with any questions!",
                    image="https://se-images.campuslabs.com/clink/images/b8ab1d8e-ee34-449f-ae5f-e843896455c704688f5b-d1b0-411e-9f69-14c063114d55.jpg?preset=med-sq")
twoEventOrg = Organization(id=4,
                    name="(aCc) - a Culture club",
                    overview="Share, respect, and support all cultural identities.",
                    description="Our Mission: Share, respect, and support all cultural identities. Share: We hold Culture Shop and Festival Assembly for our members to share their cultural identities and knowledge in culture. Culture Shop offers an online platform to showcase cultures with pictures or videos or other materials on our organization's website. Members who have a culture or multiple cultures listed online will have the chance to show their cultures at Festival Assembly, which is held once per year. We will invite all UNC students to come to our Festival Assembly. Respect: We hold workshops for lectures and discussions. We will invite professors, graduate students, researchers, and other scholars in academia to educate us about culture. We will also invite other cultural organizations to talk about connections or differences among cultures together. Respecting each other's cultural identities is our priority. Support: We hold Culture Support Community and Culture Support Service to support both international students and endangered cultures. We will have an online community chat group for students to connect, and we will hold regular meetings for students to share their stories and support each other. As for Culture Support Service, we will offer a channel to encourage people worldwide to look for and collect endangered cultures. We will work together to discover how to commit to preserving global cultural identities and bring endangered cultures back.",
                    image="https://se-images.campuslabs.com/clink/images/78a6be92-aa7f-46d3-b731-c3f92da37039571a72b6-5e51-48e9-b8a4-74ae42ac858d.JPG?preset=small-sq")


@pytest.fixture(autouse=True)
def setup_teardown(test_session: Session):
    # Bootstrap oneEventOrg and its events
    oneEventOrg_entity = OrganizationEntity.from_model(oneEventOrg)
    test_session.add(oneEventOrg_entity)
    event1_entity = EventEntity.from_model(event1)
    oneEventOrg_entity.events.append(event1_entity)
    test_session.add(oneEventOrg_entity)
    test_session.commit()
    # Bootstrap twoEventOrg and its events
    twoEventOrg_entity = OrganizationEntity.from_model(twoEventOrg)
    test_session.add(twoEventOrg_entity)
    event2_entity = EventEntity.from_model(event2)
    twoEventOrg_entity.events.append(event2_entity)
    event3_entity = EventEntity.from_model(event3)
    twoEventOrg_entity.events.append(event3_entity)
    test_session.add(twoEventOrg_entity)
    test_session.commit()
    yield


@pytest.fixture()
def event(test_session: Session):
    return EventService(test_session)

def test_get_events_length_one(event: EventService):
    print(event.get_organization_events("ACM at Carolina"))
    assert(len(event.get_organization_events("ACM at Carolina")) == 1)

def test_get_events_length_two(event: EventService):
    assert(len(event.get_organization_events("(aCc) - a Culture club")) == 2)

def tet_get_events_exact_fields(event: EventService):
    events = event.get_organization_events("(aCc) - a Culture club")
    assert(events[0].name == event2.name)
    assert(events[0].description == event2.description)
    assert(events[0].date_time == event2.Date_time)
    assert(events[0].location == event2.location)
    assert(events[1].name == event3.name)
    assert(events[1].description == event3.description)
    assert(events[1].date_time == event3.Date_time)
    assert(events[1].location == event3.location)

def test_delete_event_valid(event: EventService):
    #check default # of events
    assert(len(event.get_organization_events("(aCc) - a Culture club")) == 2)
    #then we delete and check it went down
    event.delete_event(2) # i think this works as intended but may need some more eyes on it, im dead
    assert(len(event.get_organization_events("(aCc) - a Culture club")) == 1)

def test_delete_event_invalid(event: EventService):
    #check default # of events
    assert(len(event.get_all_events()) == 3)
    #delete non existant event and raise exception
    with pytest.raises(Exception) as e:
        event.delete_event(999)
    #check that nothing was deleted 
    assert(len(event.get_all_events()) == 3)