from fastapi import Depends
from sqlalchemy import select, or_, func, update
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

    def edit_organization(self, organization: Organization) -> OrganizationEntity | None:
        query = select(OrganizationEntity).where(OrganizationEntity.name == organization.name)
        organization_entity: OrganizationEntity = self._session.scalar(query)
        if organization_entity is None:
            raise Exception("No organization with that name was found! (must be exact)")
        else:
            # the error message says: "detail": "subject table for an INSERT, UPDATE or DELETE expected, 
            # got Organization(id=6, name='1789', overview='string', description='string', image='string').", but im passing in the organization table?
            update(organization).where(OrganizationEntity.name == organization.name).values(OrganizationEntity.id == OrganizationEntity.id,
                                                                                             OrganizationEntity.name == OrganizationEntity.name,
                                                                                             OrganizationEntity.overview == organization.overview,
                                                                                             OrganizationEntity.description == organization.description,
                                                                                             OrganizationEntity.image == organization.description)
            self._session.commit()


        # def edit_organization(self, organization: Organization) -> Organization | None:
    #     query = select(OrganizationEntity).where(OrganizationEntity.name == organization.name)
    #     organization_entity: OrganizationEntity = self._session.scalar(query)
    #     if organization_entity is None:
    #         raise Exception("No organization with that name was found! (must be exact)")
    #     else:
    #         update(organization).where(OrganizationEntity.name == organization_entity.name).values(overview='test')
    #         self._session.commit()



        # def edit_organization(self, organization: Organization) -> Organization:
    #     query = select(OrganizationEntity).where(OrganizationEntity.name == organization.name)
    #     organization_entity: OrganizationEntity = self._session.scalar(query)
    #     if organization_entity is None:
    #         raise Exception("No organization with that name was found! (must be exact)")
    #     else:
    #         entity = self._session.get(OrganizationEntity, organization.name)
    #         entity.update(organization)
    #         self._session.commit()
    #         #return entity.to_model()


    #think need to pass in table model?
    # def edit_organization(self, organization: OrganizationEntity) -> Organization | None:
    #     query = select(OrganizationEntity).where(OrganizationEntity.name == organization.name)
    #     organization_entity: OrganizationEntity = self._session.scalar(query)
    #     if organization_entity is None:
    #         raise Exception("No organization with that name was found! (must be exact)")
    #     else:
    #         print(OrganizationEntity.__table__.columns)
            
    #         organization_to_edit = OrganizationEntity.from_model(organization)
    #         update(organization.to_model()).where(OrganizationEntity.name == organization.name).values(OrganizationEntity.name == organization.name)

           
           
    #         self._session.commit()
