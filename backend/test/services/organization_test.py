import pytest

from sqlalchemy.orm import Session
from ...database import engine

from ...services.organization import OrganizationService
from ...entities.organization_entity import OrganizationEntity
from ...models.organization import Organization

__authors__ = ['Antonio Tudela']
__copyright__ = 'Copyright 2023'
__license__ = 'MIT'

# Mock organizations
org1 = Organization(id=1, #CS
                    name="ACM at Carolina", 
                    overview="ACM at Carolina is dedicated to helping encourage students find their passion in the computer science world and build a strong community of students, faculty, and professionals at Chapel Hill. Feel free to check out our page!", 
                    description="Mission Statement: ""We are a professional community of Tar Heels who study computing; we are dedicated to exploring our field, defining our interests, engaging with each other, discovering our strengths, and improving our skills."" If you are interested in joining, please visit this link: https://bit.ly/ACM-Sign-Up. Also, make sure to contact us with any questions!",
                    image="https://se-images.campuslabs.com/clink/images/b8ab1d8e-ee34-449f-ae5f-e843896455c704688f5b-d1b0-411e-9f69-14c063114d55.jpg?preset=med-sq")

org2 = Organization(id=2, 
                    name="Ackland Art Museum", 
                    overview="The Ackland Art Museum features a collection of over 19,000 artworks and rotating exhibitions throughout the year. Admission to the Museum is free for all. A vibrant schedule of events and opportunities for students to get involved are available.", 
                    description="The Ackland Art Museum, located on S. Columbia Street near Franklin St., features a permanent collection of over 20,000 works of art. Rotating special exhibitions feature a wide range of art: from sound and video installations to early modern prints and photographs, from 19th-century French paintings to contemporary Japanese ceramics. Ackland Upstairs is the Museum’s second floor gallery where they display art selected by UNC-Chapel Hill faculty members to complement the courses they teach. It’s likely you will have a class at the Ackland during your time at Carolina! The Ackland also offers a vibrant year-round schedule of free and low-cost public programs featuring live music, ﬁlms, hands-on art making classes, gallery tours, and evening and weekend activities. Their ART& community space is food & beverage friendly and makes a great study spot. The Ackland offers a variety of opportunities for students to engage with the Museum, including the Ackland Student Guide program and internships. In addition, student memberships to the Museum are free for UNC undergraduate and graduate students and offer benefits including 10'%' off at the Museum Store. Sign up for FREE Ackland Student Membership. To stay connected, follow the Ackland on social media and sign up for our e-news! https://www.youtube.com/watch?v=0H1nKdxZp-E&t=2s",
                    image="https://se-images.campuslabs.com/clink/images/ee0bc303-002e-4aca-aaba-81ad270d3901c0ac95ac-7e47-4ee6-95bf-c6f9598dd2fd.jpg?preset=med-sq")

org6 = Organization(id=6,
                    name="1789",
                    overview="1789, powered by Innovate Carolina,  is free a co-working space and venture lab designed for students to take their idea to the next level, meet other student entrepreneurs, connect to resources and grow a team. ",
                    description="1789, powered by Innovate Carolina, is the University's central hub where innovation and entrepreneurship happen for all UNC students with an idea. Any UNC student is welcome to join.  1789 is free a co-working space and venture lab designed for students to take their idea to the next level, meet other student entrepreneurs, connect to resources and grow a team. With an open, flexible workspace conveniently located at 173 E. Franklin Street in the heart of downtown Chapel Hill, members may use the space for individual brainstorming, small meetings or larger events.  Innovate Carolina works to connect and support all students and programs on campus interested in innovation or entrepreneurship.  1789 members are not only connected to the Innovate Carolina network, but are also provided individualized support in starting their own ventures with access to workshops, classes, office hours and events in partnership with groups like Launch Chapel Hill, the Campus Y, the UNC Minor in Entrepreneurship, the Carolina Challenge and a plethora of other student organizations. ",
                    image="https://se-images.campuslabs.com/clink/images/13f76c3b-9504-46be-9b9a-0362c5ffb8d7f82aa3e6-2be6-4000-85f1-227422f703bc.jpg?preset=med-sq")


@pytest.fixture(autouse=True)
def setup_teardown(test_session: Session):
    # Bootstrap org1
    org_one_entity = OrganizationEntity.from_model(org1)
    test_session.add(org_one_entity)
    test_session.commit()
    #Bootstrap org2
    org_two_entity = OrganizationEntity.from_model(org2)
    test_session.add(org_two_entity)
    test_session.commit()
    #Bootstrap org6
    org_six_entity = OrganizationEntity.from_model(org6)
    test_session.add(org_six_entity)
    test_session.commit()
    yield


@pytest.fixture()
def organization(test_session: Session):
    return OrganizationService(test_session)

    
def test_organization_get_id_valid(organization: OrganizationService):
    assert(organization.get("ACM at Carolina").id == 1)


# This test makes sure that an invalid club name, i.e, one that does not exist, raises an exception (as it should as thats how we handle it in the OrganizationService class)
def test_organization_get_id_invalid(organization: OrganizationService):
    with pytest.raises(Exception) as e:
        organization.get("Nonexistent Club")


def test_edit_organization_valid(organization: OrganizationService):
    #first check to make sure the normal overview is there
    assert(organization.get("1789").overview == "1789, powered by Innovate Carolina,  is free a co-working space and venture lab designed for students to take their idea to the next level, meet other student entrepreneurs, connect to resources and grow a team. ")
    #then we make a "new org" with the desired values to be passed into the service method
    org: Organization = Organization(id=6, name="1789", overview="this is a test", description="test description", image="test image")
    #next we pass in the above org
    organization.edit_organization(org)
    #and finally we check if the service method did its job and changed the values
    assert(organization.get("1789").overview == "this is a test")


def test_edit_organization_invalid(organization: OrganizationService):
    #try to use the service method without supplying it an organization
    with pytest.raises(Exception) as e:
        org: Organization = Organization()
        organization.edit_organization(org)
        

def test_create_organization_valid(organization: OrganizationService):
    #first we check the default number of organizations
    assert(len(organization.get_all_organizations()) == 3)
    #then create a new one
    org: Organization = Organization(id=999, name="999th Club", overview="The overview for the 999th club", description="The description for the 999th club", image="The image of the 999th club")
    organization.create_organization(org)
    #we create the org, and then create it, then check that the number of orgs went up
    assert(len(organization.get_all_organizations()) == 4)


def test_create_organization_invalid(organization: OrganizationService):
    #first we check the default number of organizations
    assert(len(organization.get_all_organizations()) == 3)
    with pytest.raises(Exception) as e:
        org: Organization = Organization() #faulty organization
        organization.create_organization(org)
    #check no new organization was added
    assert(len(organization.get_all_organizations()) == 3)


def test_delete_organization_valid(organization: OrganizationService):
    #first we check the default number of organizations
    assert(len(organization.get_all_organizations()) == 3)
    #then we delete one and check the length to make sure its gone down by one
    organization.delete_organization("1789")
    assert(len(organization.get_all_organizations()) == 2)


def test_delete_organization_invalid(organization: OrganizationService):
    #first we check the default number of organizations
    assert(len(organization.get_all_organizations()) == 3)
    #then we and organization that doesnt exist so it should raise an exception
    with pytest.raises(Exception) as e:
        organization.delete_organization("Club No Name")
    #check that nothing was deleted
    assert(len(organization.get_all_organizations()) == 3)