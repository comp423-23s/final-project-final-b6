from fastapi import APIRouter, Depends, HTTPException
from ..services import UserService, OrganizationService
from ..models.organization import Organization
from .authentication import registered_user

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