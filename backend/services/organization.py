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


__authors__ = ["Jackson Davis, Antonio Tudela"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class OrganizationService:

    _session: Session
    _permission: PermissionService

    def __init__(self, session: Session = Depends(db_session), permission: PermissionService = Depends()):
        self._session = session
        self._permission = permission

    def get_all_organizations(self) -> list[Organization]:
        """Fetches all the organizations in the database.
        
        Args:
            None.
        
        Returns:
            A list of all the organizations in the database.
        """

        query = select(OrganizationEntity).order_by(OrganizationEntity.id.desc())
        organizations = self._session.scalars(query)
        organization_models = []
        for org in organizations:
            if org:
                model = org.to_model()
                organization_models.append(model)
        return organization_models

    def get(self, organization_name: str) -> Organization | None:
        """Fetches a specified organization from the database.
        
        Args:
            organization_name: A string of an organization name that the caller is searching for.
            
        Returns:
            The specified organizaiton, or none if it cannot be found.
        
        Raises:
            Exception: An error occured when trying to find the organization name supplied.
        """

        query = select(OrganizationEntity).where(OrganizationEntity.name == organization_name)
        organization_entity: OrganizationEntity = self._session.scalar(query)
        if organization_entity is None:
            raise Exception("No organization with that name was found! (must be exact)")
        else:
            model = organization_entity.to_model()
            return model

    def create_organization(self, organization: OrganizationEntity) -> Organization | None:
        """Creates an organization and adds it to the database.
        
        Args:
            organization: An organization entity that the caller wants added to the database.
            
        Returns: 
            The passed in organization, or none if an error occurs.
        
        Raises:
            Exception: An error occured when trying to add the organization to the database.
        """

        query = select(OrganizationEntity).where(OrganizationEntity.name == organization.name)
        organization_entity: OrganizationEntity = self._session.scalar(query)
        if organization_entity is None:
            organization_to_add = OrganizationEntity.from_model(organization)
            self._session.add(organization_to_add)
            self._session.commit()
            return organization
        else:
            raise Exception("An organization with this name already exists!")

    def edit_organization(self, organization: Organization) -> Organization | None:
        """Edits an organization row in the database.
        
        Args:
            organizaiton: An organization model with the desired fields the caller wants updated in the database.
        
        Returns: 
            The passed in organization, or nothing if an error occurs.
            
        Raises:
            Exception: An error occured when trying to edit the organization.
        """

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
        """Deletes an organizaiton row from the database.
        
        Args: 
            organization_name: A string of the organization the caller wants deleted from the database.
            
        Returns:
            Nothing.

        Raises:
            Exception: An error occured when trying to delete the organization to the database.        
        """
        
        query = select(OrganizationEntity).where(OrganizationEntity.name == organization_name)
        organization_entity: OrganizationEntity = self._session.scalar(query)
        if organization_entity is None:
            raise Exception("No organization with that name was found! (must be exact)")
        else:
            self._session.delete(organization_entity)
            self._session.commit()
