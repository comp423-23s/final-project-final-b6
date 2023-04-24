"""Member routes are used by the applicaiton to interact with user objects and how they interact with organizaitons.

The application mainly interacts with the funcitons in this file by the way of a post request to add a member to an 
organization, as well as a get request to return a list of all the members of a given organization.

Routes in this file are pre-fixed with an endpoint of "/api/{organization_name}/members"
"""

from fastapi import APIRouter, Depends, HTTPException
from ..services import UserService, OrganizationService, UserPermissionError
from ..models import User, organization
from .authentication import registered_user


__authors__ = ["Jackson Davis, Antonio Tudela"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


api = APIRouter(prefix="/api/{organization_name}/members")


@api.post("/add", response_model=User, tags=['Organization'])
def add_member_to_organization(organization_name: str, user: User, organization_svc: OrganizationService = Depends()):
    try:
        return organization_svc.add_member_to_organization(organization_name, user)
    except UserPermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@api.get("", response_model=list[User], tags=['Organization'])
def get_organization_members(organization_name: str, organization_svc: OrganizationService = Depends()):
    return organization_svc.get_organization_members(organization_name)

@api.delete("/delete", response_model=None, tags=['Organization'])
def delete_member_from_organization(organization_name: str, user: User, organization_svc: OrganizationService = Depends()):
    try:
        return organization_svc.delete_member_from_organization(organization_name, user)
    except UserPermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))