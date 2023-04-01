import pytest

from sqlalchemy import text
from fastapi import Depends
from sqlalchemy.orm import Session
from ...database import engine, db_session
from ...models.organization import Organization
from ...models.permission import Permission
from ...entities.organization_entity import OrganizationEntity
from ...services.organization import OrganizationService
from ...services.permission import PermissionService
from ...script.reset_database import reset_database
from ... import entities
from ...api.organization import get_all_organizations


with Session(engine) as session:
    @pytest.fixture()
    def organization():
        return OrganizationService(session)

    from ...script.dev_data import organizations
    to_entity = entities.OrganizationEntity.from_model
    session.add_all([to_entity(model) for model in organizations.models])
    session.execute(text(f'ALTER SEQUENCE {entities.OrganizationEntity.__table__}_id_seq RESTART WITH {len(organizations.models) + 1}'))
    session.commit()

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

















# Leaving here for now to show what didnt work
# TODO: REMOVE THIS BEFORE PUSHING TO STAGE JUST HERE TO LOOK THROUGH FOR BETTER IMPLIMENTATIONS DURING REVIEW!


# Mock Models
# test_organization = Organization(999,
#                                 "test_organization",
#                                 "test_overview",
#                                 "test_description",
#                                 "test_image_link")
# test_organization = Organization()
# test_organization_list = []
# test_organization_list.append(test_organization)

# @pytest.fixture(autouse=True)
# def setup_teardown(test_session: Session):
#     test_organization_entity = OrganizationEntity.from_model(test_organization)
#     test_session.add(test_organization_entity)
#     test_session.commit()

# @pytest.fixture(autouse=True)
# def pretest_clear_data():
#     """Before running each test, reset the storage module's data."""
#     reset_database()

# @pytest.fixture()
# def organization(session: Session):
#     return OrganizationService(session).get_all_organizations()







# def test_number_of_organizaitons_with_api(organization: OrganizationService):
#     assert(len(organization) == 15)



# @pytest.fixture(autouse=True)
# def setup_teardown(test_session: Session):
#     test_organization_entity = OrganizationEntity.from_model(test_organization)
#     test_session.add(test_organization_entity)
#     test_session.commit()



# def test(organization: OrganizationService):
#     assert len(test_organization_list == 1)





# organizations = OrganizationService.get_all_organizations(OrganizationService)

# # @pytest.fixture(autouse=True)
# # def pretest_clear_data():
# #     """Before running each test, reset the storage module's data."""
# #     reset_database()

# def test_database_initial(organization: OrganizationService):
#     assert(len(organization.get_all_organizations(organizations)) == 15)
#     #print(OrganizationService.get_all_organizations(organization))

