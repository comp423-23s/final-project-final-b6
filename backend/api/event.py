from fastapi import APIRouter, Depends, HTTPException
from ..services import UserService, EventService
from ..models.event import Event
from .authentication import registered_user

api = APIRouter(prefix="/api/{organization_name}/events")

    
@api.get("", response_model=list[Event], tags=['Event'])
def get(organization_name: str, event_svc: EventService = Depends()):
    try:
        return event_svc.get_organization_events(organization_name)  
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))