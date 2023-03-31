import pytest

from sqlalchemy.orm import Session
from ...models.organization import Organization
from ...entities.organization_entity import OrganizationEntity
from ...services.organization import OrganizationService
from ...script.reset_database import reset_database

organizations = OrganizationService.get_all_organizations()

@pytest.fixture(autouse=True)
def pretest_clear_data():
    """Before running each test, reset the storage module's data."""
    reset_database()

def test_database_initial(organization: OrganizationService):
    assert(len(organization.get_all_organizations(organizations)) == 15)
    #print(OrganizationService.get_all_organizations(organization))

