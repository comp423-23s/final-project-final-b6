"""Organization routes are used by the application to interact with organizations associated with UNC.

The application mainly interacts with the functions in this file by the way of get requests used to
display organizations, a post request to create an organization, a patch request to edit an existing 
organization, and a delete request to delete a specified organiztion.

Routes in this file are pre-fixed with an endpoint of: "/api/organizations".
"""

from fastapi import APIRouter, Depends, HTTPException
from ..services import UserService, OrganizationService
from ..models.organization import Organization
from ..models.user import User
from .authentication import registered_user


__authors__ = ["Jackson Davis, Antonio Tudela"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


api = APIRouter(prefix="/api/organizations")


@api.get("", response_model=list[Organization], tags=['Organization'])
def get_all_organizations(organization_svc: OrganizationService = Depends()):
    return organization_svc.get_all_organizations()
    
@api.get("/{organization_name}", response_model=Organization, tags=['Organization'])
def get(organization_name, organization_svc: OrganizationService = Depends()):
    try:
        return organization_svc.get(organization_name)  
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@api.post("", response_model=Organization, tags=['Organization'])
def create_organization(organization: Organization, organizaton_svc: OrganizationService = Depends()):
    try:
        return organizaton_svc.create_organization(organization)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@api.patch("/{organization_name}", response_model=Organization, tags=['Organization'])
def edit_organization(organization: Organization, organization_svc: OrganizationService = Depends()):
    try:
        return organization_svc.edit_organization(organization)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@api.delete("/{organization_name}", response_model=None, tags=['Organization'])
def delete_organizaiton(organization_name: str, organization_svc: OrganizationService = Depends()): #may also need to add authorization here so that only admins can delete organizations, unless that will be handled on the frontend
    try:
        return organization_svc.delete_organization(organization_name)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))