"""Event services are used by the applicaiton to provide the functionality for the application to manipulate the database accordingly.

Please see .api/event for more details.
"""

from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models.event import Event
from ..entities import OrganizationEntity, EventEntity
from ..entities import EventEntity
from .permission import PermissionService


__authors__ = ["Jackson Davis, Antonio Tudela"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class EventService:

    _session: Session
    _permission: PermissionService

    def __init__(self, session: Session = Depends(db_session), permission: PermissionService = Depends()):
        self._session = session
        self._permission = permission

    def get_event_details(self, event_id: int) -> Event | None:
        """Fetches event details from the database.
    
        Args:
            event_id: The id for a given event that the caller wants details from.

        Returns:
            A model of an event entity for the frontend to display details about,
            or, nothing in the event of an exception.

        Raises:
            Exception: An error occured when trying to find an event with the given event it.
        """
        
        query = select(EventEntity).where(EventEntity.id == event_id)
        event_entity = self._session.scalar(query)
        if event_entity is None:
            raise Exception("No event with that event id was found! Please try again")
        else:
            model = event_entity.to_model()
            return model

    def get_all_events(self) -> list[Event]:
        """Fetches all the events from the database.
        
        Args:
            None
        
        Returns:
            A list of event models of event entities to be used at some point in the future.
        """

        query = select(EventEntity)
        events = self._session.scalars(query)
        event_models = []
        for ev in events:
            if ev:
                model = ev.to_model()
                event_models.append(model)
        return event_models

    def get_organization_events(self, organization_name: str) -> list[Event] | None:
        """Fetches all events associated with an organization from the database.
        
        Args:  
            organization_name: A name of an organization that the caller is trying to grab events for.
            
        Returns:
            A list of event models of event entities to be displayed for an organizaiton.
            
        Raises:
            Exception: An error occured when trying to grab the organizaiton name from the database.
        """

        # get the associated organization entity to find its id
        organization_query = select(OrganizationEntity).where(OrganizationEntity.name == organization_name)
        organization_entity = self._session.scalar(organization_query)
        if organization_entity is None:
            raise Exception("No organization with that name was found! (must be exact)")
        organization_id = organization_entity.id
        # get the event entities using the organization id 
        events_query = select(EventEntity).where(EventEntity.organization_id == organization_id).order_by(EventEntity.date_time.asc())
        events = self._session.scalars(events_query)
        event_models = []
        for ev in events:
            if ev:
                model = ev.to_model()
                event_models.append(model)
        return event_models

    def delete_event(self, event_id: int) -> None:
        """Deletes an event from the database.
        
        Args:
            event_id: The id of an event that the caller wants to delete.
            
        Returns:
            Nothing.
        
        Raises:
            Exception: An error occured when trying to find an event with the given event id.
        """

        query = select(EventEntity).where(EventEntity.id == event_id)
        event_entity = self._session.scalar(query)
        if event_entity is None:
            raise Exception("No event with that event id was found! Please try again")
        else:
            self._session.delete(event_entity)
            self._session.commit()

    def edit_event(self, event: Event) -> Event | None:
        """Edits an event in the database.
        
        Args:
            An event model that contains the updated fields the caller wants to use.
            
        Returns:
            The event that was passed in with updated fields.
            
        Raises:
            Exception: An error occured when trying to find the an event with the supplied event's id field.
        """

        query = select(EventEntity).where(EventEntity.id == event.id)
        event_entity: EventEntity = self._session.scalar(query)
        if(event_entity is None):
            raise Exception("An event with that ID cannot be found! Please try again.")
        else:
            event_entity.name = event.name
            event_entity.description = event.description
            event_entity.date_time = event.date_time
            event_entity.location = event.location
            event_entity.image = event.image
            self._session.commit()
            return event
        
    def create_event(self, event: EventEntity) -> Event | None:
        """Creates an event and adds it to the database.
        
        Args:
            An event entity that the caller wants added to the database.
            
        Returns:
            An event model of the desired event to add.
        """

        event_to_add = EventEntity.from_model(event)
        self._session.add(event_to_add)
        self._session.commit()
        return event