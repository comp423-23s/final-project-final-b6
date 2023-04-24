"""Organization services are used by the applicaiton to provide the functionality for the application to manipulate the database accordingly.

Please see .api/organization for more details.
"""

from fastapi import Depends
from sqlalchemy import select, or_, func, update
from ..entities.entity_base import EntityBase
from sqlalchemy.orm import Session
from ..database import db_session
from ..models.organization import Organization
from ..models.user import User
from ..entities import OrganizationEntity, UserEntity
from .permission import PermissionService
from .permission import UserPermissionError


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

    def create_organization(self, organization: OrganizationEntity, user: UserEntity) -> Organization | None:
        """Creates an organization and adds it to the database.
        
        Args:
            organization: An organization entity that the caller wants added to the database.

            user: A user entity that is passed in to check if the given user has the needed 
            permissions to be able to create an organizaiton.

        Returns: 
            The passed in organization, or none if an error occurs.
        
        Raises:
            Exception: An error occured when trying to add the organization to the database.

            UserPermissionError: An error occured when trying to create an organization due to 
            improper user permissions.
        """

        user_query = select(UserEntity).where(UserEntity.id == user.id)
        user_entity: UserEntity = self._session.scalar(user_query)
        action = 'organization.create_organization'
        resource = '/create'

        if self._permission.check(user_entity, action, resource):
            query = select(OrganizationEntity).where(OrganizationEntity.name == organization.name)
            organization_entity: OrganizationEntity = self._session.scalar(query)
            if organization_entity is None:
                organization_to_add = OrganizationEntity.from_model(organization)
                self._session.add(organization_to_add)
                self._session.commit()
                return organization
            else:
                raise Exception("An organization with this name already exists!")
        else:
            raise UserPermissionError(action, resource)

    def edit_organization(self, organization: Organization, user: UserEntity) -> Organization | None:
        """Edits an organization row in the database.
        
        Args:
            organizaiton: An organization model with the desired fields the caller wants updated in the database.

            user: A user entity that is passed in to check if the given user has the needed permissions to be able to 
            edit an organizaiton.
        
        Returns: 
            The passed in organization, or nothing if an error occurs.
            
        Raises:
            Exception: An error occured when trying to edit the organization.

            UserPermissionError: An error occured when trying to edit an organization due to 
            improper user permissions.
        """

        user_query = select(UserEntity).where(UserEntity.id == user.id)
        user_entity: UserEntity = self._session.scalar(user_query)
        action = 'organization.edit_organization'
        resource = '/{organization.name}/edit'

        if self._permission.check(user_entity, action, resource):
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
        else:
            raise UserPermissionError(action, resource)

    def delete_organization(self, organization_name: str, user: UserEntity) -> None: 
        """Deletes an organizaiton row from the database.
        
        Args: 
            organization_name: A string of the organization the caller wants deleted from the database.

            user: A user entity that is passed in to check if the given user has the needed permissions to 
            be able to delete an organizaiton.
            
        Returns:
            Nothing.

        Raises:
            Exception: An error occured when trying to delete the organization to the database.        

            UserPermissionError: An error occured when trying to edit an organization due to improper user 
            permissions.
        """

        user_query = select(UserEntity).where(UserEntity.id == user.id)
        user_entity: UserEntity = self._session.scalar(user_query)
        action = 'organization.delete_organization'
        resource = '/{organization.name}'
        
        if self._permission.check(user_entity, action, resource):
            query = select(OrganizationEntity).where(OrganizationEntity.name == organization_name)
            organization_entity: OrganizationEntity = self._session.scalar(query)
            if organization_entity is None:
                raise Exception("No organization with that name was found! (must be exact)")
            else:
                self._session.delete(organization_entity)
                self._session.commit()
        else:
            raise UserPermissionError(action, resource)        

    def add_member_to_organization(self, organization_name: str, user: UserEntity) -> User | None:
        """Adds a member to an organization in the database.
        
        Args:
            organization_name: A string of the organization name the caller wants to add the user to
            in order for them to become a member.
            
            user: A user entity model representing the desired user that the caller wants to add to an organizaiton.

        Returns:
            The passed in user, or nothing if an error occurs.

        Raises:
            Exception:  An error occured trying to find the specified organization from the given organization_name.

            UserPermissionError: An error occured when trying to add a user that is not the current user.
        """

        organization_query = select(OrganizationEntity).where(OrganizationEntity.name == organization_name)
        organization_entity: OrganizationEntity = self._session.scalar(organization_query)
        if organization_entity is None:
            raise Exception("No organization with that name was found! (must be exact)")
        else:
            user_to_add = self._session.scalar(select(UserEntity).where(UserEntity.id == user.id))
            if user_to_add.pid != user.pid:
                raise UserPermissionError("add", "other user")
            else:
                organization_entity.users.append(user_to_add)
                self._session.commit()
        return user

    def delete_member_from_organization(self, organization_name: str, user: UserEntity) -> None:
        """Deletes a member from a given organizaiton in the database.
        
        Args:
            organization_name: A string of the organization name the caller wants to delete the user from.
            
            user: A user entity model representing the desired user that the caller wants to delete from an organizaiton.

        Returns:
            Nothing.

        Raises:
            Exception: An error occured trying to find the specified organization from the given organization_name.

            UserPermissionError: An error occured when trying to delete a user that is not the current user
        """
        
        organization_query = select(OrganizationEntity).where(OrganizationEntity.name == organization_name)
        organization_entity: OrganizationEntity = self._session.scalar(organization_query)
        if organization_entity is None:
            raise Exception("No organization with that name was found! (must be exact)")
        else:
            user_query = select(UserEntity).where(UserEntity.id == user.id)
            user_entity: UserEntity = self._session.scalar(user_query)
            if user_entity.pid != user.pid:
                raise UserPermissionError("delete", "other user")
            else:
                organization_entity.users.remove(user_entity)
                self._session.commit()

    def get_organization_members(self, organization_name: str) -> list[User]:
        """Fetches all the members that belong to a given organizaiton.
        
        Args:
            organization_name: A string of the organization name the caller wants to retrieve the members of.
            
        Returns:
            A list of the users that belong to a specific organization.
            
        Raises:
            Exception: An error occured trying to find the specified organization from the given organization_name.
        """

        organization_query = select(OrganizationEntity).where(OrganizationEntity.name == organization_name)
        organization_entity: OrganizationEntity = self._session.scalar(organization_query)
        users = organization_entity.users
        user_models = []
        if organization_entity is None:
            raise Exception("No organization with that name was found! (must be exact)")
        else:
            for user in users:
                user_models.append(UserEntity.to_model(user))
        return user_models