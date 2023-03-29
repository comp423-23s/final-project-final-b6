from fastapi import Depends
from sqlalchemy import select, or_, func
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

    def get_all_organizations(self) -> list[Organization]:
        query = select(OrganizationEntity)
        organizations = self._session.scalars(query)
        organization_models = []
        for org in organizations:
            if org:
                model = org.to_model()
                organization_models.append(model)
        return organization_models

    def get(self, organization_name: str) -> Organization | None:
        query = select(OrganizationEntity).where(OrganizationEntity.name == organization_name)
        organization_entity: OrganizationEntity = self._session.scalar(query)
        if organization_entity is None:
            raise Exception("No organization with that name was found! (must be exact)")
        else:
            model = organization_entity.to_model()
            return model

    # This method will add an org to the db based on the passed in params.
    # Might need to clean up the variable names a little, but as of now, the api works with test data
    def create_organization(self, organization_name: OrganizationEntity) -> Organization | None: #org_name of type OrgEnt or str?
        query = select(OrganizationEntity).where(OrganizationEntity.name == organization_name.name)
        organization_entity: OrganizationEntity = self._session.scalar(query)
        if organization_entity is None:
            orgToAdd = OrganizationEntity.from_model(organization_name)
            self._session.add(orgToAdd)
            self._session.commit()
            return organization_name
        else:
            raise Exception("An organization with this name already exists!")