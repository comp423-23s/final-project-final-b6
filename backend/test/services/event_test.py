"""These tests are used to ensure that the methods in ...services/event are functioning as intended.

Each method contains detialed inline comments to help developers understand what is being tested, as well as why.
"""

import pytest
from fastapi import Depends
from ...database import db_session
from ...api.authentication import registered_user
from sqlalchemy.orm import Session
from ...services.event import EventService
from ...services.permission import PermissionService, UserPermissionError
from ...models.event import Event
from ...models.organization import Organization
from ...models.user import User
from ...models.role import Role
from ...entities import OrganizationEntity, EventEntity, UserEntity, RoleEntity, PermissionEntity
from datetime import datetime


__authors__ = ["Jackson Davis, Antonio Tudela"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


# mock user and role
root = User(id=1, pid=999999999, onyen='root', email='root@unc.edu')
root_role = Role(id=1, name='root')
root_user_entity = UserEntity.from_model(root)


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
    # Bootstrap root User and Role
    global root_user_entity
    root_user_entity = UserEntity.from_model(root)
    test_session.add(root_user_entity)
    root_role_entity = RoleEntity.from_model(root_role)
    root_role_entity.users.append(root_user_entity)
    test_session.add(root_role_entity)
    root_permission_entity = PermissionEntity(action='*', resource='*', role=root_role_entity)
    test_session.add(root_permission_entity)
    test_session.commit()
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
    return EventService(test_session, PermissionService(test_session))

# this test checks that the ACM organization has only one event
def test_get_events_length_one(event: EventService):
    assert(len(event.get_organization_events("ACM at Carolina")) == 1)

# this test chekcs that the aCc organization has two events 
def test_get_events_length_two(event: EventService):
    assert(len(event.get_organization_events("(aCc) - a Culture club")) == 2)

# this test checks the get organization events method properly returns the correct event with the correct corresponding event fields
def test_get_events_exact_fields(event: EventService):
    events = event.get_organization_events("(aCc) - a Culture club")
    assert(events[1].name == event2.name)
    assert(events[1].description == event2.description)
    assert(events[1].date_time == event2.date_time)
    assert(events[1].location == event2.location)
    assert(events[0].name == event3.name)
    assert(events[0].description == event3.description)
    assert(events[0].date_time == event3.date_time)
    assert(events[0].location == event3.location)

# this test checks that the delete event method actually deletes the event
def test_delete_event_valid(event: EventService):
    #check default # of events
    #with pytest.raises(Exception) as e:
    #assert(permission.check(root_user_entity, '*', '*' ))
    assert(len(event.get_organization_events("(aCc) - a Culture club")) == 2)
    #then we delete and check it went down
    event.delete_event(2, root_user_entity)
    assert(len(event.get_organization_events("(aCc) - a Culture club")) == 1)

# this test makes sure that the deleve event method correctly raises an exception when passed in an invalid event id
def test_delete_event_invalid(event: EventService):
    #check default # of events
    assert(len(event.get_all_events()) == 3)
    #delete non existant event and raise exception
    with pytest.raises(Exception) as e:
        event.delete_event(999)
    #check that nothing was deleted 
    assert(len(event.get_all_events()) == 3)

# this test checks that the edit event method actually edits the events fields
def test_edit_event_valid(event: EventService):
    #check normal name
    assert(event.get_organization_events("ACM at Carolina")[0].name == "Culture Club Meeting") # this is because this event was added to ACM instead of aCc, but this still ensures its working correctly 
    #now we make "new" event with desired values
    ev: Event = Event(  id=1,
                        name="test name",
                        description="test desc",
                        date_time=datetime.strptime('04/06/23 16:00', '%m/%d/%y %H:%M'),
                        location="test location",
                        image="test image",
                        organization_id=1)   
    event.edit_event(ev, root)
    #check that the event is edited
    assert(event.get_organization_events("ACM at Carolina")[0].name == "test name")
    assert(event.get_organization_events("ACM at Carolina")[0].description == "test desc")
    assert(event.get_organization_events("ACM at Carolina")[0].date_time == datetime.strptime('04/06/23 16:00', '%m/%d/%y %H:%M'))
    assert(event.get_organization_events("ACM at Carolina")[0].location == "test location")
    assert(event.get_organization_events("ACM at Carolina")[0].image == "test image")

# this test checks that the edit event method raises an exception when passed in a faulty event
def test_edit_event_invalid(event: EventService):
    #check normal name
    assert(event.get_organization_events("ACM at Carolina")[0].name == "Culture Club Meeting")
    #fake event
    with pytest.raises(Exception) as e:
        ev: Event = Event()
        event.edit_event(ev)
    #check nothing changed
    assert(event.get_organization_events("ACM at Carolina")[0].name == "Culture Club Meeting")

#this test checks that the get event details method correctly returns the correct fields 
def test_get_event_details_valid(event: EventService):
    #here is the event details for reference that we will be testing correctness for:
    # event3 = Event(
    #             name="Active Minds Get Together!",
    #             description="Come join us for a get together of our Active Minds! >:)",
    #             date_time = datetime.strptime('04/05/23 14:59', '%m/%d/%y %H:%M'),
    #             location="Fetzer Gym",
    #             organization_id=3,
    #             image="https://se-images.campuslabs.com/clink/images/074a951c-704c-4b35-9e81-f16da39f9f3ed291f0dd-d7c7-47c5-9ba9-e014a2a1dc04.jpg?preset=med-sq")

    #now check that the values returned from the service method are the actual expected values 
    assert(event.get_event_details(3)).name == "Active Minds Get Together!"
    assert(event.get_event_details(3)).description == "Come join us for a get together of our Active Minds! >:)"
    assert(event.get_event_details(3)).date_time == datetime.strptime('04/05/23 14:59', '%m/%d/%y %H:%M')
    assert(event.get_event_details(3)).location == "Fetzer Gym"
    assert(event.get_event_details(3)).image == "https://se-images.campuslabs.com/clink/images/074a951c-704c-4b35-9e81-f16da39f9f3ed291f0dd-d7c7-47c5-9ba9-e014a2a1dc04.jpg?preset=med-sq"
    
# this test checks that the get evetn details method raises an exception when passed in an invalid event id
def test_get_event_details_invalid(event: EventService):
    with pytest.raises(Exception) as e:
        #make faulty fake event
        event4 = Event()
        #make sure the method raises an exception
        event.get_event_details(event4.id)

def test_create_event_valid(event: EventService):
    #first we check the default number of event for the organization
    assert(len(event.get_organization_events("(aCc) - a Culture club")) == 2)
    #then create a new one
    ev: Event = Event(name="New org meeting",description="The new org is meeting!",date_time = datetime.strptime('04/06/23 17:00', '%m/%d/%y %H:%M'),location="The Quad",organization_id=2,image="https://se-images.campuslabs.com/clink/images/78a6be92-aa7f-46d3-b731-c3f92da37039571a72b6-5e51-48e9-b8a4-74ae42ac858d.JPG?preset=small-sq")
    event.create_event(ev, root)
    # we create an event object, then check that the number of events went up
    assert(len(event.get_organization_events("(aCc) - a Culture club")) == 3)


def test_create_organization_invalid(event: EventService):
    #first we check the default number of events for the organization
    assert(len(event.get_organization_events("(aCc) - a Culture club")) == 2)
    with pytest.raises(Exception) as e:
        ev: Event = Event() #faulty event
        event.create_event(ev)
    #check no new event was added
    assert(len(event.get_organization_events("(aCc) - a Culture club")) == 2)