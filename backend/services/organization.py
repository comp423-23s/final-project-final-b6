"""Organization services are used by the applicaiton to provide the functionality for the application to manipulate the database accordingly.

Please see .api/organization for more details.
"""

from fastapi import Depends
from sqlalchemy import select, or_, func, update
from ..entities.entity_base import EntityBase
from sqlalchemy.orm import Session
from ..database import db_session
from ..models.organization import Organization
from ..entities import OrganizationEntity
from .permission import PermissionService


class OrganizationService:

    _session: Session
    _permission: PermissionService

    def __init__(self, session: Session = Depends(db_session), permission: PermissionService = Depends()):
        self._session = session
        self._permission = permission

    # This method returns a list of all organizaitons in the DB
    def get_all_organizations(self) -> list[Organization]:
        query = select(OrganizationEntity).order_by(OrganizationEntity.id.desc())
        organizations = self._session.scalars(query)
        organization_models = []
        for org in organizations:
            if org:
                model = org.to_model()
                organization_models.append(model)
        return organization_models

    # This method takes in an organization name, and returns details about the organization
    def get(self, organization_name: str) -> Organization | None:
        query = select(OrganizationEntity).where(OrganizationEntity.name == organization_name)
        organization_entity: OrganizationEntity = self._session.scalar(query)
        if organization_entity is None:
            raise Exception("No organization with that name was found! (must be exact)")
        else:
            model = organization_entity.to_model()
            return model

    # This method will add an org to the db based on the passed in params.
    def create_organization(self, organization: OrganizationEntity) -> Organization | None:
        query = select(OrganizationEntity).where(OrganizationEntity.name == organization.name)
        organization_entity: OrganizationEntity = self._session.scalar(query)
        if organization_entity is None:
            organization_to_add = OrganizationEntity.from_model(organization)
            self._session.add(organization_to_add)
            self._session.commit()
            return organization
        else:
            raise Exception("An organization with this name already exists!")

    # This method takes in an organization object, and updates the correlating organization already in the DB with updated info
    def edit_organization(self, organization: Organization) -> Organization | None:
        query = select(OrganizationEntity).where(OrganizationEntity.name == organization.name)
        organization_entity: OrganizationEntity = self._session.scalar(query)
        if organization_entity is None:
            raise Exception("No organization with that name was found! (must be exact)")
        else:
            organization_entity.overview = organization.overview
            organization_entity.description = organization.description
            organization_entity.image = organization.image
            self._session.commit()
            return organization

    # This method takes in the name of an organization to be deleted and then deletes it from the DB
    def delete_organization(self, organization_name: str) -> None: 
        query = select(OrganizationEntity).where(OrganizationEntity.name == organization_name)
        organization_entity: OrganizationEntity = self._session.scalar(query)
        if organization_entity is None:
            raise Exception("No organization with that name was found! (must be exact)")
        else:
            self._session.delete(organization_entity)
            self._session.commit()
