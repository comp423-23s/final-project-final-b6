from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models.event import Event
from ..entities import OrganizationEntity, EventEntity
from ..entities import EventEntity
from .permission import PermissionService

class EventService:

    _session: Session
    _permission: PermissionService

    def __init__(self, session: Session = Depends(db_session), permission: PermissionService = Depends()):
        self._session = session
        self._permission = permission

    def get_all_events(self) -> list[Event]:
        query = select(EventEntity)
        events = self._session.scalars(query)
        event_models = []
        for ev in events:
            if ev:
                model = ev.to_model()
                event_models.append(model)
        return event_models

    def get_organization_events(self, organization_name: str) -> list[Event] | None:
        # get the associated organization entity to find its id
        organization_query = select(OrganizationEntity).where(OrganizationEntity.name == organization_name)
        organization_entity = self._session.scalar(organization_query)
        if organization_entity is None:
            raise Exception("No organization with that name was found! (must be exact)")
        organization_id = organization_entity.id
        # get the event entities using the organization id 
        events_query = select(EventEntity).where(EventEntity.organization_id == organization_id)
        events = self._session.scalars(events_query)
        event_models = []
        for ev in events:
            if ev:
                model = ev.to_model()
                event_models.append(model)
        return event_models