"""Event routes are used by the application to interact with events associated with a given organization.

The application mainly interacts with the functions in this file by the way of get requests used to display events,
a delete request to delete a given event from an organization, a patch request to edit an organization, and a 
post request to create an event for an organization.

Routes in this file are pre-fixed with an endpoint of: "/api/{organization_name}/events".
"""

from fastapi import APIRouter, Depends, HTTPException
from ..services import UserService, EventService, UserPermissionError
from ..models.event import Event
from ..models.user import User
from .authentication import registered_user


__authors__ = ["Jackson Davis, Antonio Tudela"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


api = APIRouter(prefix="/api/{organization_name}/events")

    
@api.get("", response_model=list[Event], tags=['Event'])
def get(organization_name: str, event_svc: EventService = Depends()):
    try:
        return event_svc.get_organization_events(organization_name)  
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api.get("/{event_id}", response_model=Event, tags=['Event'])
def get(event_id: int, event_svc: EventService = Depends()):
    try:
        return event_svc.get_event_details(event_id)  
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


@api.delete("/{event_id}", response_model=None, tags=['Event'])
def delete_event(event_id: int, event_svc: EventService = Depends(), subject: User = Depends(registered_user)):
    try:
        return event_svc.delete_event(event_id, subject)
    except UserPermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@api.patch("/{event_id}", response_model=Event, tags=['Event'])
def edit_event(event: Event, event_svc: EventService = Depends(), subject: User = Depends(registered_user)):
    try:
        return event_svc.edit_event(event, subject)
    except UserPermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@api.post("", response_model=Event, tags=['Event'])
def create_event(event: Event, event_svc: EventService = Depends(), subject: User = Depends(registered_user)):
    try:
        return event_svc.create_event(event, subject)
    except UserPermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))