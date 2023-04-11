import pytest

from sqlalchemy import text
from sqlalchemy.orm import Session
from ...database import engine

from ...services.organization import OrganizationService
from ...entities.organization_entity import OrganizationEntity
from ...models.organization import Organization
from ...script.reset_database import reset_database
from ... import entities


__authors__ = ['Antonio Tudela']
__copyright__ = 'Copyright 2023'
__license__ = 'MIT'

#reset_database() 
#instead of using the below lines (commented out) to load up the dev data from scratch, i tried calling reset database, but then that made the tests fail too :(

with Session(engine) as session:
    @pytest.fixture()
    def organization():
        return OrganizationService(session)
    
    @pytest.fixture()
    def organization_entity():
        return OrganizationEntity()

    @pytest.fixture()
    def organization_organization():
        return Organization()

    from ...script.dev_data import organizations
    # to_entity = entities.OrganizationEntity.from_model
    # session.add_all([to_entity(model) for model in organizations.models])
    # session.execute(text(f'ALTER SEQUENCE {entities.OrganizationEntity.__table__}_id_seq RESTART WITH {len(organizations.models) + 1}'))
    # session.commit()

    def test_number_of_organizaitons_with_service(organization: OrganizationService):
        assert(len(organization.get_all_organizations()) == 15)


def test_number_of_organizations_with_models():
    assert(len(organizations.models) == 15)
    
    
def test_organization_get_id_valid(organization: OrganizationService):
    assert(organization.get("ACM at Carolina").id == 1)


# This test makes sure that an invalid club name, i.e, one that does not exist, raises an exception (as it should as thats how we handle it in the OrganizationService class)
def test_organization_get_id_invalid(organization: OrganizationService):
    with pytest.raises(Exception) as e:
        organization.get("Nonexistent Club")


def test_edit_organization_valid(organization: OrganizationService):
    #first check to make sure the normal overview is there
    assert(organization.get("(aCc) - a Culture club").overview == "Share, respect, and support all cultural identities.")
    #then we make a "new org" with the desired values to be passed into the service method
    org: Organization = Organization(id=4, name="(aCc) - a Culture club", overview="this is a test", description="test description", image="test image")
    #next we pass in the above org
    organization.edit_organization(org)
    #and finally we check if the service method did its job and changed the values
    assert(organization.get("(aCc) - a Culture club").overview == "this is a test")


def test_edit_organization_invalid(organization: OrganizationService):
    #try to use the service method without supplying it an organization
    with pytest.raises(Exception) as e:
        org: Organization = Organization()
        organization.edit_organization(org)