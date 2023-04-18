"""Member routes are used by the applicaiton to interact with user objects and how they interact with organizaitons

"""

from fastapi import APIRouter, Depends, HTTPException
from ..services import UserService, OrganizationService
from ..models import User, organization
from .authentication import registered_user

api = APIRouter(prefix="/api/{organization_name}/member")

@api.post("/add", response_model=User, tags=['Organization'])
def add_member_to_organization(organization_name: str, user: User, organization_svc: OrganizationService = Depends()):
    try:
        return organization_svc.add_member_to_organization(organization_name, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api.get("/all", response_model=list[User], tags=['Organization'])
def get_organization_members(organization_name: str, organization_svc: OrganizationService = Depends()):
    return organization_svc.get_organization_members(organization_name)
